import csv
import json
import pickle

class FileHandler:
    def __init__(self, input_file_name, output_file_name, changes):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.changes = changes
        self.all_products = []

    def load_file(self):
        pass  

    def apply_changes(self):
        for change in self.changes:
            split_content = change.split(",")
            column_int = int(split_content[0])
            row_int = int(split_content[1])
            change_cell = split_content[2]

            if 0 <= row_int < len(self.all_products) and 0 <= column_int < len(self.all_products[0]):
                self.all_products[row_int][column_int] = change_cell
            else:
                print("Invalid row or column index. Change and save failed.")        

    def save_file(self):
        pass  

class CSVHandler(FileHandler):
    def load_file(self):
        with open(self.input_file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                self.all_products.append(row)


    def save_file(self):
        with open(self.output_file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.all_products)

class JsonHandler(FileHandler):
    def load_file(self):
        with open(self.input_file_name, "r") as f:
            self.all_products = json.load(f)


    def save_file(self):
        with open(self.output_file_name, "w") as f:
            json.dump(self.all_products, f, indent=4)

class PickleHandler(FileHandler):
    def load_file(self):
        with open(self.input_file_name, "rb") as f:
            self.all_products = pickle.load(f)

    def save_file(self):
        with open(self.output_file_name, "wb") as f:
            pickle.dump(self.all_products, f)
