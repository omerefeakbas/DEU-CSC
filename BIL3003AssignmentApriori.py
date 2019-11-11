"""
Created on Tue Oct 22 18:10:22 2019
@author: Omer Efe Akbas - 2017280004
"""


#EXAMININING THE DATA
#--------------------
errorLineCount = 0
missCount = 0
totalMissCount = 0
moreThanTwo = 0
lineCount = 0
errorArray = [0,0,0,0,0,0,0,0,0,0,0,0]
#--------------------


flag = False
file = open("sampleDataText.txt","r")
fileToWrite = open("ProcessedData.txt","w")
fileRules = open("GeneratedRules.txt","w")


data = [] #Actual Data
compData = [] #Also Actual Data (But For Comparison)

#Formating The Data
for line in file.readlines():
    missCount = 0
    flag = False
    line = line.replace("\n","")
    line = line.split(",")
    data.append(line)
    compData.append(line)
    lineCount = lineCount + 1
   
#Finding missing values with making comparisons with other datas
for i in range(len(data)):
    for j in range(12):
        if data[i][j] == "?":
            for x in range(i-5,i+5):
                if compData[x][j] != "?" and data[x][1] == compData[x][1] and data[x][2] == compData[x][2] and data[x][3] == compData[x][3] and data[x][4] == compData[x][4] and data[x][6] == compData[x][6] and data[x][7] == compData[x][7] and data[x][8] == compData[x][8] and data[x][11] == compData[x][11]:
                    data[i][j] = compData[x][j]


#Storing the processed data on another file
for i in range(len(data)):
    blankString = ""
    missCount = 0
    flag = False
    for j in range(12):
        if data[i][j] == "?":
            print(data[i])

            flag = True
            totalMissCount = totalMissCount + 1
            missCount = missCount + 1
            errorArray[j] = errorArray[j] + 1
    if flag == True:
        errorLineCount = errorLineCount + 1
    if missCount >= 2:
        moreThanTwo = moreThanTwo + 1
    for j in data[i]:
        blankString += j + ","
    fileToWrite.write(blankString)
    fileToWrite.write("\n")             


column = []
counts = []
countsB = []
countsC = []
countsData = []
typeCount = 0
for j in range(12):
    column.clear()
    counts.clear()
    countsB.clear()
    typeCount = 0 
    for i in range(len(data)-1):
        column.append(data[i+1][j]) 
    for item in column:
        if item not in counts:
            counts.append(item)
            typeCount += 1      
    for item in counts:
        itemCountInColumn = 0
        for i in column:
            if item == i:
                itemCountInColumn += 1
        countsB.append([item,itemCountInColumn])
    countsC.append([data[0][j],typeCount])
        
            
#------------------------------------------------------------------------------   
    
#-------------*--------------
#CATEGORIZATION
#-------------*--------------
for i in range(len(data)-1):   
    
    
#    --------------o--------------
#    Average_Delay_Time_Per_Sec - Index:2 - 3 Categories
#    --------------o--------------   
    if(i<=355):
        data[i+1][2] = ">=0.000406 & <0.000483"
    elif(i<=710):
        data[i+1][2] = ">=0.000483 & <0.000856"
    else:
        data[i+1][2] = ">=0.000856 & <=0.005237"


    
#    --------------o--------------
#    Packet_lost - Index:5 - 4 Categories
#    --------------o--------------     
    if (int(data[i+1][5])>=3913 and int(data[i+1][5])<16548):
        data[i+1][5] = ">=3913 & <16582"
    elif (int(data[i+1][5])>=16548 and int(data[i+1][5])<33164):
        data[i+1][5] = ">=16548 & <33164"
    elif (int(data[i+1][5])>=33164 and int(data[i+1][5])<49749):
        data[i+1][5] = ">=33164 & <49749"
    else:
        data[i+1][5] = ">=49749 & <62415"
               

        
#    --------------o--------------
#    AVG_Drop-Rate - Index:7 - 4 Categories 0.143741
#    --------------o--------------    
    if(float(data[i+1][7])>= 0.058749 and float(data[i+1][7])<0.202490):
        data[i+1][7] = ">= 0.058749 & <0.202490"
    elif(float(data[i+1][7])>= 0.202490 and float(data[i+1][7])<0.346231):
        data[i+1][7] = ">= 0.202490 & <0.346231"
    elif(float(data[i+1][7])>= 0.346231 and float(data[i+1][7])<0.489972):
        data[i+1][7] = ">= 0.346231 & <0.489972"
    else:
        data[i+1][7] = ">= 0.489972 & <=0.633714"


