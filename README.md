# progressx

Lightweight CLI progress bars, spinners, and task manager for Python.

## Features

- Progress bars
- Spinners
- Colored bars and spinners
- Multiple live tasks
- Clean terminal rendering
- No third-party runtime dependencies

## Installation

```bash
pip install progressx
```

### Quick start

```
from progressx import ProgressBar
import time

bar = ProgressBar(total=100, label="Upload")

for _ in range(100):
    bar.update()
    print("\r" + bar.render(), end="", flush=True)
    time.sleep(0.02)

print()

```

## Spinner

```from progressx import Spinner
import time

spinner = Spinner(label="Loading")

for _ in range(20):
    spinner.tick()
    print("\r" + spinner.render(), end="", flush=True)
    time.sleep(0.1)

spinner.succeed("done")
print("\r" + spinner.render())
```

## Progress manager

```
from progressx import ProgressBar, Spinner, ProgressManager
import time

with ProgressManager() as manager:
    spinner = manager.add(Spinner(label="Preparing"))
    bar = manager.add(ProgressBar(total=50, label="Download"))

    for i in range(50):
        spinner.tick()
        if i == 10:
            spinner.succeed("ready")
        bar.update()
        time.sleep(0.05)
```

## CLI demo

```
progressx demo
```

---

# How to run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip pytest build
python -m pip install -e .

```

Run tests:

```
pytest
```

Run demo:

```
progressx demo
```

### Example usage

Simple progress bar

```
import time
from progressx import ProgressBar

bar = ProgressBar(total=20, label="Export")

for _ in range(20):
    bar.update()
    print("\r" + bar.render(), end="", flush=True)
    time.sleep(0.1)

print()
```

### Multiple tasks

```
import time
from progressx import ProgressBar, Spinner, ProgressManager

with ProgressManager(refresh_rate=0.05) as manager:
    prepare = manager.add(Spinner(label="Preparing"))
    files = manager.add(ProgressBar(total=30, label="Files"))
    rows = manager.add(ProgressBar(total=50, label="Rows", color="blue"))

    for i in range(50):
        prepare.tick()
        if i == 8:
            prepare.succeed("done")

        if i < 30:
            files.update()

        rows.update()
        time.sleep(0.06)
```

## License

MIT
