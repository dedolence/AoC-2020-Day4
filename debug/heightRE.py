import re
"""
Checks the validity of height measurements.
Valid heights must be a number followed by 'cm' or 'in'.
If 'cm': number must be between 150 and 193 inclusive
if 'in': number must be between 59 and 76 inclusive
"""
checks = [
    "149cm",     # Calse
    "150cm",     # True
    "175cm",     # True
    "193cm",     # True
    "194cm",     # False
    "58in",      # False
    "59in",      # True
    "65in",      # True
    "76in",      # True
    "77in",      # False
    ]


check1 = '^(1[5-8][0-9]|19[0-3])(cm)$'  # between 150-193cm
check2 = '^(59|6[0-9]|7[0-6])(in)$'     # between 59-76in

# hgtRE = "%s|%s" % (check1, check2)

hgtRE = "^(1[5-8][0-9]|19[0-3])(cm)$|^(59|6[0-9]|7[0-6])(in)$"

for c in checks:
    finds = re.match("^(1[5-8][0-9]|19[0-3])(cm)$|^(59|6[0-9]|7[0-6])(in)$", c)
    print(bool(finds))