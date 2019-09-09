from enums import Session
from exceptions import InvalidValueException

class Step:
    

    def __init__(self, number_of_sessions: int, number_of_stars: str):
        """
            number of sessions is any in [1, 2, 3, ..., 9]
            number of stars is any in [one, two, ...,  five]
        """

        if 1 <= number_of_sessions <= 9:
            self.number_of_sessions = number_of_sessions
        else:
            raise InvalidValueException("Invalid number of sessions")
        
        if number_of_stars.lower() in Session.VALID_STARS_STRING:
            self.number_of_stars = number_of_stars
        else:
            raise InvalidValueException("Invalid input for stars")


    def make_step(self):
        """
            print a sentence with the following format
            I completed {number_of_sessions} sessions and I rated my expert {number_of_stars} stars
            number_of_sessions is converted to str
            number_of_stars is converted to int
        """

        if self.number_of_sessions in Session.NUMBER_TO_TEXT_MAP:
            sessions_converted_str = Session.NUMBER_TO_TEXT_MAP[self.number_of_sessions]
        else:
            raise InvalidValueException("Number of sessions is not valid")

        for key, value in Session.NUMBER_TO_TEXT_MAP.items():
            if value == self.number_of_stars.lower():
                stars_converted_int = key
                break 
        else:
            raise InvalidValueException("Number of stars is not valid")

        print(f"I completed {sessions_converted_str} sessions and I rated my expert {stars_converted_int} stars")

if __name__ == '__main__':
    try:
        valid_step = Step(5, "three")
        valid_step.make_step()
        valid_step.make_step()
        # Step(0, "five").make_step()
        Step(2, "six").make_step()
    except InvalidValueException as e:
        print(e)
