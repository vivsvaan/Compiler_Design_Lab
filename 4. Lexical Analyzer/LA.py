def lexicalParser(line):
    global key_buffer
    global key_print
    global iden_buffer
    global iden_print
    global op_buffer
    global op_print
    global buffer
    global deli_buffer

    for c in line:
        if c in operators:
            op_buffer = op_buffer + str(c)
        elif c in delimeters and c not in deli_buffer:
            deli_buffer = deli_buffer + str(c)
        elif(c.isalnum()):
            buffer = buffer + str(c)

        elif((c==' ' or c=='\n') and buffer):
            if(buffer in keywords):
                key_buffer.append(str(buffer))
            else:
                iden_buffer.append(str(buffer))
            buffer = ""
    for ch in op_buffer:
        if ch not in op_print:
            op_print = op_print + ch

    for i in key_buffer:
        if i not in key_print:
            key_print.append(i)

    for i in iden_buffer:
        if i not in iden_print:
            iden_print.append(i)




import keyword
keywords = keyword.kwlist
delimeters = ["(", ")", "[", "]", "{","}", ",", ":", ".", "`", "=", ";", "+=", "-=", "*=", "/=", "%=", "**=", "&=", "|=", "^=", ">>=", "<<="]
key_buffer = []
key_print = []
iden_buffer = []
iden_print = []
operators = "+-*/%="
j,k,z=0,0,0
op_buffer = ""
op_print = ""
buffer = ""
deli_buffer = ""
noOfLines = 0
print("enter choice \n 1. read from file \n 2. give input")
choice = input()
if choice=="1":
    with open("program.txt") as file:
        for line in file.readlines():
            noOfLines=noOfLines+1
            lexicalParser(line)
elif choice=="2":
    line = " "
    print("\nEnter quit when done\n")
    while(line!="quit"):
        noOfLines=noOfLines+1
        line = str(input())
        lexicalParser(line)
print("\nnumber of lines are: ", noOfLines)
print("\noperators are: ", ", ".join(op_print))
print("\nkeywords are: ",", ".join(key_print))
print("\nidentifiers are: ",", ".join(iden_print))
print("\ndelimeters are: ", ", ".join(deli_buffer))
