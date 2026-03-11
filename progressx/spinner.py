from __future__ import annotations


from dataclasses import dataclass, field
from .utils import now
from .colors import bcolors


@dataclass
class Spinner:
    label: str = ""
    frames: tuple[str, ...] = ("|", "/", "-", "\\")
    interval: float = 0.1

    index: int = 0
    last_tick: float = field(default_factory=now)
    finished: bool = False
    success_symbol: str = "✔"
    fail_symbol: str = "✖"
    done_message: str | None = None
    failed: bool = False
    color: str = ""

    def tick(self) -> None:
        if self.finished:
            return

        current_time = now()
        if current_time - self.last_tick >= self.interval:
            self.index = (self.index + 1) % len(self.frames)
            self.last_tick = current_time

    def render(self) -> str:

        verified_color = bcolors.WHITE
        if self.color:
            verified_color = bcolors.get_color_code(self.color)

        if self.finished:
            symbol = self.fail_symbol if self.failed else self.success_symbol
            if self.done_message:
                return (
                    f"{verified_color}{symbol} {self.label} {self.done_message}{bcolors.ENDC}".strip()
                )
            return f"{verified_color}{symbol} {self.label}{bcolors.ENDC}".strip()

        return f"{verified_color}{self.frames[self.index]} {self.label}{bcolors.ENDC}".strip()

    def succeed(self, message: str | None = None) -> None:
        self.finished = True
        self.failed = False
        self.done_message = message

    def fail(self, message: str | None = None) -> None:
        self.finished = True
        self.failed = True
        self.done_message = message
