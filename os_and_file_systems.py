import os

print(os.getcwd())  # Returns present working directory
print("\n")
print(
    os.listdir()
)  # Returns list of files and directories present in the current directory
print("\n")

print(
    os.path.abspath("C:\\Users\\Dell\\Desktop\\Python")
)  # Returns the absolute path of the given path
print("\n")

print(
    os.path.dirname("C:\\Users\\Dell\\Desktop\\Python")
)  # Returns the directory name of the given path

# help(os.listdir)

print("\n")

print(os.listdir("."))  # Relative Path, '.' refers to current directory
# any file starting with '.' are hidden files
print("\n")

# print(os.listdir('/usr'))
# print(os.listdir('/usr/lib'))
print(os.listdir("Practise"))

# help(os.makedirs)

os.makedirs("./data", exist_ok=True)

# Verifies if the 'data' directory exists in the directory
print("data" in os.listdir("."))

print(os.listdir("./data"))

import urllib.request

url1 = "https://gist.githubusercontent.com/aakashns/8de7b03f241b787042be1a1e4afd91da/raw/a15ba86d0260ca2d2615afa9d809bf4be019ab3d/loans1.txt"

url2 = "https://gist.githubusercontent.com/aakashns/8de7b03f241b787042be1a1e4afd91da/raw/a15ba86d0260ca2d2615afa9d809bf4be019ab3d/loans2.txt"

url3 = "https://gist.githubusercontent.com/aakashns/8de7b03f241b787042be1a1e4afd91da/raw/a15ba86d0260ca2d2615afa9d809bf4be019ab3d/loans3.txt"

# Storing the content in the url into a file in the 'data' directory
urllib.request.urlretrieve(url1, "./data/loans1.txt")
urllib.request.urlretrieve(url2, "./data/loans2.txt")
urllib.request.urlretrieve(url3, "./data/loans3.txt")

print(os.listdir("./data"))

file1 = open("./data/loans1.txt", mode="r")
# To view the contents of the file, we use the 'read' method of the file object
print(file1.read())
# After operations on files its important to close the files to free up memory/.
file1.close()

# ^ To deal with this problem of constantly opening and closing files, we can use a "with" statement
# ^ which automatically envokes the .close() method on the file after the block of code within it is executed.

with open("./data/loans2.txt", mode="r") as file2:
    file2_contents = file2.read()
    print(file2_contents)
# This line of code wont work as the file has been closed.
# file2.read()

with open("./data/loans3.txt", "r") as file3:
    # In the readLines() function, each line is a separate string.
    files3_lines = file3.readlines()
    print(files3_lines)

    print(files3_lines[0])
    # To remove the '\n' character after every line, we can use the strip() function
    # The strip function removes any extra spaces in the beggining and the end of the string
    # and newline characters \n
    print(files3_lines[0].strip())

print("\n" * 2)
# Custom processing of data from files
print(file2_contents)

print("828400,120,0.11,100000".split(","))
# The split method breaks a string into a list using the given separator.
loan1 = {"amount": 82400, "duration": 120, "rate": 0.11, "down_payment": 100000}


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


headers = parse_headers(files3_lines[0])
print(headers)
print(files3_lines[1])
print(parse_values(files3_lines[1]))


def create_item_dict(values, headers):
    result = {}
    for value, headers in zip(values, headers):
        result[headers] = value
    return result


header1 = parse_headers(files3_lines[0])
values1 = parse_values(files3_lines[1])
result1 = create_item_dict(values1, header1)
print(result1)


# A final function with all the functions put together
def read_csv(path):
    result = []
    with open(path, "r") as file:
        lines = file.readlines()
        headers = parse_headers(lines[0])
        values = []
        for line in lines[1:]:
            values2 = parse_values(line)
            item_dict = create_item_dict(values2, headers)
            result.append(item_dict)
    return result


print(read_csv("./data/loans2.txt"))
