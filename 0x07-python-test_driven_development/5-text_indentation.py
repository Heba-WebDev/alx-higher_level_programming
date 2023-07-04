#!/usr/bin/python3

""" Text indentation """


def text_indentation(text):
    """Indentates text.

        Args:
        text: string

        Returns:
        string: The full string indentated

        Raises:
        TypeError: If text ist not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])

    print(text, end="")
