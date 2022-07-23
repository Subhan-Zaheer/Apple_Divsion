"""Apple division"""

def Apple_div(n, min, max):
    """

    :param n: Number of Apples
    :param min: starting of range of student.
    :param max: ending of range of student.
    This code will calculate if the number of Apples will be divided equally in given number of students or not.
    Number of Students are in given range.
    """
    for i in range(min, max + 1):
        if n % i == 0:

            print("\n")
            print(f"Your \"{n}\" number of Apples will be equally distributed in \"{i}\" students.")
            print(f"Each student will get \"{int(n / i)}\" Apple/s.")
            print("\n")

        elif n % i != 0:
            mod = n % i
            quotient = int(n / i)

            print("\n")
            print(f"Your \"{n}\" number of Apples not distributed equally in \"{i}\" students."
                  f"\"{mod}\" Apple/s will be remaining.")
            print(f"Each student got \"{quotient}\" Apples")
            print(f"If we will have \"{i - mod}\" apple/s more than we will be able to equally distribute the Apples."
                  f"After that each student will have \"{quotient + 1}\"")
            print("\n")


if __name__ == '__main__':
    n = int(input("Enter total number of apples : "))
    print("Now you have to enter range of people to distribute the apples between them.")
    min = int(input("Enter start of range : "))
    max = int(input("Enter end of range : "))
    Apple_div(n, min, max)