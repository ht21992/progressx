from progressx.progress import ProgressBar


def test_progress_percent():
    p = ProgressBar(total=10, label="Test")
    p.update(5)
    assert p.percent() == 50.0


def test_progress_finish():
    p = ProgressBar(total=3)
    p.update(3)
    assert p.finished is True
    assert p.current == 3


def test_progress_render_contains_label():
    p = ProgressBar(total=10, label="Upload")
    assert "Upload" in p.render()
