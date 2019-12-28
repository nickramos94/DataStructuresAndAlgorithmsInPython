num = ''
op = ''
current = ['0']
print(0)

while True:
    print(current, op)
    a = input()
    try:
        int(a)
        if op == '':
            if len(current) == 1:
                current[0] += a
            else:
                current = [a]
        else:
            current[1] += a
    except ValueError:
        if a == 'reset':
            op = ''
            current =['0']
            print(0)
        elif a == 'clear':
            if len(current) == 1:
                current[0] == '0'
            else:
                current[1] == '0'
        elif len(current) == 1:
            current.append('')
            op = a
        elif current[1] == '':
            op = a
        else:
            if op == '+':
                b = int(current[0]) + int(current[1])
            if op == '*':
                b = int(current[0]) * int(current[1])
            if op == '-':
                b = int(current[0]) - int(current[1])
            if op == '/':
                b = int(current[0]) / int(current[1])
            if op == '//':
                b = int(current[0]) // int(current[1])
            if op == '%':
                b = int(current[0]) % int(current[1])
            print(b)
            if a == '=':
                op = ''
            else:
                op = a
            current = [str(b),'']
