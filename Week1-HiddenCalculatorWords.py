flipped_numbers = {
    1: "I",
    2: "Z",
    3: "E",
    4: "H",
    5: "S",
    6: "G",
    7: "L",
    8: "B",
    9: "-",
    0: "O",
}


def turn_calc(number):
    """
    This function takes a number as input and returns the word that is spelled out when the number is flipped upside down.
    Numbers with a leading 0 need to be passed as strings due to the way Python handles leading zeros.
    """
    output = "".join(
        [flipped_numbers[int(digit)] for digit in str(number) if digit.isdigit()]
    ).upper()[::-1]
    return output


test_cases = [707, 5508, 3045, "07734"]

for test in test_cases:
    print(f"Input: {test} Output: {turn_calc(test)}")
