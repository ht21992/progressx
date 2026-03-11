from __future__ import annotations

import sys
import threading
import time
from dataclasses import dataclass, field
from typing import Protocol

from .utils import is_tty, terminal_width


class Renderable(Protocol):
    def render(self) -> str: ...


@dataclass
class ProgressManager:
    refresh_rate: float = 0.1
    stream: object = sys.stdout
    enabled: bool = True

    items: list[Renderable] = field(default_factory=list)
    _running: bool = False
    _thread: threading.Thread | None = None
    _lock: threading.Lock = field(default_factory=threading.Lock)

    def add(self, item: Renderable) -> Renderable:
        with self._lock:
            self.items.append(item)
        return item

    def remove(self, item: Renderable) -> None:
        with self._lock:
            if item in self.items:
                self.items.remove(item)

    def start(self) -> None:
        if not self.enabled:
            return

        if self._running:
            return

        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        if not self.enabled:
            return

        self._running = False
        if self._thread:
            self._thread.join(timeout=1.0)
            self._thread = None
        self._clear_block()

    def _loop(self) -> None:
        while self._running:
            self.render()
            time.sleep(self.refresh_rate)

    def _supports_live_render(self) -> bool:
        return self.enabled and is_tty()

    def _truncate(self, text: str) -> str:
        width = terminal_width()
        if len(text) <= width:
            return text
        return text[: max(0, width - 3)] + "..."

    def render(self) -> None:
        with self._lock:
            lines = [self._truncate(item.render()) for item in self.items]

        if not self._supports_live_render():
            return

        if not lines:
            return

        output = "\x1b[?25l"
        output += "\r"
        output += "\x1b[J"
        output += "\n".join(lines)
        output += f"\x1b[{len(lines)-1}A" if len(lines) > 1 else ""

        self.stream.write(output)
        self.stream.flush()

    def _clear_block(self) -> None:
        if not self._supports_live_render():
            return

        with self._lock:
            line_count = len(self.items)

        if line_count <= 0:
            self.stream.write("\x1b[?25h")
            self.stream.flush()
            return

        output = "\r\x1b[J"
        if line_count > 1:
            for _ in range(line_count - 1):
                output += "\n\x1b[J"
            output += f"\x1b[{line_count - 1}A"
        output += "\x1b[?25h"
        self.stream.write(output)
        self.stream.flush()

    def print(self, message: str) -> None:
        if self._supports_live_render():
            with self._lock:
                line_count = len(self.items)

            self.stream.write("\r\x1b[J")
            if line_count > 1:
                for _ in range(line_count - 1):
                    self.stream.write("\n\x1b[J")
                self.stream.write(f"\x1b[{line_count - 1}A")
            self.stream.write(message + "\n")
            self.stream.flush()
        else:
            self.stream.write(message + "\n")
            self.stream.flush()

    def __enter__(self) -> "ProgressManager":
        self.start()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.stop()
