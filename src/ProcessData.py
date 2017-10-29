"""
Contains functionality for post-processing FEC data that has been parsed by
the ParseData module.
"""

from src.MedianHeap import MedianHeap
from datetime import datetime

def process_for_zip(data, data_by_zip):
    """
    Takes data from the ParseData module and processes it for conveniently
    determining statistics when data is grouped by recipient and zip code.
    Returns pipe delimited data for output to file.

    :param data:        Dict from ParseData:
                        None if CMTE_ID or TRANSACTION_AMT are empty. None if
                        OTHER_ID is not empty. Otherwise, dict with the
                        following keys:
                        CMTE_ID:         Raw data, ID of the recipient
                        ZIP_CODE:        5-digit zip code of the sender, None
                                         if zip code was invalid in raw data
                        TRANSACTION_DT:  Raw transaction date
                        date_key:        If TRANSACTION_DT is a valid date,
                                         the date in Year Month Day format,
                                         with no spaces. Otherwise, None.
                        TRANSACTION_AMT: Int, amount of transaction
    :param data_by_zip: Dict where keys have the following format:
                        CMTE_ID|ZIP_CODE,
                        and values are MedianHeaps storing the contribution
                        amounts for that recipient and zip code.
    :returns:           Pipe delimited string, ready to write to file, with
                        the following data:
                        CMTE_ID|ZIP_CODE|Median|# Contributions|Sum
    """
    if not data or not data["ZIP_CODE"]:
        return None
    key = data["CMTE_ID"] + "|" + data["ZIP_CODE"]
    if key not in data_by_zip:
        data_by_zip[key] = MedianHeap()
    cur_data = data_by_zip[key]
    cur_data.add(data["TRANSACTION_AMT"])
    output_data = (key + "|" + str(cur_data.median()) + "|" + 
                   str(cur_data.length()) + "|" + str(cur_data.sum))
    return output_data

def process_for_date(data, data_by_date):
    """
    Takes data from the ParseData module and processes it for conveniently
    determining statistics when data is grouped by recipient and date.

    :param data:         Dict from ParseData:
                         None if CMTE_ID or TRANSACTION_AMT are empty. None if
                         OTHER_ID is not empty. Otherwise, dict with the
                         following keys:
                         CMTE_ID:         Raw data, ID of the recipient
                         ZIP_CODE:        5-digit zip code of the sender, None
                                          if zip code was invalid in raw data
                         TRANSACTION_DT:  Raw transaction date
                         date_key:        If TRANSACTION_DT is a valid date,
                                          the date in Year Month Day format,
                                          with no spaces. Otherwise, None.
                         TRANSACTION_AMT: Int, amount of transaction
    :param data_by_date: SortedDict where keys have the following format:
                         CMTE_ID|date,
                         where date is in Year Month Day format, and the
                         dict's values are MedianHeaps storing the contribution
                         amounts for that recipient and date. Keys are in
                         sorted order of alphabetically by recipient, then
                         chronologically by date.
    """
    if not data or not data["date_key"]:
        return None
    key = data["CMTE_ID"] + "|" + data["date_key"]
    if key not in data_by_date:
        data_by_date[key] = MedianHeap()
    cur_data = data_by_date[key]
    cur_data.add(data["TRANSACTION_AMT"])

def output_for_date(data_by_date):
    """
    Takes data after all of the data has been collected, and generates an
    output for one recipient and date. The output is generated for the entry
    that is lowest alphabetically by recipient, then earliest chronologically
    by date. This value is also removed from data_by_date.
    :param data_by_date: SortedDict where keys have the following format:
                         CMTE_ID|date,
                         where date is in Year Month Day format, and the
                         dict's values are MedianHeaps storing the contribution
                         amounts for that recipient and date. Keys are in
                         sorted order of alphabetically by recipient, then
                         chronologically by date.
    :returns:            Pipe delimited string, ready to write to file, with
                         the following data:
                         CMTE_ID|Date|Median|# Contributions|Sum
                         where Date is in Month Day Year format.
    """
    if len(data_by_date) == 0:
        return
    key, cur_data = data_by_date.popitem(last=False)
    key = key.split("|")
    CMTE_ID = key[0]
    date_key = key[1]
    date_key = datetime.strptime(date_key, '%Y%m%d')
    output_date = date_key.strftime('%m%d%Y')
    output_data = (CMTE_ID + "|" + output_date + "|" + str(cur_data.median()) +
                   "|" + str(cur_data.length()) + "|" + str(cur_data.sum))
    return output_data