def anyalnum(s):
    countal = 0
    countnu = 0
    for i in s:
        if 97<= ord(i) <=122:
            countal = countal+1
        elif 65<= ord(i) <=90:
            countal = countal+1
        elif 48<= ord(i) <=57:
            countnu = countnu+1

    if countal>0 or countnu>0:
        return True
    else:
        return False

def anyalpha(s):
    countal = 0
    for i in s:
        if 97<= ord(i) <=122:
            countal = countal+1
        elif 65<= ord(i) <=90:
            countal = countal+1

    if countal>0:
        return True
    else:
        return False

def anydigit(s):
    countnu = 0
    for i in s:
        if 48<= ord(i) <=57:
            countnu = countnu+1

    if countnu>0:
        return True
    else:
        return False

def anylower(s):
    count = 0
    for i in s:
        if 97<= ord(i) <=122:
            count = 1
            break
    if count == 1:
        return True
    else:
        return False

def anyupper(s):
    count = 0
    for i in s:
        if 65<= ord(i) <=90:
            count = 1
            break
    if count == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    s = input()
    print(anyalnum(s))
    print(anyalpha(s))
    print(anydigit(s))
    print(anylower(s))
    print(anyupper(s))
