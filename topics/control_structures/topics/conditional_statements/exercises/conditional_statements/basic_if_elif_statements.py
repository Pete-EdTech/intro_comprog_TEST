# basic_if_elif_statements.py

def check_number(number):
    # Comparing the number to determine its nature
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    number = int(input("Enter an integer: "))
    result = check_number(number)
    print(result)

if __name__ == "__main__":
    main()

# end of code