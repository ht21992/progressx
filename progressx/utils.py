from __future__ import annotations
import shutil
import sys
import time


def terminal_width(default: int = 80) -> int:
    try:
        return shutil.get_terminal_size((default, 20)).columns
    except Exception:
        return default


def is_tty() -> bool:
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def clamp(value: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(maximum, value))


def format_seconds(seconds: float) -> str:
    seconds = max(0, int(seconds))
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    if hours:
        return f"{hours:d}:{minutes:02d}:{sec:02d}"
    return f"{minutes:02d}:{sec:02d}"


def now() -> float:
    return time.perf_counter()
