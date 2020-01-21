
def cat(path):
    with open(path, 'r') as f:
        data  = f.read()
        f.close()
        print(data)

def head(path, lines):
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()
        for  index in range(lines):
            print(data[index])

def tail(path, lines):
    total = 0
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()
        for count  in data:
            total += 1 
        for index in range(total - lines, total):
            print(data[index])

def grep(path, string):
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()
        for line in data:
            if string in line:
                print(line)


def cut(path, field, separator):
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()
        for line in data:
            count_field = 0
            for char in line:
                if char == separator:
                    count_field += 1
                if count_field == field:
                    print(char,end='')
            print()

def sed(path, before, after):
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()
        with open(path, 'w') as f:
            for line in data:
                for char in line:
                    if char != before:
                        f.write(char)
                    else:
                        f.write(after)
                f.write('\n')
            f.close()

def touch(path):
    with open(path, 'w') as f:
         f.write('')
         f.close()

def hostname():
    with open('/etc/hostname') as f:
        data = f.readline()
        f.close()
        print(data)


