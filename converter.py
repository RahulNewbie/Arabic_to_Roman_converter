
# Global variable section
STANDARD_ARABIC_TO_ROMAN = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),(100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))

# Maximum arabic number to convert to to roman
MAX_NUM_TO_CONVERT = 3999


def convert_arabic_to_roman(arabic_number, is_negative=False):
    # Initiating list for resulting roman number
    result_roman = []
    # Case 1: Check if the number is not an integer
    try:
        int_arab = int(arabic_number)
    except ValueError:
        raise ValueError("Provided Arabic number is not an "
                         "integer, Please provide integer")

    # Case 2: Check if the number is Negative
    if int_arab < 0:
        # Check if is_negative parameter is true
        if is_negative:
            # If user set the parameter is_negative is true and
            # Want to convert negative number to roman then it is a valid case
            # for this reason, get the absolute value of the number
            # The number should be below than the 3999
            # Convert the arabic number to roman and append "-" in front of it

            if abs(int_arab) <= MAX_NUM_TO_CONVERT:
                result_roman.append("-")
                int_arab = abs(int_arab)
            else:
                raise ValueError("Provided number should be below 3999")
        else:
            # If the user didn't set the is_negative parameter as True
            # Then it will be a invalid case. User should get notified
            # regarding the error and rerun with correct parameter
            raise ValueError("Provided number is negative, please rerun"
                             " with \"is_negative = True\" as parameter")

    # Case 3: Check if the number is in the allowed limit
    # If the number is equal to zero or it exceeds the maximum number
    # Then raise an error to show to the user
    if int_arab == 0 or int_arab > MAX_NUM_TO_CONVERT:
        raise ValueError("Provided value should be inside the range of 1 and 3999")
    else:
        # Main code block to convert arabic to roman number
        # here the processing will be done in below steps
        # Step 1. Loop through the tuple of STANDARD_ARABIC_TO_ROMAN
        # and get the arabic number
        # Step 2. Divide the provided number with arabic number and
        # get the result(no_of_times)
        # Step 3. Add corresponding roman character to the result,
        # that many times with the result in previous step.
        # Step 4. Once addition of roman number is done, then
        # deduct the value of no_of_time* arabic number from the provided number
        # Continue the first loop, till it reaches the end of tuple
        # Step 5: Join every roman character in the result list and return

        # Step 1
        for arabic, roman in STANDARD_ARABIC_TO_ROMAN:
            # Step 2
            no_of_time = int_arab//arabic
            # print(no_of_time)
            # Step 3
            for unused_var in range(no_of_time):
                result_roman.append(roman)
            # Step 4
            int_arab -= no_of_time*arabic
        # Step 5
        return "".join(result_roman)
