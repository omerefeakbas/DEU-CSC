"""
Created on Wed Dec 18 22:30:00 2019

@author: Omer Efe Akbas 2017280004
"""
file = open("trainSet.csv","r")
file_test = open("testSet.csv","r")
data = []
testData = []


#CART


#Reading the data
for i in file.readlines():
    line = i
    line.replace("\n","")
    data.append(line.split(","))
   
#FOR DEBUG 
# =============================================================================
itero = 0
itera = 0
# =============================================================================

treeArray = []
titles = []
titles.append(data[0])


#FORMATING THE DATA
for i in range(750):
    if int(data[i+1][1]) > 250 and int(data[i+1][1])<=6498:
        data[i+1][1] = '250-6498'
    elif int(data[i+1][1]) > 6498 and int(data[i+1][1]) <= 9337:
        data[i+1][1] = '6498-9337'
    elif int(data[i+1][1]) > 9337 and int(data[i+1][1]) <= 12176:
        data[i+1][1] = '9337-12176'
    else:
        data[i+1][1] = '12176-18424'
        
        #min: 250
        #max: 18424
        #stdev: 2839.0152803695482
        #avg: 9337.0
        #***
        #250-6498    6498-9337   9337-12176   12176-18424
        #***


    if int(data[i+1][4]) > 19 and int(data[i+1][4])<= 25:
        data[i+1][4] = '19-25'
    elif int(data[i+1][4]) > 25 and int(data[i+1][4]) <= 36:
        data[i+1][4] = '25-36'
    elif int(data[i+1][4]) > 36 and int(data[i+1][4]) <= 47:
        data[i+1][4] = '36-47'
    elif int(data[i+1][4]) > 47 and int(data[i+1][4]) <= 58:
        data[i+1][4] = '47-58'
    elif int(data[i+1][4]) > 58 and int(data[i+1][4]) <= 69:
        data[i+1][4] = '58-69'    
    else:
        data[i+1][4] = '69-75'
        
        #min: 19
        #max: 75
        #stdev: 11.280375024934223
        #avg: 47.0
        #***
        #19-25  25-36  36-47     47-58  58-69  69-75
        #***

#Run the commands until the data is empty        
while len(data)>1:  
    itero = itero + 1
    goodC = 0
    badC = 0
    
    #Counting all goods and bads
    for bip in range(len(data)): 
        if data[bip][5] == "good\n":
            goodC = goodC + 1      
    badC = len(data)-1 - goodC
    
    
    candicateArray = []
    MOGArray = [["Split","PL","PR","P(G|tL)","P(B|tL)","P(G|tR)","P(B|tR)","2PLPR","Q(s|t)","MOG"]]
    
    
    #Examining different types and counts of these types
    array = []
    countArray = []
    bo = 0
    for u in range(5):
        
        itera = itera + 1
        for i in data:
            array.append(i[u])
        array.pop(0)
        
        #Filling the count array for each different type
        for i in array:
            if [i,0,0,0] not in countArray:
                countArray.append([i,0,0,0])
        
        #Increasing element count
        for i in range(len(array)):
            for j in range(len(countArray)):
                if array[i] in countArray[j][0]:
                    countArray[j][1] = countArray[j][1] + 1
                    if(data[i+1][5] == "good\n"):
                        countArray[j][2] = countArray[j][2] + 1
                    if(data[i+1][5] == "bad\n"):
                        countArray[j][3] = countArray[j][3] + 1
                    
                    
        for c in countArray:
            candicateArray.append([data[0][u],str(c[0]),[c[1],c[2],c[3]]])
        
