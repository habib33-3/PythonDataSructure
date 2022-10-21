import math


def egyptian_frac(numerator, denominator):
    egypt_list = []

    while numerator != 0:
        x = math.ceil(denominator / numerator)
        egypt_list.append(x)

        numerator = x * numerator - denominator
        denominator *= x

    string = ""

    for ones in egypt_list:
        string += "1/{0} + ".format(ones)

    final_string = string[:-3]

    return final_string


print(egyptian_frac(7, 31))
