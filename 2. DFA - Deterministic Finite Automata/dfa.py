def show(transitionStates, alphabets):
    print("\nState Transition table is\n")
    print('{:>10}'.format("|"), end="")
    for j in alphabets:
        print('{:>10}'.format(j+"    "+"|"), end="")
    print()
    for i in transitionStates:
        if(str(i) == "q0"):
            print('{:>10}'.format("-> q0    |"), end="" )
            for j in transitionStates[i]:
                print('{:>10}'.format(j+"    "+"|"), end="")
            print()
        else:
            print('{:>10}'.format(str(i)+"    |"), end="" )
            for j in transitionStates[i]:
                print('{:>10}'.format(j+"    "+"|"), end="")
            print()

def makeTransition(strcmp, values, key, j, transitionStates):
    if(strcmp[:3] == 'eps'):
        strcmp = strcmp[3:]
    index = 0
    while strcmp:
        if(strcmp in values):
            index = values.index(strcmp)
            return index
        strcmp = strcmp[1:]
    return index

def midSuf(transitionStates, string, alphabets, category):
    stateinfo = {}
    count = 0
    stateinfo.update({'q' + str(count):['eps']})
    count = count + 1
    while count <= len(string):
        for i in range(count):
            stateinfo.update({'q' + str(count):[string[:i+1]]})
        count = count + 1
    values = []
    for key, val in stateinfo.items():
        values.append(val[0])
    for key, val in stateinfo.items():
        for j in alphabets:
            strcmp = val[0] + j
            index = makeTransition(strcmp, values, key, j, transitionStates)
            transitionStates[key].append('q' + str(index))
        del transitionStates[key][0]
    if(category == '2'):
        k = len(transitionStates) - 1
        for j in range(len(alphabets)):
            transitionStates['q' + str(k)][j] = 'q' + str(k)

def prefix(transitionStates, string, alphabets):
    k = 0
    for i in range(len(string)):
        for j in alphabets:
            if(string[i] == j):
                transitionStates['q' + str(k)].append('q' + str(k+1))
            else:
                transitionStates['q' + str(k)].append('q-1')
        k = k + 1
        del transitionStates['q' + str(i)][0]
    k = len(transitionStates) - 1
    for j in alphabets:
        transitionStates['q' + str(k)].append('q' + str(k))
    del transitionStates['q' + str(k)][0]

def processString(transitionStates):
    processingString = input("\nEnter string to be processed: ")
    for i in transitionStates:
        currstate = i
        break
    print()
    print(" -> " + currstate, end="")
    for i in processingString:
        j = alphabets.index(i)
        if(currstate == 'q-1'):
            print("\nDead State...String Rejected")
            return
        currstate = transitionStates[currstate][j]
        print(" -> " + currstate, end="")
    print()
    finalState = 'q' + str(len(transitionStates)-1)
    if(currstate == finalState):
        print("\nString accepted")
    else:
        print("\nString rejected")

alphabets = input("\nEnter all alphabets(with space): ").split()
numberOfAlphabets = int(len(alphabets))
cat = ["suffix", "prefix", "substring"]
category = input("Enter category: suffix (0) | prefix (1) | substring (2): ")
string = input("Enter " + cat[int(category)] + ": ")
transitionStates = {}
for i in range(len(string) + 1):
    transitionStates.update({('q' + str(i)):[' ']})
if(category == '1'):
    prefix(transitionStates, string, alphabets)
else:
    midSuf(transitionStates, string, alphabets, category)
show(transitionStates, alphabets)
processString(transitionStates)
