# import zipfile
# with zipfile.ZipFile("C:/Users/Python/Desktop/fazeem/text.zip","w") as f:
#     f.write('file1.txt')
#     f.write('file2.txt')
# with zipfile.ZipFile("C:/Users/Python/Desktop/fazeem/text.zip","r")as f:
#     f.extractall('extracted')


# import csv
# with open('pamba.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "place", "age"])
#     writer.writerow(["jiji", "oolampara", "30"])
#     writer.writerow(["prajith", "pambayimula", "24"])

# import csv
# with open('pamba2.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "place", "age"])
#     writer.writerow(["jio", "jith", "22"])
#     writer.writerow(["apa", "panam", "27"])

# import zipfile
# with zipfile.ZipFile('text.zip','w') as f:
#     f.write("pamba.csv")
#     f.write("pamba2.csv")

# with zipfile.ZipFile("text.zip","r") as f:
#     f.extractall("extracted")
#     list1=f.namelist()
#     print(list1)

