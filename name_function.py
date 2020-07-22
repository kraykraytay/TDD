def formatted_name(last_name, first_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = last_name + ", " + first_name + " " + middle_name # printing names in a format used for school i.e alphatebical order of surnames 
    else:
        full_name = last_name + ", " + first_name
    return full_name.title()
