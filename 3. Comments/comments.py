def findComments(data):
    global single
    global multiple
    global comment
    if(comment == 'm'):
        mfind = data.find(multipleCom)
        if(mfind != -1):
            comment = '-1'
            multiple = multiple + 1
    else:
        sfind = data.find(singleCom)
        mfind = data.find(multipleCom)
        stringactive = data.find(stringopen)
        if((sfind<stringactive and stringactive^sfind != 0 and sfind!=-1) or (mfind<stringactive and stringactive^mfind != 0 and mfind!=-1) or stringactive == -1):
            if(sfind!= -1 and mfind == -1):
                single = single + 1
            elif(sfind==-1 and mfind!=-1):
                comment = 'm'
                multiple = multiple + 1
                mfind2 = data.rfind(multipleCom)
                if((mfind<mfind2)):
                    comment = '-1'
                    multiple = multiple + 1
            elif(sfind!=-1 and mfind !=-1):
                if((sfind<mfind) and (sfind!=-1)):
                    comment = 's'
                    single = single + 1
                elif((mfind<sfind) and (mfind!=-1)):
                    comment = 'm'
                    mfind2 = data.rfind(multipleCom)
                    multiple = multiple + 1
                    if((mfind!=mfind2) and (mfind2!=-1)):
                        comment = '-1'
                        multiple = multiple + 1


single = 0
multiple = 0
multipleCom = "'''"
singleCom = "#"
stringopen = '"'
comment = '-1'
noOfLines=0

print("enter choice \n 1. read from file \n 2. give input")
choice = input()
if(choice == '1'):
    filename = input("\nEnter filename: ")
    with open(filename, 'r') as file:
        for data in file.readlines():
            noOfLines=noOfLines+1
            findComments(data)

elif(choice == '2'):
    data = " "
    print("\nEnter quit when done\n")
    while(data!="quit"):
        noOfLines=noOfLines+1
        data = input()
        findComments(data)
print("\nNo. of lines: ", noOfLines)
print("single-line comments: ", single, "\nmulti-line comments: ", int(multiple/2))
