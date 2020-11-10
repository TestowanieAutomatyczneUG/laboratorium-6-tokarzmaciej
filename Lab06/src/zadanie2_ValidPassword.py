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
        """
        if type(password) != str:
            raise TypeError("Wrong type")


class ValidPasswordTest(unittest.TestCase):
    def setUp(self):
        self.temp = ValidPassword()

    def test_type_password(self):
        self.assertRaises(TypeError, self.temp.checkPassword, False)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    doctest.testmod(extraglobs={'validate': ValidPassword()})