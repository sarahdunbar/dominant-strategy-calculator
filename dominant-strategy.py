def optionCalc(num, nL, numL, totNum):
    print(" ")
    name = input("Name of entity " + str(num + 1) + ": ")
    opNum = int(input("How many options are available for this entity? "))
    totNum = totNum*opNum
    print (" ")
    nameList = ["0"]*opNum
    for i in range (0, len(nameList)):
        nameList[i] = input("Option " + str(i + 1) + ": ")
    numL[num + 1] = nameList
    nL[num + 1] = name
    return nL, numL, totNum
    
def probubility(probLeft, probPercent, every):
    if every != 1:
        java = True
        print ("Integer probability of this occuring from 0 - 100, given your choice. ")
        print ("Probability remaining: " + str(probLeft))
        while java == True:
            prob = int(input(": "))
            if prob < 0:
                print ("Probability cannot be negative!")
            elif prob > probLeft:
                print ("Probability too high!")
            else:
                java = False
        probLeft = probLeft - prob
        probPercent = float(prob)/100
        return probLeft, probPercent, every
    if every == 1:
        print ("Probability automatically calculated as " + str(probLeft))
        probLeft = 100
        every = 0
        return probLeft, probPercent, every
    
totNum = 0
name = input("Please enter your name: ")
options = int(input("How many options do you have? "))
totNum = totNum + options
print (" ")
nameList = ["0"]*options
for i in range (0, options):
    nameList[i] = input("Option " + str(i + 1) + ": ")
print (" ")
number = int(input("How many entities are you facing? "))
masterNameList = [0]*(number + 1)
masterOptionList = [0]*(number + 1)
masterNameList[0] = name
masterOptionList[0] = nameList
for i in range (0, number):
    masterNameList, masterOptionList, totNum = optionCalc(i, masterNameList, masterOptionList, totNum)
print (" ")
number = number + 1
probability = 100
optionals = [0]*number
resultSums = [0]*number
totalSum = 0
probLeft = 100
every = 0
probPercent = 0
for n in range (0, totNum):
    for i in range (0, number):
        oneput = masterOptionList[i][optionals[i]]
        print (masterNameList[i] + ": " + oneput)
    jarvais = False
    testOne = False
    for num in range (0, len(masterNameList)):
        num = len(masterNameList) - num - 1
        if optionals[num] + 1 < len(masterOptionList[num]) and jarvais == False: 
            jarvais = True
            if num == 0:
                every = 1
            optionals[num] = optionals[num] + 1
            for extra in range (num + 1, len(masterNameList)):
                optionals[extra] = 0
    jarvais = False
    feedback = int(input("Rating, from negative ten to ten: "))
    probLeft, probPercent, every = probubility(probLeft, probPercent, every)
    feedback = feedback*probPercent
    elven = optionals[0]
    resultSums[elven] = resultSums[elven] + feedback
    totalSum = totalSum + feedback
valuez = -10
valueznum = 0
tie = False
for i in range(0, len(resultSums)):
    if resultSums[i] > valuez:
        valueznum = i
        valuez = resultSums[i]
for i in range(0, len(resultSums)):
    if resultSums[i] == valuez and valueznum != i:
        if tie == False:
            tie = True
            print ("These options are equally viable: ")
        print(nameList[i])
if tie == True:
    print (nameList[valueznum])
    print (" ")
if tie == False:
    print ("Your best choice is: " + nameList[valueznum])
    noolist = [0]*len(resultSums)
    sumta = 0
    for i in range (0, len(resultSums)):
        noolist[i] = resultSums[i] + 10
        sumta = sumta + noolist[i]
    numba = noolist[valueznum]
    certainty = (numba/sumta)*100
    print ("Certainty: " + str(certainty) + "%")