#    --------------o--------------
#    AVG_Bandwith-Use - Index:8 - 4 Categories 0.170879
#    --------------o--------------    
    if(float(data[i+1][8])>= 0.207361 and float(data[i+1][8])<0.37824):
        data[i+1][8] = ">= 0.207361 & <0.37824"
    elif(float(data[i+1][8])>= 0.37824 and float(data[i+1][8])<0.549119):
        data[i+1][8] = ">= 0.37824 & <0.549119"
    elif(float(data[i+1][8])>= 0.549119 and float(data[i+1][8])<0.719998):
        data[i+1][8] = ">= 0.549119 & <0.719998"
    else:
        data[i+1][8] = ">= 0.719998 & <=0.89088"
                
        
#    --------------o--------------
#    FloodStatus - Index:10 - 4 Categories 0.14121
#    --------------o--------------   
    if(float(data[i+1][10])>= 0.001899 and float(data[i+1][10])<0.143109):
        data[i+1][10] = ">= 0.001899 & <0.143109"
    elif(float(data[i+1][10])>= 0.143109 and float(data[i+1][10])<0.284319):
        data[i+1][10] = ">= 0.143109 & <0.284319"
    elif(float(data[i+1][10])>= 0.284319 and float(data[i+1][10])<0.425529):
        data[i+1][10] = ">= 0.284319 & <0.425529"
    else:
        data[i+1][10] = ">= 0.425529 & <0.566739"

#------------------------------------------------------------------------------


#-----------------------------------
#------------ SUPPORT --------------
#-----------------------------------0-1
#Getting the minSupport value
while True:
    try:
        minSupportValue = float(input("Enter a min support value 0-1:"))
        if minSupportValue <= 1 and minSupportValue >= 0:
            break
        else:
            print("Please enter a number between 0 - 1.")
    except ValueError:
        print("Please enter a valid value...")
   
     
