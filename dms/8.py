def indeg(L):
    lgt = len(L)
    for i in range(lgt):
        b = 0
        for j in range(lgt):
            if L[i][j] == 1:
                b += 1
        print(i, "OUT DEGREE IS:", b)

def outdeg(L):
    lgt = len(L)
    for i in range(lgt):
        a = 0
        for j in range(lgt):
            if L[j][i] == 1:
                a += 1
        print(i, "IN DEGREE IS:", a)

def output(L):
    lgt = len(L)
    print("THE ADJACENCY MATRIX IS:")
    for i in range(lgt):
        for j in range(lgt):
            print(L[i][j], end=" ")
        print()

def input1():
    L = []
    R = int(input("ENTER THE ORDER: "))
    for i in range(R):
        a = []
        print("ENTER FOR ROWS")
        for j in range(R):
            e = int(input("ENTER THE ELEMENT: "))
            a.append(e)
        L.append(a)
    return L

def main():
    L = input1()
    indeg(L)
    outdeg(L)
    output(L)

main()