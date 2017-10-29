from src.MedianHeap import MedianHeap

def process_for_zip(data, data_by_zip):
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