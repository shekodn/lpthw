from sys import argv

script, filename = argv

txt = open(filename)

promt = ">"

print(f"Here is your file {filename}")
print(txt.read())

print("Type the filename again:")
file_again = input(promt)

txt_again = open(file_again)

print(txt_again.read())
