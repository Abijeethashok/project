import csv
from collections import Counter

with open('124421.csv',newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)

def mean(meanofdata):

    weight = []

    for i in range(len(meanofdata)):
        num = filedata[i][2]
        weight.append(float(num))
        
    

    n = len(weight)

    total = 0

    for x in weight:
        total = total + x

    mean =  total/n
    return mean

print(mean(filedata))

def median(medianofdata):

    heightmeadian = []

    for i  in range(len(medianofdata)):
        num1 = filedata[i][2]
        heightmeadian.append(float(num1))

    n = len(heightmeadian)
    heightmeadian.sort()
 
    if n%2 == 0:
        median1 = float(heightmeadian[n//2])
        median2 = float(heightmeadian[n//2-1])
        median = (median1 + median2) /2

    else:
        median = heightmeadian[n//2]
    return(median)

print(median(filedata))

def mode(modeofdata):
    height = []

    for i  in range(len(modeofdata)):
        num = filedata[i][2]
        height.append(float(num))

    data = Counter(height)

    modedata = {"75-85":0 ,"85-95":0,"95-105":0,"105-115":0,"115-125":0,"125-135":0,"135-145":0,"145-155":0,"155-165":0,"165-175":0}

    for height,occ in data.items():
        if 75 < float(height) < 85:
            modedata["75-85"] += occ
        elif 85 < float(height) < 95:
            modedata["85-95"] += occ
        elif 95 < float(height) < 105:
            modedata["95-105"] += occ
        elif 105 < float(height) < 115:
            modedata["105-115"] += occ
        elif 115 < float(height) < 125:
            modedata["115-125"] += occ
        elif 125 < float(height) < 135:
            modedata["125-135"] += occ
        elif 135 < float(height) < 145:
            modedata["135-145"] += occ
        elif 145 < float(height) < 155:
            modedata["145-155"] += occ
        elif 155 < float(height) < 165:
            modedata["155-165"] += occ
        elif 165 < float(height) < 175:
            modedata["165-175"] += occ




    moderange,modeocc = 0,0

    for range1,occ in modedata.items():
        if occ > modeocc:
            moderange,modeocc = [int(range1.split("-")[0]),int(range1.split("-")[1])],occ
    mode = float((moderange[0]+ moderange[1])/2)
    return mode

print(mode(filedata))







