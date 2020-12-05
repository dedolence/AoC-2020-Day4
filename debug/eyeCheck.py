import re
"""
Checks the validity of eye colors:
Valid: exactly one of: amb blu brn gry grn hzl oth
"""
checks = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth",
    "blue",
    "4mb",
    "BLU"
]



for c in checks:
    finds = c in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    print(finds)