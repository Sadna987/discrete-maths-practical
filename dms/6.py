def complete(L):
    lgt = len(L)
    for i in range(lgt):
        for j in range(lgt):
            if i == j and L[i][j] != 0:  # Diagonal should be 0
                print("\nGRAPH IS NOT COMPLETE\n")
                return False
            elif i != j and L[i][j] != 1:  # Non-diagonal should be 1
                print("\nGRAPH IS NOT COMPLETE\n")
                return False
    print("\nGRAPH IS A COMPLETE GRAPH\n")
    return True

def output(L):
    lgt = len(L)
    print("\nTHE ADJACENCY MATRIX IS:")
    for i in range(lgt):
        print(" ".join(map(str, L[i])))  # Cleaner matrix display

def input1():
    L = []
    R = int(input("ENTER THE ORDER OF MATRIX: "))
    print("\nENTER MATRIX ROW BY ROW:")
    for i in range(R):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != R:
            print("Invalid row size! Try again.")
            return input1()
        L.append(row)
    return L

def main():
    L = input1()
    output(L)
    complete(L)

main()