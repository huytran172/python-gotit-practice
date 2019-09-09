import re

number_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

def text_number_conversion(sentence):
    """
        function(str) -> str
        
        str format: I completed {number_of_sessions} sessions and I rated my expert {number_of_stars} stars
        number of sessions is [1, 2, 3, ..., 9]
        number of sessions is [one, two, ...,  five]

        Return a sentence with the following format
        I completed {number_of_sessions} sessions and I rated my expert {number_of_stars} stars
        number_of_sessions is converted to str
        number_of_stars is converted to int
    """

    # Search for characters between two strings to get the number of sessions and stars
    number_of_sessions = int(re.search(r"completed (.*) sessions", sentence).group(1));
    number_of_stars = re.search(r"expert (.*) stars", sentence).group(1);

    if number_of_sessions in number_dict:
        number_of_sessions = number_dict[number_of_sessions]
    else:
        raise Exception("Number of sessions is not valid")

    for key, value in number_dict.items():
        number_of_stars = number_of_stars.lower();
        if value == number_of_stars and key <= 5:
            number_of_stars = key
            break 
    else:
        raise Exception("Number of stars is not valid")

    return "I completed {} sessions and I rated my expert {} stars".format(number_of_sessions, number_of_stars)

print(text_number_conversion("I completed 2 sessions and I rated my expert three stars"))
print(text_number_conversion("I completed 5 sessions and I rated my expert five stars"))
# print(text_number_conversion("I completed 9 sessions and I rated my expert six stars"))
# print(text_number_conversion("I completed 10 sessions and I rated my expert two stars"))