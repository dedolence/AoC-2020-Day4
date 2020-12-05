import re



def check2(passport):
    def tempFunc(v):
        print("temporary function")

    """
    # convert to dict
    pDict = {}
    for pair in passport:
        pDict[pair[0]] = pair[1]
    """
    KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    keyChecks = {
        'byr': lambda v : int(v) >= 1920 and int(v) <= 2002,
        'iyr': lambda v : int(v) >= 2010 and int(v) <= 2020,
        'eyr': lambda v : int(v) >= 2020 and int(v) <= 2030,
        'hgt': lambda v : bool(re.match("^(1[5-8][0-9]|19[0-3])(cm)$|^(59|6[0-9]|7[0-6])(in)$", v))
        }

    # what passport looks like now:
    # [('xxx', 'xxxxx'), ('xxx', 'xxxxxxx'), ('xxx', 'xxxxxxx')]
    for pair in passport:
        # what pair looks like now:
        # ('xxx', 'xxxxxx')
        k = pair[0]     # 'xxx'
        v = pair[1]     # 'xxxxxxxx'
        if not keyChecks[k](v):
            return False
    
    return True

passports = [
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', '140cm')],
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', '155cm')],
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', '175cm')],
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', '165')],
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', '76in')],
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', '46in')],
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', '102in')],
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', '100')],
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', 'cmin')],
    [('byr', '1920'), ('iyr', '2012'), ('eyr', '2025'), ('hgt', '189cm')]
]

for p in passports:    
    if check2(p):
        print("Passed")
    else:
        print("failed")