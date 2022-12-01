from unittest import mock
import builtins
import pytest

from project import get_player_name, get_difficulty, get_data_and_play


def test_get_player_name():
    with mock.patch.object(builtins, "input", lambda _: "1234"):
        assert get_player_name() == "1234"
    with mock.patch.object(builtins, "input", lambda _: "abcd  1234"):
        assert get_player_name() == "abcd  1234"
    with mock.patch.object(builtins, "input", lambda _: "  abcd 1234  "):
        assert get_player_name() == "abcd 1234"
    with mock.patch.object(builtins, "input", lambda _: ""):
        with pytest.raises(SystemExit):
            assert get_player_name()
    with mock.patch.object(builtins, "input", lambda _: "1"):
        with pytest.raises(SystemExit):
            assert get_player_name()
    with mock.patch.object(builtins, "input", lambda _: "abc"):
        with pytest.raises(SystemExit):
            assert get_player_name()
    with mock.patch.object(builtins, "input", lambda _: " 12 "):
        with pytest.raises(SystemExit):
            assert get_player_name()
    with mock.patch.object(builtins, "input", lambda _: "12345 abcde"):
        with pytest.raises(SystemExit):
            assert get_player_name()


def test_get_difficulty():
    with mock.patch.object(builtins, "input", lambda _: "1"):
        playerName = "abcd"
        assert get_difficulty(playerName) == "easy"
    with mock.patch.object(builtins, "input", lambda _: "2"):
        playerName = "abcd"
        assert get_difficulty(playerName) == "medium"
    with mock.patch.object(builtins, "input", lambda _: "3"):
        playerName = "abcd"
        assert get_difficulty(playerName) == "hard"
    with mock.patch.object(builtins, "input", lambda _: "e"):
        playerName = "abcd"
        with pytest.raises(SystemExit):
            assert get_difficulty(playerName)
    with mock.patch.object(builtins, "input", lambda _: "x"):
        playerName = "abcd"
        with pytest.raises(SystemExit):
            assert get_difficulty(playerName)


def test_get_data_and_play():
    difficulty = "easy"
    playerName = "abcd"
    with mock.patch.object(builtins, "input", lambda _: " "):
        assert get_data_and_play(difficulty, playerName) == -50
    with mock.patch.object(builtins, "input", lambda _: "p"):
        assert get_data_and_play(difficulty, playerName) == -50
    for _ in range(10):
        with mock.patch.object(builtins, "input", lambda _: "a"):
            assert (
                get_data_and_play(difficulty, playerName) >= -50
                and get_data_and_play(difficulty, playerName) <= 100
            )
