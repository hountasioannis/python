def main():
    sum = 0
    mul = 1

    upper_bound = int(input("give an int: "))

    for i in range(1, upper_bound + 1):
        sum += 1
        mul *= 1

    print(f"{sum:,}, {mul:,}")

main()