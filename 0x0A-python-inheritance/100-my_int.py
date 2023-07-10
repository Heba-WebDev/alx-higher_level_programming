#!/usr/bin/python3
"""
Class MyInt
"""


class Square(int):
    """
    Inherits from int
    """

    def __eq__(self, num):
        """Rebal == """
        return super().__ne__(num)

    def __ne__(self, num):
        """Rebal != """
        return super().__eq__(num)
