import unittest
import doctest


class ValidPassword:
    def checkPassword(self, password):
        """
        >>> validate=ValidPassword()
        >>> validate.checkPassword(False)
        Traceback (most recent call last):
          File "C:\Program Files\JetBrains\PyCharm 2020.2.3\plugins\python\helpers\pycharm\docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest zadanie2_ValidPassword.ValidPassword.checkPassword[1]>", line 1, in <module>
            validate.checkPassword(False)
          File "C:/Users/dell/testowanieLab6/Lab06/src/zadanie2_ValidPassword.py", line 11, in checkPassword
            raise TypeError("Wrong type")
        TypeError: Wrong type
        >>> validate.checkPassword("abc")
        'Too short length, at least 8 characters'
        >>> validate.checkPassword('AaBcCdDeEfF')
        False
        >>> validate.checkPassword('abcdefgh')
        False
        >>> validate.checkPassword('ABc123abc')
        False
        >>> validate.checkPassword('abc123abc')
        False
        >>> validate.checkPassword('A?B123abc@')
        True
        """
        if type(password) != str:
            raise TypeError("Wrong type")
        if len(password) < 8:
            return 'Too short length, at least 8 characters'
        capitalLetter = False
        containNumber = False
        containSpecialChar = False
        for letter in password:
            number = "0123456789"
            special_char = '!*(){}[]\@#-+=_`$%^&~|:";\'<>?,./'
            if letter.isupper():
                capitalLetter = True
            if letter in number:
                containNumber = True
            if letter in special_char:
                containSpecialChar = True
        if containNumber and capitalLetter == containNumber and capitalLetter == containSpecialChar:
            return True
        else:
            return False


class ValidPasswordTest(unittest.TestCase):
    def setUp(self):
        self.temp = ValidPassword()

    def test_type_password(self):
        self.assertRaises(TypeError, self.temp.checkPassword, False)

    def test_password_length(self):
        self.assertEqual('Too short length, at least 8 characters', self.temp.checkPassword("abc"))

    def test_password_capital_letter1(self):
        self.assertEqual(self.temp.checkPassword('AaBcCdDeEfF'), False)

    def test_password_capital_letter2(self):
        self.assertEqual(self.temp.checkPassword('abcdefgh'), False)

    def test_password_without_special_char_positive(self):
        self.assertEqual(self.temp.checkPassword('ABc123abc'), False)

    def test_password_without_special_char_negative(self):
        self.assertEqual(self.temp.checkPassword('abc123abc'), False)

    def test_password_ACCEPT(self):
        self.assertEqual(self.temp.checkPassword('A?B123abc@'), True)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    doctest.testmod(extraglobs={'validate': ValidPassword()})
