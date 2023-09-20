import unittest
import lesson

class FizzbuzzTestCase(unittest.TestCase):

    def test_fizz(self):
        number = 3
        result = lesson.getReply(number) # Fizz
        self.assertEqual(result,'Fizz')

    def test_buzz(self):
        number = 5
        result = lesson.getReply(number) # Buzz
        self.assertEqual(result,'Buzz')

    def FizzBuzz(self):
        number = 15
        result = lesson.getReply(number) # Fizzbuzz
        self.assertEqual(result,'FizzBuzz')
    
if __name__ == '__main__':
    unittest.main()