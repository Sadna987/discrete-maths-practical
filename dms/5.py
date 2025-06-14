def func():
    c = [4, 2, 9]  # Coefficients
    l = []
    n = int(input("ENTER THE VALUE OF n: "))
    x = [n**2, n, 1]  # Expression components

    print("\nf(n) = 4n² + 2n + 9")
    print(f"f({n}) =", end=" ")

    result = 0
    for i in range(3):
        term = c[i] * x[i]
        l.append(term)
        result += term
        print(f"{c[i]}({x[i]})", end=" ")

    print(f"= {result}")  # Displays the final computed value

func()