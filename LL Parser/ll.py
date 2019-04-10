def goto(linenum):
    global gotoline
    gotoline = linenum



i,j,k,m,n,o,o1,var,l,f,c,f1=0,0,0,0,0,0,0,0,0,0,0,0

str1 = ["E"]
temp = []
temp1 = []
temp2 = []
tt = []
t3 = []
t = []
array = [
           [ ["NT"], ["<id>"], ["+"], ["*"], [";"] ],
           [ ["E"], ["Te"], ["Error"], ["Error"], ["Error"] ],
           [ ["e"], ["Error"], ["+Te"], ["Error"], ["\0"] ],
           [ ["T"], ["Vt"], ["Error"], ["Error"], ["Error"] ],
           [ ["t"], ["Error"], ["\0"], ["*Vt"], ["\0"] ],
           [ ["V"], ["<id>"], ["Error"], ["Error"], ["Error"] ]
        ]

print("LL(1) Parser Table")
for i in range(6):
    for j in range(5):
        print('{:>10}'.format(array[i][j]))
    print()
string = str(input("\nEnter the String: "))
if string[len(string)-1] != ';':
    print("End of string marker should be ';'")
    exit()
print("Checking validation of string")
print(str1)
i=0
gotoline == 'again'
while(i<len(string)):
    if gotoline == 'again':
        if(string[i]==' ' and i<len(string)):
            print("Spaces are not allowed in source string ")
            quit()
        temp[k]=string[i]
        f1=0
        goto('again1')
        continue
    elif gotoline == 'again1':
        if(i>=len(string)):
            quit()
        for l in range(1, 5):
            tempstring = "".join(temp)
            if(array[0][l] == tempstring):
                f1=1
                m,o,var,o1=0,0,0,0
                while(m<len(str1) and m<len(string)):
                    if str1[m]==string[m]:
                        var=m+1
                        temp2[o1]=str1[m]
                        m=m+1
                        o1=o1+1
                    else:
                        if (m+1)<len(str1):
                            m=m+1
                            temp1[o]=str1[m]
                            o=o+1
                        else:
                            m=m+1
                t[0]=str1[var]
                for n in range(1, 6):
                    if array[n][0] == t:
                        break
                str1 = list(str1)
                temp2 = list(temp2)
                str1=temp2
                str1.append(array[n][l])
                str1.append(temp1)
                str1 = "".join(str1)
                temp2 = "".join(temp2)
                print(str1)

                if array[n][l] == NULL:
                    if(i==(len(str)-1)):
                        str1 = list(str1)
                        str1[len(str)-1] = '\0'
                        str1 = "".join(str1)
                        print(str1)
                        print("Entered string is Valid")
                        exit()
                if array[n][l] == "Error":
                    print("Error in your source string")
                    exit()
                tt=NULL
                tt=lint(tt)
                tt=array[n][l]
                tt="".join(tt)
                t3=NULL
                f=0
                for c in range(len(tt)):
                    t3[c]=tt[c]
                    if t3==temp:
                        f=0
                        break
                    else:
                        f=1
                if f==0:
                    temp = NULL
                    temp1 = NULL
                    temp2 = NULL
                    t = NULL
                    i=i+1
                    k=0
                    goto("again")
                    continue
                else:
                    temp1=NULL
                    temp2=NULL
                    t=NULL
                    goto("again1")
        i=i+1
        k=k+1
    if(f1==0):
        print("Entered string is invalid")
    else:
        print("Entered string is valid")
