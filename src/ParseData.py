"""
Provides functionality for parsing data that is read in from FEC, as well as
handling some erroneous data.
"""

from datetime import datetime

def valid_zip(zip):
    """
    Given a string, verifies if it contains a valid zip code or not. If 
    valid, returns the 5-digit zip code. If not, returns None.

    :param zip: String representation of a value which may or may not be a
                valid zip code
    :returns  : 5-digit zip code if valid, None if not.
    """
    if not zip:
        return None
    if len(zip) < 5:
        return None
    if " " in zip:
        return None
    if len(zip) > 5:
        zip = zip[0:5]
    try:
        int(zip)
    except ValueError:
        return None
    return zip

def valid_date(date):
    """
    Given a string, verifies if it contains a valid date or not. If 
    valid, returns a string in the format Year Month Day (with no spaces).
    If invalid, returns None. The output format is helpful for maintaining
    a SortedDict where keys are arranged chronologically.

    :param date: String representation of a value which may or may not be a
                 valid date
    :returns:    Date in Year Month Day format if valid, None if invalid.
    """
    if not date:
        return None
    if len(date) != 8:
        return None
    try:
        date = datetime.strptime(date, '%m%d%Y')
        date_key = date.strftime('%Y%m%d')
    except ValueError:
        return None
    return date_key


def parse_row(row):
    """
    Given a row from the input text data stream, parses out relevant data
    fields. If CMTE_ID or TRANSACTION_AMT in the original data are empty,
    returns None (as this data is not to be used for any downstream
    calculation). If OTHER_ID is not empty, returns None, for the same reason.
    Otherwise, returns a dict with the parsed data.

    :param row: One row of data from input data stream
    :returns:   None if CMTE_ID or TRANSACTION_AMT are empty. None if OTHER_ID
                is not empty. Otherwise, dict with the following keys:
                CMTE_ID:         Raw data, ID of the recipient
                ZIP_CODE:        5-digit zip code of the sender, None if zip
                                 code was invalid in raw data
                TRANSACTION_DT:  Raw transaction date
                date_key:        If TRANSACTION_DT is a valid date, the date
                                 in Year Month Day format, with no spaces.
                                 Otherwise, None.
                TRANSACTION_AMT: Int, amount of transaction
    """
    data = row.split("|")
    if not data[0] or not data[14] or not not data[15]:
        return None
    return {
        "CMTE_ID": data[0],
        "ZIP_CODE": valid_zip(data[10]),
        "TRANSACTION_DT": data[13],
        "date_key": valid_date(data[13]),
        "TRANSACTION_AMT": int(data[14]),
    }

