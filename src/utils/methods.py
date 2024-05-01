def input_list() -> list[int]:
    print("Enter a list")
    result = []
    while True:
        try:
            n = int(input("if you want to stop enter a letter, else enter a number to the list: "))
            result.append(n)
        except ValueError:
            break
    print("You have enter:\n\t{0}".format(result))
    return result
