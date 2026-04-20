# log_b(y) = x
# y = b^x

base = 3
y = 80
digits_past_decimal = 8


def find_starting_value(log_base, exponent_value):
    placeholder_log_base = log_base
    placeholder_exponent_value = exponent_value
    power_increment = 0
    negative = False

    if log_base == exponent_value:
        return 1
    
    if exponent_value == 1:
        return 0

    if exponent_value < 1:
        placeholder_exponent_value = 1 / exponent_value
        negative = True
        # Because log_b(y^a) = a * log_b(y),
        # log_b(1/y) = -log_b(y)
    
    if placeholder_exponent_value > log_base:

        while placeholder_log_base < placeholder_exponent_value:
            power_increment += 1
            placeholder_log_base = log_base ** power_increment

    if negative:
        power_increment= power_increment * -1

    if placeholder_log_base == placeholder_exponent_value:
        return power_increment
    elif negative:
        power_increment += 1
    elif exponent_value < log_base:
        return power_increment
    else:
        power_increment -= 1

    # Because of the very silly way I wrote this function
    # if the number exists it has a special case

    return power_increment

def find_difference(log_base, check_value, target_value):
    
    if target_value < 1:
        target_value = 1 / target_value
    
    difference = target_value - log_base ** check_value
    return difference

def log(base, y, digits_past_decimal):
    value = find_starting_value(base, y)
    negative = False

    if value < 0:
        negative = True
        value = value * -1

    for n in range(0, digits_past_decimal + 1):
        stored_add_number = 0

        if y == 1:
            value = 0
            break

        if y == base:
            value = 1
            break

        for digit in range(1, 10):

            add_number = digit * (10 ** (n * -1))
            check = value + add_number

            difference = find_difference(base, check, y)

            if difference < 0:
                value += stored_add_number
                break
            else:
                stored_add_number = add_number

            if digit == 9:
                value += add_number

    if negative:
        value = value * -1

    value = round(value, digits_past_decimal)

    return value

        