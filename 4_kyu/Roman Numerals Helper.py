"""
DESCRIPTION:
Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
It should follow the API demonstrated in the examples below.
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
"""


class RomanNumerals:
    digs = {'M': 1000, 'CM': 900,'D': 500,
            'CD': 400, 'C': 100, 'XC': 90,
            'L': 50, 'XL': 40, 'X': 10,
            'IX': 9, 'V': 5, 'IV': 4, 'I':1}

    def to_roman(val):
        res = ''
        for k, v in RomanNumerals.digs.items():
            while val >= v:
                res += k
                val -= v
        return res

    def from_roman(roman_num):
        res = 0
        for i in range(len(roman_num) - 1):
            if RomanNumerals.digs[roman_num[i]] < RomanNumerals.digs[roman_num[i + 1]]:
                res -= RomanNumerals.digs[roman_num[i]]
            else:
                res += RomanNumerals.digs[roman_num[i]]
        res += RomanNumerals.digs[roman_num[-1]]
        return res