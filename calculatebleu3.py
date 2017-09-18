import math
import sys
import os
import string
import codecs
import ast
from os import listdir
g = globals()

def truncate(x, d):
    return int(x*(10.0**d))/(10.0**d)

candPath=sys.argv[1]
refPath=sys.argv[2]
refFiles=[]
#Find if the reference path is a file or a directory. Find path to files
if os.path.isdir(refPath):
    #print("Is directory" + refPath)
    fileList=listdir(refPath)
    #print(type(l))
    fileCount=len(fileList)
    refFiles = [codecs.open(refPath+"/"+fileList[f], "r", encoding='utf-8') for f in range(0,fileCount)]
    refText = []
    for r in range(0, len(refFiles)):
        refText.append([])
        for line in refFiles[r]:
            line = line.strip("\n")
            refText[r].append(line)

    #refFile=refPath+"/"+fileList[0]
    #print(trainFile)

else:
    #print("Is file" + refPath)
    refFile=refPath
    refFileHandle = codecs.open(refFile, "r", encoding='utf-8')
    refText = []
    refText.append([])
    for line in refFileHandle:
        line = line.strip("\n")
        refText[0].append(line)

candFile=codecs.open(candPath,"r", encoding='utf-8')
#candFile=codecs.open("candidate-3.txt","r", encoding='utf-8')
#print(candFile)
#print(candPath)
candText=[]
for line in candFile:
    line=line.strip("\n")
    candText.append(line)
bleuScore1=0
bleuScore2=0
bleuScore3=0
bleuScore4=0
total1,total2,total3,total4=0,0,0,0
fileLen=len(candText)
r=0
c=0
refDict1 = {}
refDict2 = {}
refDict3 = {}
refDict4 = {}
#print(refText[1])
for i in range(0,fileLen):
    candSentence = candText[i].split()
    c+=len(candSentence)
    #print(candSentence)
    diff=[]
    minvalue=0
    for m in range(0,len(refText)):
        #print(len(candSentence), len(refText[m][i].split()))
        reflength=len(refText[m][i])
        diff.append(abs(len(candSentence)-len(refText[m][i].split())))
    #minvalue=min(diff)

    #print(diff)
    #print(minvalue)
    ind=diff.index(min(diff))
    r+=len(refText[ind][i].split())
    #print(c)
    for n in range(0,4):
        # print(m,i)
        #unigram
        if n==0 and len(candSentence)>=n:
            refLenDict1={}
            candDict1 = {}
            for w in range(0, len(candSentence)):
                words = candSentence[w].lower()
                if words not in candDict1:
                    candDict1[words] = 1
                else:
                    candDict1[words] += 1
            for m in range(0,len(refText)):

                refDict1[m]={}
                refSentence=refText[m][i].split()
                for w in range(0, len(refSentence)):
                    words = refSentence[w].lower()
                    if words not in refDict1[m]:
                        refDict1[m][words] = 1
                        refLenDict1[words]=[]
                        #refLenDict1[words].append(refDict1[m][words])
                    else:
                        refDict1[m][words] += 1
                    refLenDict1[words].append(refDict1[m][words])
            for k, v in candDict1.items():
                total1+=candDict1[k]
                if k in refLenDict1:
                    maxRef=max(refLenDict1[k])
                    #print(k,maxRef)
                    if candDict1[k] > maxRef:
                        bleuScore1 += maxRef

                    else:
                        bleuScore1 += candDict1[k]

        elif n==1 and len(candSentence)>=(n+1):
            refLenDict2={}
            candDict2 = {}
            for w in range(0, len(candSentence)-1):
                words = str(candSentence[w:w+2]).lower()
                if words not in candDict2:
                    candDict2[words] = 1
                else:
                    candDict2[words] += 1
            for m in range(0,len(refText)):
                refDict2[m]={}
                refSentence=refText[m][i].split()
                for w in range(0, len(refSentence)-1):
                    words = str(refSentence[w:w+2]).lower()
                    if words not in refDict2[m]:
                        refDict2[m][words] = 1
                        refLenDict2[words]=[]
                        #refLenDict1[words].append(refDict1[m][words])
                    else:
                        refDict2[m][words] += 1
                    refLenDict2[words].append(refDict2[m][words])
            for k, v in candDict2.items():
                total2+=candDict2[k]
                if k in refLenDict2:
                    maxRef=max(refLenDict2[k])
                    #print(k,maxRef)
                    if candDict2[k] > maxRef:
                        bleuScore2 += maxRef

                    else:
                        bleuScore2 += candDict2[k]
        #trigrams
        elif n==2 and len(candSentence)>=(n+1):
            refLenDict3={}
            candDict3 = {}
            for w in range(0, len(candSentence)-2):
                words = str(candSentence[w:w+3]).lower()
                if words not in candDict3:
                    candDict3[words] = 1
                else:
                    candDict3[words] += 1
            for m in range(0,len(refText)):
                refDict3[m]={}
                refSentence=refText[m][i].split()
                for w in range(0, len(refSentence)-2):
                    words = str(refSentence[w:w+3]).lower()
                    if words not in refDict3[m]:
                        refDict3[m][words] = 1
                        refLenDict3[words]=[]
                        #refLenDict1[words].append(refDict1[m][words])
                    else:
                        refDict3[m][words] += 1
                    refLenDict3[words].append(refDict3[m][words])
            for k, v in candDict3.items():
                total3+=candDict3[k]
                if k in refLenDict3:
                    maxRef=max(refLenDict3[k])
                    #print(k,maxRef)
                    if candDict3[k] > maxRef:
                        bleuScore3 += maxRef

                    else:
                        bleuScore3 += candDict3[k]
        #n=4
        elif n==3 and len(candSentence)>=(n+1):
            refLenDict4={}
            candDict4 = {}
            for w in range(0, len(candSentence)-3):
                words = str(candSentence[w:w+4]).lower()
                if words not in candDict4:
                    candDict4[words] = 1
                else:
                    candDict4[words] += 1
            for m in range(0,len(refText)):
                refDict4[m]={}
                refSentence=refText[m][i].split()
                for w in range(0, len(refSentence)-3):
                    words = str(refSentence[w:w+4]).lower()
                    if words not in refDict4[m]:
                        refDict4[m][words] = 1
                        refLenDict4[words]=[]
                        #refLenDict1[words].append(refDict1[m][words])
                    else:
                        refDict4[m][words] += 1
                    refLenDict4[words].append(refDict4[m][words])
            for k, v in candDict4.items():
                total4+=candDict4[k]
                if k in refLenDict4:
                    maxRef=max(refLenDict4[k])
                    #print(k,maxRef)
                    if candDict4[k] > maxRef:
                        bleuScore4 += maxRef

                    else:
                        bleuScore4 += candDict4[k]

#print(total1)
#print(refLenDict1)
#print(bleuScore1)
p1=(bleuScore1/total1)
p2=bleuScore2/total2
p3=bleuScore3/total3
p4=bleuScore4/total4
print(total1,total2,total3,total4)

if(c>r):
    bp=1
else:
    bp=math.exp(1-(r/c))
print(bp)
#p1=truncate(p1,12)
#p2=truncate(p2,12)
#p3=truncate(p3,12)
#p4=truncate(p4,12)

print(p1,p2,p3,p4)
finalScore=(total1*math.log(p1)+ total2*math.log(p2)+ total3*math.log(p3)+total4*math.log(p4))/(total1+total2+total3+total4)
bleuscore=bp*math.exp(finalScore)

print(bleuscore)
modelFile = open('bleu_out.txt', 'w')
modelFile.write(str(bleuscore))

