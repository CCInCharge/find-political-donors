from src.MedianHeap import MedianHeap
import src.ParseData as ParseData
import src.ProcessData as ProcessData
from sortedcontainers import SortedDict
import sys

def main():
    if len(sys.argv) == 1:
        input_file = "input/itcont.txt"
        output_zip_file = "output/medianvals_by_zip.txt"
        output_date_file = "output/medianvals_by_date.txt"
    elif len(sys.argv) == 4:
        input_file = sys.argv[1]
        output_zip_file = sys.argv[2]
        output_date_file = sys.argv[3]
    else:
        print("Provide either no arguments to use defaults, or provide three:")
        print("<Input File> <Output (sorted by Zip)> Output <sorted by date)>")
    
    data_by_zip = dict()
    data_by_date = SortedDict()
    
    try:
        with open(output_zip_file, "w") as op_zip:
            try:
                with open(input_file, "r") as fp:
                    for line in fp:
                        data = ParseData.parse_row(line)
                        output_data_zip = ProcessData.process_for_zip(data,
                                                                data_by_zip)
                        ProcessData.process_for_date(data, data_by_date)

                        if output_data_zip:
                            op_zip.write(output_data_zip + "\n")
            except FileNotFoundError:
                sys.stderr.write("Could not open input file '" + 
                                input_file + "'\n")
                sys.exit(1)
    except:
        sys.stderr.write("Could not open output file for writing\n")
        sys.exit(1)
    
    try:
        with open(output_date_file, "w") as op_date:
            while len(data_by_date) > 0:
                op_date.write(ProcessData.output_for_date(data_by_date) + "\n")
    except:
        sys.stderr.write("Could not open output file for writing\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
