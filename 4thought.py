
operators = [' + ', ' - ', ' * ' , ' // ']

solutions = {}

for one in operators:
    for two in operators:
        for three in operators:
            val_str = "4{:s}4{:s}4{:s}4".format(one, two, three)
            val = eval(val_str)
            solutions[val] = val_str.replace('//', '/') + " = {:d}".format(val)

for i in range(0, int(input())):
    m = int(input())
    if m not in solutions or m > 256:
        print("no solution")
    else:
        print(solutions[m])
               
