def is_natural_number(my_number):
    if isinstance(my_number, int):
        if my_number < 0:
            return False
        else:
            return True
    else:
        return False

print(is_natural_number(10))