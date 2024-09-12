def main():
    userInput = input("What's the value in kg say? ")
    print(einstein(userInput))


def einstein(userInput):
    m = int(userInput)
    c= 300000000
    return m*c**2

main()