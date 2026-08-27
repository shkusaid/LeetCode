def simplify_path(path):
    paths = path.split('/')
    Stack = []
    for pth in paths:
        if pth == '' or pth == '.':
            continue
        if pth == '..':
            if Stack:
                Stack.pop()
            continue
        Stack.append(pth)

    return '/' + '/'.join(Stack)

path = '/home/foo/.//documents/..'

print(simplify_path(path))