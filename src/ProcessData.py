"""
Contains functionality for post-processing FEC data that has been parsed by
the ParseData module.
"""

from src.MedianHeap import MedianHeap

def process_for_zip(data, data_by_zip):
    """
    Takes data from the ParseData module and processes it for conveniently
    determining statistics when data is grouped by contributor and zip code.

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