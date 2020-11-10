import doctest


class FizzBuzz:
    def game(self, num):
        """
        >>> myGame = FizzBuzz()
        >>> myGame.game(10)
        'Buzz'
        >>> myGame.game(27)
        'Fizz'
        >>> myGame.game(90)
        'FizzBuzz'
        >>> myGame.game(7)
        '7'
        >>> myGame.game(True)
        Traceback (most recent call last):
          File "C:\Program Files\JetBrains\PyCharm 2020.2.3\plugins\python\helpers\pycharm\docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest zadanie1_fizzbuzz.FizzBuzz.game[5]>", line 1, in <module>
            myGame.game(True)
          File "C:/Users/dell/testowanieLab6/Lab06/zadanie1_fizzbuzz.py", line 31, in game
            raise Exception("Error in FizzBuzz")
        Exception: Error in FizzBuzz
        >>> myGame.game(11.123)
        '11.123'
        >>> myGame.game("abc")
        Traceback (most recent call last):
          File "C:\Program Files\JetBrains\PyCharm 2020.2.3\plugins\python\helpers\pycharm\docrunner.py", line 138, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest zadanie1_fizzbuzz.FizzBuzz.game[7]>", line 1, in <module>
            myGame.game("15")
          File "C:/Users/dell/testowanieLab6/Lab06/zadanie1_fizzbuzz.py", line 32, in game
            if num % 5 == 0 and num % 3 != 0 and num % 15 != 0:
        TypeError: not all arguments converted during string formatting
        """


        if num % 5 == 0 and num % 3 != 0 and num % 15 != 0:
            return "Buzz"
        elif num % 3 == 0 and num % 5 != 0 and num % 15 != 0:
            return "Fizz"
        elif num % 15 == 0:
            return "FizzBuzz"
        elif num % 5 != 0 and num % 15 != 0 and num % 3 != 0 and (type(num) == int or type(num) == float):
            return str(num)
        else:
            raise Exception("Error in FizzBuzz")


if __name__ == "__main__":
    doctest.testmod(extraglobs={'myGame': FizzBuzz()})

