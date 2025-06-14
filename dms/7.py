def complete(L):
    lgt = len(L)
    flg = 1
    for i in range(lgt):
        for j in range(lgt):
            if i == j:
                if L[i][j] == 0:
                    flg = 1
                else:
                    flg = 0
            else:
                if L[i][j] == 1:
                    flg = 1
                else:
                    flg = 0

    if flg == 0:
        print("GRAPH IS NOT COMPLETE GRAPH")
    else:
        print("GRAPH IS A COMPLETE GRAPH")

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

def adjlist(L):
    l = ["A", "B", "C", "D", "E", "F", "G"]
    lgt = len(L)
    l1 = l[:len(L)]
    flg = 1
    print("VERTEX ADJACENT VERTEX")
    for i in range(lgt):
        print()
        print(l1[i], end=" ")
        for j in range(lgt):
            if i == j:
                if L[i][j] == 0:
                    flg = 1
                else:
                    flg = 0
            else:
                if L[i][j] == 1:
                    flg = 1
                    print(l1[j], end=" ")
                else:
                    flg = 0

def main():
    L = input1()
    complete(L)
    output(L)
    adjlist(L)

main()