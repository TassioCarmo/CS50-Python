def main():
    userInput = input("What's you wanna say? ")
    print(indoorVoice(userInput))


def indoorVoice(userInput):
    return userInput.lower()

main()