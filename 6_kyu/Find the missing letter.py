"""
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input
and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing.
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""

from string import ascii_letters as al


def find_missing_letter(chars):
    result = al[al.find(chars[0]) + 1:al.find(chars[-1])]
    for i in result:
        if i not in chars:
            return i