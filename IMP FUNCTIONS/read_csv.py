# This function is generic enough to read CSV files of any rows and columns
# This function reads csv files and converts it into a dictionary of key-value pairs
def parse_headers(header_line):
    return header_line.strip().split(",")


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(","):
        # To handle edge cases
        if item == "":
            values.append(0.0)
        else:
            values.append(float(item))
    return values


def create_item_dict(values, headers):
    result = {}
    for value, headers in zip(values, headers):
        result[headers] = value
    return result


def read_csv(path):
    result = []
    with open(path, "r") as file:
        lines = file.readlines()
        headers = parse_headers(lines[0])
        values = []
        for line in lines[1:]:
            values = parse_values(line)
            item_dict = create_item_dict(values, headers)
            result.append(item_dict)
    return result
