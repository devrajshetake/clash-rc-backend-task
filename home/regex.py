import re
from typing import Pattern

def is_email_valid(email):
    regex = r'[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-]{2,}'
    pattern = re.compile(regex)
    valid = re.fullmatch(pattern, email)
    if valid is not None:
        return True
    else:
        return False


def find_numbers(txt):
    # pattern = f'-?\d+\.?\d*'
    pattern = r'(-?\d+)(\.?\d)?(\d*)'
    matches = re.finditer(pattern, txt)
    lst =[]
    for match in matches:
        s = match.start()
        e = match.end()
        lst.append(txt[s:e])
    return lst

def is_mac_valid(mac):
    regex = (r'([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})|'+
             r'([0-9a-fA-F]{2}[-]){5}([0-9a-fA-F]{2})|'+
             r'(([0-9a-fA-F]{3}\.){3}([0-9a-fA-F]{3}))')
    pattern = re.compile(regex)
    valid = re.search(pattern, mac)
    if valid is not None:
        return True
    else:
        return False

def extract_quotes(txt):
    regex = r"'[^']+'"
    matches = re.finditer(regex, txt)
    lst =[]
    for match in matches:
        s = match.start()
        e = match.end()
        lst.append(txt[s:e])
    return lst

def is_ip_valid(ip):
    general = r'(((25[0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9]?[0-9]))\.){2}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))(\s*)$'
    classA = r'^(\s*)((((1[0-1][0-9])|(12[0-7])|([1-9]?[0-9]))\.)'
    classB = r'^(\s*)((((12[8-9])|(1[3-8][0-9])|(19[0-1]))\.)'
    classC = r'^(\s*)((((2[0-1][0-9])|(22[0-3])|(19[2-9]))\.)'
    classD = r'^(\s*)((((22[4-9])|(23[0-9]))\.)'
    classE = r'^(\s*)((((24[0-9])|(25[0-5]))\.)'

    lst =[]
    if re.search(classA+general, ip) is not None:
        lst.append(f'{ip} is a valid IP Address, and is of Class A')
    elif re.search(classB+general, ip) is not None:
        lst.append(f'{ip} is a valid IP Address, and is of Class B')
    elif re.search(classC+general, ip) is not None:
        lst.append(f'{ip} is a valid IP Address, and is of Class C')
    elif re.search(classD+general, ip) is not None:
        lst.append(f'{ip} is a valid IP Address, and is of Class D')
    elif re.search(classE+general, ip) is not None:
        lst.append(f'{ip} is a valid IP Address, and is of Class E')
    else:
        lst.append(f'INVALID IP')
    return lst

def extract_date(url):
    regex = r'(\d{4})-(0[1-9]|1[0-2])-(([0-2][0-9]|[3][0-1])[^0-9])'
    matches = re.finditer(regex, url)
    lst =[]
    for match in matches:
        s = match.start()
        e = match.end()
        lst.append(url[s:e])
    return lst

def CamelTo_snake(txt):
    # regex = r'([A-Z][a-z]+)([A-Z][a-z]+)'
    CamelCase =r'^(\s*)((([a-zA-Z][a-z]+)|\d+)(([A-Z][a-z]+)|\d+)+)(\s*)$'
    valid = re.search(CamelCase, txt)
    if valid is None:
        return ["Not a valid CamelCase"]
    regex = r'([a-z0-9])([A-Z])'
    ans = (re.sub(regex, r'\1_\2', txt)).lower()
    lst = [ans]
    return lst


# DevrajShetake IsIn 2d2d222ndYe


#  fshgsfhgdchg gfhdjhg 'devraj' gsvhgvh "fshghfhgfd"

# txt = """10 1.5 -12.6 -12 4568726 56.6365 12. For extracting numbers, if the string is "My roll number is 75, i am in 2nd year", then we have to output [75, 2] right?? 0-9 45."""

#3D:F2:C9:A6:B3:4F  3D-F2-C9-A6-B3-4F 3df.acb.abc.abc

# ip addresses 666.1.2.2 192.168.0.1 666.1.2.2 25.99.208.255  

# genral = ((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){2}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])
# classA = (((1[0-1][0-9])|(12[0-7])|([1-9]?[0-9]))\.)
# classB(128-191)



