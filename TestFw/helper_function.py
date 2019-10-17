"""
Provide common helper function
"""


class HelperFunction:
    """
    Helper function for common methods used in all test cases
    """
    def __init__(self):
        pass

    def auto_generate_one_letter_list(self, start_char):
        """
        This method will generate a list of char starting with the passed in value
        :param start_char: start char from a - z
        :return: list
        """
        character_list = []
        first_char = start_char
        counter = 1
        while counter <= 26:
            character_list.append(first_char)
            first_char = chr(ord(first_char) + 1)
            counter += 1
        return character_list

    def auto_generate_two_letter_list(self, start_char):
        """
        This method creates two letter permutation starting with the pass in
        char - z.
        a - z will be appended to each of the letter.
        :param start_char:
        :return: list
        """

        start_char = start_char.lower()

        two_letter_list = []
        list_a = self.auto_generate_one_letter_list(start_char)
        list_b = self.auto_generate_one_letter_list('a')

        for item_in_a in list_a:
            for item_in_b in list_b:
                two_letter_list.append(item_in_a + item_in_b)
            if item_in_a == 'z':
                break
        return two_letter_list
