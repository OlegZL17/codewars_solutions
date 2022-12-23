"""
DESCRIPTION:
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized.
The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    result = text.replace('_', ' ').replace('-', ' ').split()
    try:
        for i in range(1, len(result)):
            result[i] = result[i].capitalize()
        return ''.join(result)
    except:
        return ''