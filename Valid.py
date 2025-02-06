import re

# never used python before btw
class Valid:
    """
    Validate a ZIP code. return true if the input is a valid ZIP,
    false otherwise.

    input: string
    output: boolean

    TODO: implement a method to validate a ZIP code
    """

    @staticmethod
    def zip(input):
        zip_pattern = "^[0-9]{5}(?:-[0-9]{4})?$"  # stinky regex -- 5 digits, optional dash and 4 digits
        if re.match(zip_pattern, input) == None:
            return False
        else:
            return True

    # not sure how to ensure the ZIP code is real but this validates the format

    """
  Validate a Phone Number. return true if the input is a valid Phone number, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a Phone Number
  """

    @staticmethod
    def phone(input):
        phone_pattern = "^\+[0-9]{1,3} \([0-9]{3}\) [0-9]{3}-[0-9]{4}$" # more stinky regex
        if re.match(phone_pattern, input) == None:
            return False
        else:
            return True
