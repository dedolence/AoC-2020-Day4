import re
"""
Checks the validity of passports:
Valid: a nine-digit number, including leading zeroes.
"""
checks = [
    "000000001",        # valid
    "0123456789",       # invalid
    "186cm",            # invalid
    "012533040",        # true
    "021572410",        # true
    "3556412378",       # invalid
    "087499704",        # valid
    "896056539",        # valid
    "545766238",        # valid
    "093154719"         # valid
]



for c in checks:
    finds = re.match("^[0-9]{9}$", c)
    print(bool(finds))