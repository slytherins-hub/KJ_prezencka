def is_whole_number(my_number):
    if isinstance(my_number, float):
        return False
    else:
        return True

print(is_whole_number(10))