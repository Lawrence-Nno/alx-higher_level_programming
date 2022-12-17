def roman_to_int(roman_string):
    val = 0
    count = 0
    length = len(roman_string)
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if not isinstance(roman_string, str):
        return 0
    for a in list(roman_string):
        if a not in roman_dict:
            return 0

    for a in list(roman_string):
        if count < length - 1:
            if roman_dict[list(roman_string)[count]] < roman_dict[list(roman_string)[count + 1]]:
             val -= roman_dict[a]
            else:
                val += roman_dict[a]
        else:
            val += roman_dict[a]
        count = count + 1

    return val
