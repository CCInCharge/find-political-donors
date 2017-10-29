from src.MedianHeap import MedianHeap
import src.ParseData as ParseData
import src.ProcessData as ProcessData
import sys

def main():
    if len(sys.argv) == 1:
        print("No input file selected, using default: input/itcont_test.txt")
        input_file = "input/itcont_test.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    
    data_by_zip = dict()

    output_zip_file = "output/medianvals_by_zip.txt"
    try:
        with open(output_zip_file, "w") as op_zip:
            try:
                with open(input_file, "r") as fp:
                    for line in fp:
                        data = ParseData.parse_row(line)
                        output_data = ProcessData.process_for_zip(data,
                                                                data_by_zip)
                        if not output_data:
                            continue
                        op_zip.write(output_data + "\n")
            except FileNotFoundError:
                sys.stderr.write("Could not open input file '" + 
                                input_file + "'\n")
                sys.exit(1)
    except:
        sys.stderr.write("Could not open output file for editing\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
