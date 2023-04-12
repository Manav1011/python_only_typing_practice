from essential_generators import DocumentGenerator
import json
import random
import sys


file=open('para.json','r')
ParaGraphs= json.loads(file.read())

mostCommon=open('most_common.json','r')
MostCommonWords=(json.loads(mostCommon.read()))


Common=open('words.json','r')
CommonWords=(json.loads(Common.read()))

def ParaGraphGeneratorEasy():    
    SendableWords=''
    index=random.randint(0,len(MostCommonWords)-1)   
    # print(MostCommonWords) 
    return MostCommonWords[str(index)][0].lower()

def ParaGraphGeneratorMedium():
    SendableWords=''
    index=random.randint(0,len(CommonWords)-400)
    print(index)
    print(len(CommonWords)-400)    
    for i in range(0,300):
        SendableWords+=CommonWords[str(index + i)][0]+' '
    return SendableWords

def ParaGraphGeneratorHard():
    index=random.randint(0, len(ParaGraphs))
    return ParaGraphs[str(index)]

def ParaGraphGeneratorExtreme():
    gen = DocumentGenerator()
    raw_paragraph=gen.paragraph(20,25)    
    return raw_paragraph

def erase_line():
    sys.stdout.write('\r')
    sys.stdout.write('\033[K')

def erase_last_character():
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    sys.stdout.write('\b')