#Creating the Frequent Item Set
fis = []
rules = []  
countsC.clear()
print("Minimum Support Count: " + str((minSupportValue * 1075)//10))             
for j in range(12):
    column.clear()
    counts.clear()
    countsB.clear()
    typeCount = 0
    
    for i in range(len(data)-1):
        column.append(data[i+1][j])
        
    for item in column:
        if item not in counts:
            counts.append(item)
            typeCount += 1
        
    for item in counts:
        itemCountInColumn = 0
        for i in column:
            if item == i:
                itemCountInColumn += 1
        countsB.append([item,itemCountInColumn])
    for i in range(len(countsB)):
        
        if countsB[i][1]/1075 > minSupportValue:
            fis.append([data[0][j],countsB[i]])
            print([data[0][j],countsB[i]])
    
    countsC.append([data[0][j],typeCount])

#Geting User Input (Metric Selection)
#Possible Selections 1,2,3,Confidence,Lift,Leverage7
    
while True:
        selectedMetric = input("Enter the metric you want\n1)Confidence  2)Lift   3)Leverage\n")
        if selectedMetric == "Confidence" or selectedMetric == "Lift" or selectedMetric == "Leverage" or selectedMetric == "1" or selectedMetric == "2" or selectedMetric == "3":
            break
        else:
            print("Please enter a valid value...")



#If confidence is selected:

#------------------------------------
#----------- CONFIDENCE -------------
#------------------------------------0-1
if selectedMetric == "Confidence" or selectedMetric == "1":
    while True:
        try:
            minConfidenceValue = float(input("Enter a min confidence value 0-1:"))
            if minConfidenceValue <= 1 and minConfidenceValue >= 0:
                break
            else:
                print("Please enter a number between 0 - 1.")
        except ValueError:
            print("Please enter a valid value...")
    
    index1 = -1
    index2 =-1
    countD = 0
    for item in fis:
        for item2 in fis:
            countD = 0
            if(item[0] != item2[0]):
                for i in range(12):
                    if data[0][i] == item[0]:
                        index1 = i
                    if data[0][i] == item2[0]:
                        index2 = i
                for i in range(len(data)-1):
                    if data[i+1][index1] == item[1][0] and data[i+1][index2] == item2[1][0]:
                        countD +=1
                
                if countD/1075 >= minSupportValue and countD/item[1][1] >= minConfidenceValue:
                    RuleString = "IF " + item[0] + " = " + str(item[1][0]) + " THEN " + item2[0] + " = " + str(item2[1][0]) + " --> Support: " + str(countD/1075) + "  -  Confidence: " + str(countD/item[1][1])
                    if RuleString not in rules:
                        rules.append(RuleString)
                if countD/1075 >= minSupportValue and countD/item2[1][1] >= minConfidenceValue:
                    RuleString = "IF " + item2[0] + " = " + str(item2[1][0]) + " THEN " + item[0] + " = " + str(item[1][0]) + " --> Support: " + str(countD/1075) + "  -  Confidence: " + str(countD/item2[1][1])
                    if RuleString not in rules:
                        rules.append(RuleString)
 
                   
#If lift is selected:    

#-----------------------------------
#-------------- LIFT ---------------  Lift(A->B) = confidence(A->B)/support(B)
#-----------------------------------  0 - INF
if selectedMetric == "Lift" or selectedMetric == "2":
    while True:
        try:
            minLiftValue = float(input("Enter a min lift value 0 - INF:"))
            if minLiftValue >= 0:
                break
            else:
                print("Please enter a number GREATHER THAN 0")
        except ValueError:
            print("Please enter a valid value...")
    
    
    index1 = -1
    index2 =-1
    countD = 0
    for item in fis:
        for item2 in fis:
            countD = 0
            if(item[0] != item2[0]):
                for i in range(12):
                    if data[0][i] == item[0]:
                        index1 = i
                    if data[0][i] == item2[0]:
                        index2 = i
                for i in range(len(data)-1):
                    if data[i+1][index1] == item[1][0] and data[i+1][index2] == item2[1][0]:
                        countD +=1
                
                if countD/1075 >= minSupportValue and (countD/item[1][1])/(item2[1][1]/1075) >= minLiftValue:
                    RuleString = "IF " + item[0] + " = " + str(item[1][0]) + " THEN " + item2[0] + " = " + str(item2[1][0]) + " --> Support: " + str(countD/1075) + "  -  Lift: " + str((countD/item[1][1])/(item2[1][1]/1075))
                    if RuleString not in rules:
                        rules.append(RuleString)
                    
                if countD/1075 >= minSupportValue and (countD/item2[1][1])/(item[1][1]/1075) >= minLiftValue:
                    RuleString = "IF " + item2[0] + " = " + str(item2[1][0]) + " THEN " + item[0] + " = " + str(item[1][0]) + " --> Support: " + str(countD/1075) + "  -  Lift: " + str((countD/item2[1][1])/(item[1][1]/1075))
                    if RuleString not in rules:
                        rules.append(RuleString)


#If leverage is selected:                   

#-------------------------------
#---------  LEVERAGE ----------- Leverage(A->B) = support(A->B) - support(A)*support(B)
#------------------------------- -0.25 - 0.25
if selectedMetric == "Leverage" or selectedMetric == "3":           
    while True:
        try:
            minLeverageValue = float(input("Enter a min leverage value -0.25  -  0.25"))
            if minLeverageValue >= -0.25 and minLeverageValue <= 0.25:
                break
            else:
                print("Please enter a number between -0.25 - 0.25")
        except ValueError:
            print("Please enter a valid value...")
            
    index1 = -1
    index2 =-1
    countD = 0
    for item in fis:
        for item2 in fis:
            countD = 0
            if(item[0] != item2[0]):
                for i in range(12):
                    if data[0][i] == item[0]:
                        index1 = i
                    if data[0][i] == item2[0]:
                        index2 = i
                for i in range(len(data)-1):
                    if data[i+1][index1] == item[1][0] and data[i+1][index2] == item2[1][0]:
                        countD +=1
                
                if countD/1075 >= minSupportValue and (countD/1075)-(item[1][1]/1075)*(item2[1][1]/1075) >= minLeverageValue:
                    RuleString = "IF " + item[0] + " = " + str(item[1][0]) + " THEN " + item2[0] + " = " + str(item2[1][0]) + " --> Support: " + str(countD/1075) + "  -  Levereage: " + str((countD/1075)-(item[1][1]/1075)*(item2[1][1]/1075))
                    if RuleString not in rules:
                        rules.append(RuleString)
                    
                if countD/1075 >= minSupportValue and (countD/1075)-(item2[1][1]/1075)*(item[1][1]/1075) >= minLeverageValue:
                    RuleString = "IF " + item2[0] + " = " + str(item2[1][0]) + " THEN " + item[0] + " = " + str(item[1][0]) + " --> Support: " + str(countD/1075) + "  -  Leverage: " + str((countD/1075)-(item2[1][1]/1075)*(item[1][1]/1075))
                    if RuleString not in rules:
                        rules.append(RuleString)
                        
#Writing the generated rules to "GeneratedRules.txt"
                        
fileRules.write("GENERATED RULES:\n\n")           
for i in range(len(rules)):
    print(rules[i])
    fileRules.write(rules[i]+"\n")
#Closing opened files                
file.close()
fileToWrite.close()
fileRules.close()

#Happy Ending 11.11.19 11:11