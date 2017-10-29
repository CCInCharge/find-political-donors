import unittest
import src.ParseData as ParseData

def empty_zip():
    return ParseData.valid_zip('')

def none_zip():
    return ParseData.valid_zip(None)

def valid_zip():
    return ParseData.valid_zip("24125")

def valid_zeroes_zip():
    return ParseData.valid_zip("00000")

def short_zip():
    return ParseData.valid_zip("4361")

def invalid_symbols():
    return ParseData.valid_zip("9339a")

def spaces_zip():
    return ParseData.valid_zip(" 9458")

def empty_date():
    return ParseData.valid_date('')

def none_date():
    return ParseData.valid_date(None)

def date_too_short():
    return ParseData.valid_date("1102017")

def dashes():
    return ParseData.valid_date("01-10-2017")

def invalid_date():
    return ParseData.valid_date("04312017")

def invalid_leap():
    return ParseData.valid_date("02292017")

def valid_leap():
    return ParseData.valid_date("02292016")

def valid_date():
    return ParseData.valid_date("10302017")

class TestValidZip(unittest.TestCase):
    def test_empty_zip(self):
        self.assertEqual(empty_zip(), None)
    
    def test_none_zip(self):
        self.assertEqual(none_zip(), None)
    
    def test_valid_zip(self):
        self.assertEqual(valid_zip(), "24125")
    
    def test_valid_zeroes_zip(self):
        self.assertEqual(valid_zeroes_zip(), "00000")
    
    def test_short_zip(self):
        self.assertEqual(short_zip(), None)
    
    def test_invalid_symbols(self):
        self.assertEqual(invalid_symbols(), None)

    def test_spaces_zip(self):
        self.assertEqual(spaces_zip(), None)

class TestValidDate(unittest.TestCase):
    def test_empty_date(self):
        self.assertEqual(empty_date(), None)
    
    def test_none_date(self):
        self.assertEqual(none_date(), None)
    
    def test_date_too_short(self):
        self.assertEqual(date_too_short(), None)
    
    def test_dashes(self):
        self.assertEqual(dashes(), None)
    
    def test_invalid_date(self):
        self.assertEqual(invalid_date(), None)
    
    def test_invalid_leap(self):
        self.assertEqual(invalid_leap(), None)
    
    def test_valid_leap(self):
        self.assertEqual(valid_leap(), "20160229")

    def test_valid_date(self):
        self.assertEqual(valid_date(), "20171030")

if __name__ == "__main__":
    unittest.main()