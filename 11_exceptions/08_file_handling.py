# file = open("test.txt", "w")
# try:
#     file.write("Hello World")
# except:
#     print("Error writing to file")
# finally:
#     file.close()

# file = open("test.txt", "r")
# print(file.read())
# file.close()

with open("test1.txt", "w") as file:
    file.write("Ginger Tea")
