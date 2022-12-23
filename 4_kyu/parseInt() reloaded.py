"""
DESCRIPTION:
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
"""


nums = {'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90}
mult = {'million': 1000000,
        'thousand': 1000,
        'hundred': 100}


def parse_int(string):
    string = string.replace(' and ', ' ').split()
    result = 0
    for i in mult:
        if i in string:
            result += parse_int(' '.join(string[:string.index(i)])) * mult[i]
            string = string[string.index(i) + 1:]
    for i in string:
        if '-' in i:
            i = i.split('-')
            result += nums[i[0]] + nums[i[1]]
        else:
            result += nums[i]
    return result