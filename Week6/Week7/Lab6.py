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
file = open("textfile.txt","r")
content = file.read()
print(content)
