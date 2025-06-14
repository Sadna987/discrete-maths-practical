def permutation(orig, fact):
    n = len(orig)
    ls = []
    for i in range(n):
        a = 1
        for j in range(0, -2, -1):
            l = []
            l.append(orig[i])
            sl = orig[0:i] + orig[i+1:]
            l.extend(sl[j::a])
            a = -1
            ls.append(l)
    return ls

def fact(orig):
    n = len(orig)
    fact = 1
    for i in range(n):
        fact = fact * i
    return fact

def input1():
    l = []
    n = int(input("ENTER THE NO. OF ELEMENTS: "))
    for i in range(n):
        e = int(input("ENTER THE ELEMENT: "))
        l.append(e)
    return l

def main():
    orig = input1()
    fact(orig)
    rslt = permutation(orig, fact)

    print("PERMUTATIONS ARE ")
    for i in range(len(rslt)):
        for j in range(len(rslt[i])):
            print(rslt[i][j], end=" ")
        print()

main()