from essential_generators import DocumentGenerator
import json
import random

gen = DocumentGenerator()


file=open('para.json','r')
ParaGraphs= json.loads(file.read())

mostCommon=open('most_common.json','r')
MostCommonWords=(json.loads(mostCommon.read()))


Common=open('words.json','r')
CommonWords=(json.loads(Common.read()))

def ParaGraphGeneratorEasy(request):
    SendableWords=''
    index=random.randint(0,len(MostCommonWords)-302)
    print(index)
    print(len(MostCommonWords)-300)
    for i in range(0,300):
        SendableWords+=MostCommonWords[str(index+i)][0]+' '
    return SendableWords

def ParaGraphGeneratorMedium(request):
    SendableWords=''
    index=random.randint(0,len(CommonWords)-400)
    print(index)
    print(len(CommonWords)-400)    
    for i in range(0,300):
        SendableWords+=CommonWords[str(index + i)][0]+' '
    return SendableWords

def ParaGraphGeneratorHard(request):
    index=random.randint(0, len(ParaGraphs))
    return ParaGraphs[str(index)]

def ParaGraphGeneratorExtreme(request):
    raw_paragraph=gen.paragraph(20,25)    
    return raw_paragraph
