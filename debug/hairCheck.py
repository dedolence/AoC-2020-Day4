import re
"""
Checks the validity of hair colors:
Valid: a # followed by exactly six characters 0-9 or a-f.
"""
checks = [
    "#4bd3eb",
    "#a078b7",
    "#e821cd",
    "#c6a4f9",
    "#a80c63",
    "#8adeb3",
    "#f29180",
    "#33d794",
    "#a78452",
    "#75cec0"
]



for c in checks:
    print(c, re.match('^#([0-9]|[a-f]){6}$', c.lower()))