from name_function import formatted_name

print("Please enter the first and last name or enter x to E[x]it.")

while True:
    first_name = input("please enter the first name")
    if first_name == "x":
        print("Goodbye.")
        break

    middle_name = input("please enter the middle name")
    if middle_name == "x":
        print("Goodbye.")
        break

    last_name = input("Please enter the last name.")
    if last_name == "x":
        print("Goodbye.")
        break 

    result = formatted_name(last_name, first_name, middle_name)
    print("formatted name is: " + result + ".")