#-------------------------------------------------------------------------  
#Calculatin necessary values and adding them to MEASURE OF GOODNESS Array    
#   MOGArray =  [["Split","PL","PR","P(G|tL)","P(B|tL)","P(G|tR)","P(B|tR)","2PLPR","Q(s|t)","MOG"]]
#-------------------------------------------------------------------------
            
            
        for m in countArray: 
            MOGArray.append( [bo, #"Split"
                             m[1]/750, #"PL"
                             (750-m[1])/750,#"PR"
                             m[2]/m[1], #"P(G|tL)"
                             m[3]/m[1],#"P(B|tL)"
                             (goodC-m[2])/(750-m[1]),#"P(G|tR)"
                             (badC-m[3])/(750-m[1]), #"P(B|tR)"
                             2*(m[1]/750)*((750-m[1])/750),# "2PLPR"
                             abs((m[2]/m[1])-((goodC-m[2])/(750-m[1]))) + abs((m[3]/m[1])-((badC-m[3])/(750-m[1]))),# "Q(s|t)"
                             (2*(m[1]/750)*((750-m[1])/750))*(abs((m[2]/m[1])-((goodC-m[2])/(750-m[1]))) + abs((m[3]/m[1])-((badC-m[3])/(750-m[1]))))])# "MOG"
            bo = bo + 1
        bo = 0  
        array.clear()
        countArray.clear()
        
 
    #Finding the element  that has maximum Measure Of Goodness, and its index.
    maxMOG=0
    maxMOGIndex = 0
    for i in MOGArray:
        if i[9] == "MOG":
            continue
        if float(i[9]) > maxMOG:
            maxMOGIndex = MOGArray.index(i)
            maxMOG = float(i[9])
            
    #DEBUG PRINTS
    print("\n")
    print("ITERATION: " + str(itera) + " " + str(itero) + "\n")
    print("Mog Index: " + str(maxMOGIndex))
    print("MOG: " + str(maxMOG))
    print("Data Len: " + str(len(data)-1))
    print("Good Count: " + str(goodC))
    print("Bad Count: " + str(badC))
    if len(candicateArray) > 0:
        print(candicateArray[maxMOGIndex][0] + " = " + candicateArray[maxMOGIndex][1])
         
        
    #finding the index of the value
    if len(candicateArray) > 0:
        indexFound = data[0].index(candicateArray[maxMOGIndex][0])
        dataLen = len(data)-1
        foundCount = 0
        
        #If current element matches with value , remove it from the data
        for i in range(len(data)):
            if candicateArray[maxMOGIndex][1] == data[dataLen-i][indexFound]:
                del data[dataLen-i]
                foundCount = foundCount +1
                
    print("Data Len After : " + str(len(data)-1))
    
    print("foundCount: " +str(foundCount))
    
    
    
    #Counting all goods and bads
    goodC = 0
    badC = 0
    for bip in range(len(data)): 
        if data[bip][5] == "good\n":
            goodC = goodC + 1      
    badC = len(data)-1 - goodC
    
    
    #DEBUG PRINT
    print("")
    print("CANDICATES:")   
    for i in range(len(candicateArray)):
        print(candicateArray[i],MOGArray[i+1][9])
        
        
    if candicateArray[maxMOGIndex][2][1] > candicateArray[maxMOGIndex][2][2] :
        treeArray.append([candicateArray[maxMOGIndex][0],candicateArray[maxMOGIndex][1],'good'])
    else:
        treeArray.append([candicateArray[maxMOGIndex][0],candicateArray[maxMOGIndex][1],'bad'])
    
    foundCount = 0
    
    
    print("MOGLEN: " +str(len( MOGArray )-1))
    print("Candicate array len: " + str(len(candicateArray)))  
        
    MOGArray.clear()
    candicateArray.clear()
#DEBUG PRINT
print("\nTREE ARRAY:")    
for i in treeArray:
    print(i)
    
print("\n")    


#READING AND FORMATING THE TEST DATA
#------------------------------------------------------------------------------
for i in file_test.readlines():
    line = i
    line.replace("\n","")
    testData.append(line.split(","))   
    
    
for i in range(250):
    if int(testData[i+1][1]) > 250 and int(testData[i+1][1])<=6498:
        testData[i+1][1] = '250-6498'
    elif int(testData[i+1][1]) > 6498 and int(testData[i+1][1]) <= 9337:
        testData[i+1][1] = '6498-9337'
    elif int(testData[i+1][1]) > 9337 and int(testData[i+1][1]) <= 12176:
        testData[i+1][1] = '9337-12176'
    else:
        testData[i+1][1] = '12176-18424'
        #min: 250
        #max: 18424
        #stdev: 2839.0152803695482
        #avg: 9337.0
        #***
        #250-6498    6498-9337   9337-12176   12176-18424
        #***
        

    if int(testData[i+1][4]) > 19 and int(testData[i+1][4])<= 25:
        testData[i+1][4] = '19-25'
    elif int(testData[i+1][4]) > 25 and int(testData[i+1][4])<= 36:
        testData[i+1][4] = '25-36'
    elif int(testData[i+1][4]) > 36 and int(testData[i+1][4]) <= 47:
        testData[i+1][4] = '36-47'
    elif int(testData[i+1][4]) > 47 and int(testData[i+1][4]) <= 58:
        testData[i+1][4] = '47-58'
    elif int(testData[i+1][4]) > 58 and int(testData[i+1][4]) <= 69:
        testData[i+1][4] = '58-69'
    else:
        testData[i+1][4] = '69-75'
 
        #min: 19
        #max: 75
        #stdev: 11.280375024934223
        #avg: 47.0
        #***
        #19-25  25-36  36-47     47-58  58-69  69-75
        #***
#------------------------------------------------------------------------------        
TP = 0
FP = 0
TN = 0
FN = 0
#testing the data (Getting TP FP TN FN Counts)
for i in range(250):
    for j in treeArray:
        titleIndex = titles[0].index(j[0])
        
        if testData[i+1][titleIndex] == j[1]:

            if testData[i+1][5] == j[2] + "\n":
                if(j[2] == "good"):

                    TP = TP + 1
                    break
                if(j[2] == "bad"):
                    TN = TN + 1
                    break
                    
            else:
                if(j[2] == "good"):
                    FP = FP + 1
#                print(testData[i+1][5])
#                print(j[2])
#                print("UNmach")
                    break
                if(j[2] == "bad"):
                    FN = FN + 1
                    break
        else:
            continue
            
print("Accuracy: " + str((TP+TN)/(TP + TN + FP + FN))) 
print("True Positive Rate: " + str(TP/(TP+FP)))
print("True Negative Rate: " + str(TN/(TN+FN)))
print("True Positive Count: " + str(TP))
print("True Negative Count: " + str(TN))