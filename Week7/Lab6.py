'''
def validate_access_code(raw_code):
    x= raw_code.strip().lower()
    if x.startswith("admin") and x.endswith("2026"):
        return True
    else:
        return False



x = input("Enter a word:")
if validate_access_code(x) == True:
    print("Access granted")
else:
    print("Access deny")
    '''
'''
def audit_text_stream (flagged_word):
    counter = 0
    x=input("Enter a sentance: ")
    x = x.lower()
    while x != 'exit':
      counter = counter + x.count(flagged_word.lower())
      x=input("Enter a sentance: ")
      x = x.lower()
    return counter
print(audit_text_stream("Ust"))
'''
'''
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week6\\Week7\\textfile.txt","r")
content = file.read()
print(content)
'''
'''
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week6\\Week7\\textfile.txt","r")

count=0

for i in file:
     count= count+int(i)
print(count)
file.close()
'''
'''
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week6\\Week7\\textfile.txt","w")
file.write("Hello, python\n")
file.write("Welcome , 2026!\n")
file.write("UST\n")
file.close()
'''
'''
name=input("Enter your name: ")
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week6\\Week7\\textfile.txt","a")
file.write(name)
file.close()
'''
'''
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week7\\textfile.txt","r")
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week7\\textfile.txt","r")
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week7\\textfile.txt","r")
count=0
total = 0
for i in file:
    total = total + int(i)
    count = count + 1
a = total / count
print(a)
file.close()
'''
with open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week7\\textfile.txt" , 'r') as infile:
    with open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week7\\textfile2.txt",'w') as outfile:
        for i in infile:
            outfile.write(i.upper()) 