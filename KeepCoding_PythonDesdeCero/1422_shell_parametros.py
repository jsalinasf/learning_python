import sys

def area(b, h):
    return (b * h) / 2

# print(len(sys.argv))

# for item in sys.argv:
#     print(item)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        base = float(sys.argv[1])
        altura = float(sys.argv[2])
        print('Area',area(base,altura))
    else:
        base = float(input('Base: '))
        altura = float(input('Altura: '))
        print('Area',area(base,altura))
