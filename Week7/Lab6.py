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
'''
def verify_file_record(line_content):
    clean_line = line_content.strip()
    if clean_line.startswith("#"):
        return 0
    elif clean_line.startswith("id:") and clean_line.endswith(".dat"):
        return 1
    else:
        return -1
print(verify_file_record("   # This is a comment   "))
print(verify_file_record("id:file.dat"))
print(verify_file_record("Hello world"))
'''
'''
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week7\\textfile.txt","r")
total = 0
counter = 0
for i in file:
    number = float(i.strip())
    total = total + number
    counter +=  1
file.close()
print(total)
print(counter)
average = total/counter
print("sum =", total, "average =", average)
'''
'''
even = 0
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week7\\textfile.txt","r")
for i in file:
    num = int(i.strip())
    if num %2 == 0:
        even += num
print("Sum of even #: ", even)
'''
'''
numbers = input("Enter numbers separated by spaces: ").split()
file = open("odd_numbers.txt","w")
for i in numbers:
    if int(i)%2 !=0:
        file.write(i + "\n")
'''
'''
def filter_log_records():
    with open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week7\\textfile.txt","r") as infile, open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week7\\textfile2.txt", "w") as outfile:
        for i in infile:
            cleaned_line = i.strip()
            if cleaned_line:
                outfile.write(cleaned_line.upper()+"\n")
filter_log_records()
'''