import os
import sys
from classes import CSVHandler, JsonHandler, PickleHandler

def get_handler_for_file(input_file_name,utput_file_name,change_values):
    if input_file_name.endswith(".csv"):
        return CSVHandler(input_file_name,utput_file_name,change_values)
    elif input_file_name.endswith(".json"):
        return JsonHandler(input_file_name,utput_file_name,change_values)
    elif input_file_name.endswith(".pkl"):
        return PickleHandler(input_file_name,utput_file_name,change_values)


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print(f"Error: Expected more arguments in commnad: {sys.argv}")
        quit()
    file_path=sys.argv[1]
    if not os.path.exists(file_path):
        file_directory = os.path.split(file_path)[0]
        if not file_directory:
            file_directory = os.getcwd()
        other_files_in_directory = [f for f in os.listdir(file_directory) if not os.path.isdir(f) and (".csv" in f or ".txt" in f or ".json" in f or ".pkl" in f)]
        print(f"Error:File does not exist{file_path}")
        print(f"Maybe you wanted select onf of these files in the same directiory {other_files_in_directory}")
        quit()

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    change_values = sys.argv[3:]

    input_file_handler = get_handler_for_file (input_file_name,output_file_name,change_values)
    input_file_handler.load_file()
    input_file_handler.apply_changes()

    print(input_file_handler.all_products)

    output_file_handler = get_handler_for_file (output_file_name,output_file_name,change_values)

    output_file_handler.all_products=input_file_handler.all_products

    output_file_handler.save_file()



