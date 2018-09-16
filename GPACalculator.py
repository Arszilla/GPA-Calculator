classes = {}
grade_letters = {"AA": 4.0,
                 "BA": 3.5,
                 "BB": 3.0,
                 "CB": 2.5,
                 "CC": 2.0,
                 "DC": 1.5,
                 "DD": 1.0,
                 "FD": 0.0,
                 "FF": 0.0}


def class_collect():
    print("Please input the number of classes:" + "\n")
    while True:
        class_amount = input("> ")
        print("")
        if class_amount.isdecimal():
            class_amount = int(class_amount)
            break
        else:
            print("Please input a number." + "\n")
            continue

    a = 1
    while a <= class_amount:
        print("Please input the class's name:" + "\n")
        class_name = input("> ")
        print("")

        print("Please input the credit for {}:".format(class_name) + "\n")
        while True:
            class_credit = input("> ")
            print("")
            if class_credit.isdecimal():
                class_credit = int(class_credit)
                break
            else:
                print("Please input a number." + "\n")
                continue

        print("Please input your letter grade for {}:".format(class_name) + "\n")
        print("WARNING:")
        print("Possible grades are: AA, BA, BB, CB, CC, DC, DD, FD, FF" + "\n")
        while True:
            class_grade = input("> ")
            print("")
            if class_grade.isalpha() and len(class_grade) == 2:
                if class_grade in grade_letters.keys():
                    break
                else:
                    print("Please make sure that you are submitting a valid letter grade." + "\n")
            else:
                print("Please make sure your keyword does not have any spaces, numbers or symbols in it." + "\n")
                continue

        classes[class_name] = (class_credit, class_grade)

        a = a + 1

    print(calculate(classes, grade_letters))


def calculate(classes, grade_letters):
    class_values = classes.values()
    return sum([int(credit) * grade_letters[grade] for credit, grade in class_values]) / sum([int(credit) for credit, grade in class_values])


if __name__ == '__main__':
    class_collect()
