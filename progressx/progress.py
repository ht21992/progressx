from __future__ import annotations

from dataclasses import dataclass, field

from .utils import clamp, format_seconds, now

from .colors import bcolors


@dataclass
class ProgressBar:
    total: int
    label: str = ""
    width: int = 30
    show_percent: bool = True
    show_count: bool = True
    show_eta: bool = True
    fill_char: str = "█"
    empty_char: str = "░"
    color: str = ""

    current: int = 0
    start_time: float = field(default_factory=now)
    finished: bool = False

    def update(self, step: int = 1) -> None:
        if self.finished:
            return

        self.current += step
        if self.current >= self.total:
            self.current = self.total
            self.finished = True

    def set(self, value=int) -> None:
        if self.finished:
            return

        self.current = max(0, min(value, self.total))
        if self.current >= self.total:
            self.finished = True

    def percent(self) -> float:
        if self.total <= 0:
            return 100.0
        return clamp((self.current / self.total) * 100.0, 0.0, 100.0)

    def ratio(self) -> float:
        if self.total <= 0:
            return 100.0
        return clamp(self.current / self.total, 0.0, 100.0)

    def elapsed(self) -> float:
        return now() - self.start_time

    def eta(self) -> str:
        if self.current <= 0 or self.finished:
            return "00:00"

        elapsed = self.elapsed()
        per_item = elapsed / self.current
        remaining = (self.total - self.current) * per_item
        return format_seconds(remaining)

    def bar(self) -> str:
        filled = int(round(self.width * self.ratio()))
        empty = max(0, self.width - filled)
        return f"{self.fill_char * filled}{self.empty_char * empty}"

    def render(self) -> str:
        parts: list[str] = []

        verified_color = bcolors.WHITE
        if self.color:
            verified_color = bcolors.get_color_code(self.color)

        if self.label:
            parts.append(self.label)

        parts.append(f"[{self.bar()}]")

        if self.show_percent:
            parts.append(f"{self.percent():6.2f}%")

        if self.show_count:
            parts.append(f"{self.current}/{self.total}")

        if self.show_eta:
            if self.finished:
                parts.append("ETA 00:00")
            else:
                parts.append(f"ETA {self.eta()}")

        text = " ".join(parts)
        return f"{verified_color}{text}{bcolors.ENDC}"

    def finish(self) -> None:
        self.current = self.total
        self.finished = True
