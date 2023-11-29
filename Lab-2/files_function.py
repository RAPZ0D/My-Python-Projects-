# file_operations.py

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File '{filename}' not found."

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return "File written successfully."
    except Exception as e:
        return f"Error writing to file: {str(e)}"
