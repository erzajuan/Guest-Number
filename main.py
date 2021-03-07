import random


def main():
    range = int(input("Set The Range to Guest   : "))
    answer = random.randint(0, range)
    while True:
        guest = int(input("Your Guest   : "))
        if guest == answer:
            print("Correct! The Answer is ", answer)
            break
        if guest > answer:
            print("Too Big!, try again")
        if guest < answer:
            print("To small!, ty again")


if __name__ == '__main__':
    main()
