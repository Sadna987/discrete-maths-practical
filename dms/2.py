def reflexive(m):
    n = len(m)
    for i in range(n):
        if m[i][i] != 1:
            print("\nNOT REFLEXIVE\n")
            return False
    print("\nREFLEXIVE\n")
    return True

def symmetric(m):
    n = len(m)
    for i in range(n):
        for j in range(n):  # Should iterate over n, not len(m[i])
            if m[i][j] != m[j][i]:
                print("\nNOT SYMMETRIC\n")
                return False
    print("\nSYMMETRIC\n")
    return True

def antisymmetric(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] == m[j][i] and i != j:
                print("\nNOT ANTISYMMETRIC\n")
                return False
    print("\nANTISYMMETRIC\n")
    return True

def transitive(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if m[i][j] and m[j][k] and not m[i][k]:  # Correcting transitivity check
                    print("\nNOT TRANSITIVE\n")
                    return False
    print("\nTRANSITIVE\n")
    return True

def equivalence(m):
    if reflexive(m) and symmetric(m) and transitive(m):
        print("\nEQUIVALENCE RELATION\n")
    else:
        print("\nNOT AN EQUIVALENCE RELATION\n")

def partial(m):
    if reflexive(m) and transitive(m) and antisymmetric(m):
        print("\nPARTIAL ORDERING RELATION\n")
    else:
        print("\nNOT A PARTIAL ORDERING RELATION\n")

def input1():
    m = []
    print("\nENTER MATRIX ELEMENTS ROW BY ROW")
    n = int(input("Enter matrix size (n x n): "))
    for i in range(n):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        if len(row) != n:
            print("Invalid row size! Try again.")
            return input1()
        m.append(row)
    return m

def main():
    while True:
        print("\nMENU:")
        print("1: REFLEXIVE RELATION")
        print("2: SYMMETRIC RELATION")
        print("3: TRANSITIVE RELATION")
        print("4: ANTISYMMETRIC RELATION")
        print("5: EQUIVALENCE RELATION")
        print("6: PARTIAL ORDERING RELATION")
        print("7: EXIT")

        choice = int(input("ENTER YOUR CHOICE: "))
        if choice in range(1, 7):
            matrix = input1()
            if choice == 1:
                reflexive(matrix)
            elif choice == 2:
                symmetric(matrix)
            elif choice == 3:
                transitive(matrix)
            elif choice == 4:
                antisymmetric(matrix)
            elif choice == 5:
                equivalence(matrix)
            elif choice == 6:
                partial(matrix)
        elif choice == 7:
            break
        else:
            print("INVALID CHOICE. TRY AGAIN.")

main()