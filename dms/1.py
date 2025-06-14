def input1():
    L = []
    ans = "y"
    while ans.lower() == "y":
        e = int(input("ENTER THE ELEMENT: "))
        L.append(e)
        ans = input("CONTINUE? Y/N: ")
    return L

def ismember():
    l1 = input1()
    num = int(input("ENTER A NUMBER: "))
    print("THE SET IS", l1)
    if num in l1:
        print("NUMBER FOUND IN SET")
        return True
    else:
        print("NUMBER NOT FOUND IN SET")
        return False

def powerset():
    l1 = input1()
    list1 = [[]]  # Start with empty set
    for elem in l1:
        list1 += [subset + [elem] for subset in list1]
    print("THE POWER SET IS:", list1)
    return list1

def subset():
    l2 = sorted(input1())
    list1 = powerset()
    if l2 in list1:
        print("IS A SUBSET")
        return True
    else:
        print("NOT A SUBSET")
        return False

def union():
    l1 = input1()
    l2 = input1()
    l3 = list(set(l1) | set(l2))  # Union using set operations
    print("UNION IS", l3)
    return l3

def intersection():
    l1 = sorted(input1())
    l2 = sorted(input1())
    l3 = list(set(l1) & set(l2))  # Intersection using set operations
    print("INTERSECTION IS", l3)
    return l3

def complement():
    l1 = sorted(input1())
    u = sorted(input1())  # Universal set
    l3 = [x for x in u if x not in l1]
    print("COMPLEMENT IS", l3)
    return l3

def setdiff():
    l1 = sorted(input1())
    l2 = sorted(input1())
    l3 = list(set(l1) - set(l2))  # Difference using set operations
    print("SET DIFFERENCE IS", l3)
    return l3

def symmdiff():
    l1 = sorted(input1())
    l2 = sorted(input1())
    l3 = list(set(l1) ^ set(l2))  # Symmetric Difference using set operations
    print("SYMMETRIC DIFFERENCE IS", l3)
    return l3

def cartesian():
    l1 = sorted(input1())
    l2 = sorted(input1())
    l3 = [(a, b) for a in l1 for b in l2]
    print("CARTESIAN PRODUCT IS", l3)
    return l3

def main():
    while True:
        print("\nMENU:")
        print("1: MEMBERSHIP")
        print("2: POWER SET")
        print("3: SUBSET")
        print("4: UNION")
        print("5: INTERSECTION")
        print("6: COMPLEMENT")
        print("7: SET DIFFERENCE")
        print("8: SYMMETRIC DIFFERENCE")
        print("9: CARTESIAN PRODUCT")
        print("10: EXIT")

        choice = int(input("ENTER YOUR CHOICE: "))
        if choice == 1:
            ismember()
        elif choice == 2:
            powerset()
        elif choice == 3:
            subset()
        elif choice == 4:
            union()
        elif choice == 5:
            intersection()
        elif choice == 6:
            complement()
        elif choice == 7:
            setdiff()
        elif choice == 8:
            symmdiff()
        elif choice == 9:
            cartesian()
        elif choice == 10:
            break
        else:
            print("INVALID CHOICE. TRY AGAIN.")

main()