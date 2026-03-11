from progressx.spinner import Spinner


def test_spinner_render():
    s = Spinner(label="Working")
    text = s.render()
    assert "Working" in text


def test_spinner_success():
    s = Spinner(label="Working")
    s.succeed("done")
    assert "done" in s.render()
    assert "✔" in s.render()
