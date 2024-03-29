ERROR_MESSAGE = 'Wrong one or two arguments'


def string_concatenate(string_1, string_2):
    if not isinstance(string_1, str) or not isinstance(string_2, str):
        return ERROR_MESSAGE
    return string_1 + string_2


def test_passing():
    assert string_concatenate("abcd", "efgh") == "abcdefgh"


def test_failing():
    assert string_concatenate("abcd", "efgh") != "efghabcd"


def test_invalid_data():
    assert string_concatenate(123, 'abcd') == ERROR_MESSAGE
    assert string_concatenate('efgh', 456) == ERROR_MESSAGE


if __name__ == '__main__':
    test_passing()
    test_failing()
    test_invalid_data()
