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

def other_id_not_none():
    row = "C00629618|N|TER|P|201701230300133512|15C|IND|PEREZ, JOHN A|LOS ANGELES|CA|90017|PRINCIPAL|DOUBLE NICKEL ADVISORS|01032017|40|H6CA34245|SA01251735122|1141239|||2012520171368850783"
    return ParseData.parse_row(row)

def valid_row():
    row = "C00177436|N|M2|P|201702039042410893|15|IND|WATJEN, THOMAS R.|KEY LARGO|FL|330375267|UNUM|CHAIRMAN OF THE BOARD|01042017|5000||40373239|1147350|||4020820171370029334"
    return ParseData.parse_row(row)

def no_cmte_id():
    row = "|N|M2|P|201702039042410893|15|IND|WATJEN, THOMAS R.|KEY LARGO|FL|330375267|UNUM|CHAIRMAN OF THE BOARD|01042017|5000||40373239|1147350|||4020820171370029334"
    return ParseData.parse_row(row)

def no_transaction_amt():
    row = "C00177436|N|M2|P|201702039042410893|15|IND|WATJEN, THOMAS R.|KEY LARGO|FL|330375267|UNUM|CHAIRMAN OF THE BOARD|01042017|||40373239|1147350|||4020820171370029334"
    return ParseData.parse_row(row)

def neg_transaction_amt():
    row = "C00177436|N|M2|P|201702039042410893|15|IND|WATJEN, THOMAS R.|KEY LARGO|FL|330375267|UNUM|CHAIRMAN OF THE BOARD|01042017|-5000||40373239|1147350|||4020820171370029334"
    return ParseData.parse_row(row)

def invalid_date_in_row():
    row = "C00177436|N|M2|P|201702039042410893|15|IND|WATJEN, THOMAS R.|KEY LARGO|FL|330375267|UNUM|CHAIRMAN OF THE BOARD|04312017|5000||40373239|1147350|||4020820171370029334"
    return ParseData.parse_row(row)

def invalid_zip_in_row():
    row = "C00177436|N|M2|P|201702039042410893|15|IND|WATJEN, THOMAS R.|KEY LARGO|FL|3a0375267|UNUM|CHAIRMAN OF THE BOARD|01042017|5000||40373239|1147350|||4020820171370029334"
    return ParseData.parse_row(row)

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

class TestParseRow(unittest.TestCase):
    def test_other_id_not_none(self):
        self.assertEqual(other_id_not_none(), None)
    
    def test_valid_row(self):
        row = valid_row()
        self.assertEqual(row["CMTE_ID"], 'C00177436')
        self.assertEqual(row["ZIP_CODE"], '33037')
        self.assertEqual(row["TRANSACTION_DT"], '01042017')
        self.assertEqual(row["date_key"], '20170104')
        self.assertEqual(row["TRANSACTION_AMT"], 5000)
    
    def test_no_cmte_id(self):
        self.assertEqual(no_cmte_id(), None)
    
    def test_no_transaction_amt(self):
        self.assertEqual(no_transaction_amt(), None)
    
    def test_neg_transaction_amt(self):
        self.assertEqual(neg_transaction_amt(), None)
    
    def test_invalid_date_in_row(self):
        row = invalid_date_in_row()
        self.assertEqual(row["CMTE_ID"], 'C00177436')
        self.assertEqual(row["ZIP_CODE"], '33037')
        self.assertEqual(row["TRANSACTION_DT"], '04312017')
        self.assertEqual(row["date_key"], None)
        self.assertEqual(row["TRANSACTION_AMT"], 5000)
    
    def test_invalid_zip_in_row(self):
        row = invalid_zip_in_row()
        self.assertEqual(row["CMTE_ID"], 'C00177436')
        self.assertEqual(row["ZIP_CODE"], None)
        self.assertEqual(row["TRANSACTION_DT"], '01042017')
        self.assertEqual(row["date_key"], '20170104')
        self.assertEqual(row["TRANSACTION_AMT"], 5000)

if __name__ == "__main__":
    unittest.main()