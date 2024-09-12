def main():
    userInput = input("What's you wanna say? ")
    print(playback(userInput))


def playback(userInput):
    return '...'.join(userInput.split())

main()