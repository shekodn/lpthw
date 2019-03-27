from sys import argv
script, filename = argv

filename: print(f"Erasing {filename}")
print("Opening the file...")

target = open(filename, 'w')
target.truncate()

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

target.close()
