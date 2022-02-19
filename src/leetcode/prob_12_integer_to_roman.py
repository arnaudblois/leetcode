"""Leetcode 012  - Convert an integer up to 3999 into its Roman form."""


CONVERT_DICT = [
    {
        "0": "",
        "1": "I",
        "2": "II",
        "3": "III",
        "4": "IV",
        "5": "V",
        "6": "VI",
        "7": "VII",
        "8": "VIII",
        "9": "IX",
    },
    {
        "0": "",
        "1": "X",
        "2": "XX",
        "3": "XXX",
        "4": "XL",
        "5": "L",
        "6": "LX",
        "7": "LXX",
        "8": "LXXX",
        "9": "XC",
    },
    {
        "0": "",
        "1": "C",
        "2": "CC",
        "3": "CCC",
        "4": "CD",
        "5": "D",
        "6": "DC",
        "7": "DCC",
        "8": "DCCC",
        "9": "CM",
    },
    {
        "1": "M",
        "2": "MM",
        "3": "MMM",
    },
]


def convert_to_roman(num: int) -> str:
    """Convert an integer to its Roman form.

    Input is assumed to be in [1; 3999].
    """
    converted_num = []
    for index, digit in enumerate(str(num)[::-1]):
        converted_num.append(CONVERT_DICT[index][digit])
    return "".join(converted_num[::-1])
