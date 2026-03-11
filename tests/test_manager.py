import io

from progressx.manager import ProgressManager
from progressx.progress import ProgressBar


def test_manager_add_remove():
    stream = io.StringIO()
    manager = ProgressManager(stream=stream, enabled=False)
    bar = ProgressBar(total=10)

    manager.add(bar)
    assert len(manager.items) == 1

    manager.remove(bar)
    assert len(manager.items) == 0


def test_manager_print():
    stream = io.StringIO()
    manager = ProgressManager(stream=stream, enabled=False)
    manager.print("hello")
    assert "hello" in stream.getvalue()
