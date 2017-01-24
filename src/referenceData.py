from compiler.ast import flatten
import os

crimeList = []

scores={}
crimeList={}
currPath = os.getcwd()
PROJECT_DIR=currPath.strip('src')
exportDir = os.path.join(PROJECT_DIR,'InputFiles')

def AfinDict():
    afinnfile = open(os.path.join(exportDir, 'AFINN-111.txt'))
    for line in afinnfile:
        term, score  = line.split("\t")                          # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)                                # Convert the score to an integer.

    return scores

def crimeWords():
    ocfile = open(os.path.join(exportDir, 'crimeWords'))
    #ocfile = open("crimeWords")
    for line in ocfile:
        line = line.lower()                                      # Convert into lower case string
        crimeList.append((line.splitlines()))
    return flatten(crimeList)                                    # return a flatten list instead of a nested list. The above was creating a nested list
