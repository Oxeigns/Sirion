import importlib.util
from pathlib import Path
import pytest

spec = importlib.util.spec_from_file_location(
    "formatters", Path(__file__).resolve().parents[1] / "bot" / "utils" / "formatters.py"
)
formatters = importlib.util.module_from_spec(spec)
spec.loader.exec_module(formatters)

time_to_seconds = formatters.time_to_seconds
seconds_to_min = formatters.seconds_to_min


def test_time_to_seconds():
    assert time_to_seconds("01:30") == 90


@pytest.mark.parametrize(
    "seconds,expected",
    [
        (None, "-"),
        (90, "01:30"),
        (61, "01:01"),
        (3661, "01:01:01"),
        (90061, "01:01:01:01"),
    ],
)
def test_seconds_to_min(seconds, expected):
    assert seconds_to_min(seconds) == expected
