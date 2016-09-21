import unittest 
from examples import *



class TestExamples(unittest.TestCase):




    def test(self):


        self.assertEqual(True, True)


    def test_get_winner_tie(self):
        a="A"
        b="B"
        result=get_winner(a, 3, b, 3)  
        self.assertEqual(result, a + " " + b)



    def test_get_winner_a(self):
        a= "A"
        b= "B"
        result=get_winner(a, 3, b, 2)
        self.assertEqual(result, a)





























if __name__ == '__main__':
    unittest.main()