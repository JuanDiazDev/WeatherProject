import unittest
import City
import Codes


class Tests(unittest.TestCase):
    def testCity_not_found(self):
        test = City.City('ParangacutirimicuaroASDFGLJ')
        res = test.get_weather()
        self.assertEqual(res, 'Weather unavailable')

    def testCodes(self):
        test = Codes.Codes('airportcodes.csv')
        res = test._CODES['CUU']
        self.assertEqual(res, 'Chihuahua')

    def testCache(self):
        test = City.City('Chihuahua')
        res = test.get_weather()
        self.assertEqual(res, test.dic['Chihuahua'])

if __name__ == '__main__':
    unittest.main()
