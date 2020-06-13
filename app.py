#
# Custom exponent function: the base x and the exponent or power y
#


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print("Base: 3, Power: 7 = " + str(raise_to_power(3, 7)))
print("Base: 5, Power: 9 = " + str(raise_to_power(5, 9)))
print("Base: 2, Power: 13 = " + str(raise_to_power(2, 13)))
