# Creating a file and writing content
def create_and_write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Reading content from a file
def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return content

# Example usage
filename = 'example.txt'
content_to_write = "Hello, this is an example content."

# Create and write content to the file
create_and_write_file(filename, content_to_write)

# Read content from the file
read_content = read_file(filename)
print("Content read from the file:")
print(read_content)