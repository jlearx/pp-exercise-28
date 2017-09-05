'''
Created on Aug 31, 2017

@author: jlearx
'''

def getNumber(varNum):
    question = input("Please enter the " + varNum + " value: ")
    questAbs = question.lstrip("-")
    
    # Only true if not a float or a string
    if (questAbs.isdigit()):
        return int(question)
    
    idx = questAbs.find('.')
    
    # If not a float, then it is a string
    if (idx < 0):
        return question
    
    whole = questAbs[:idx]
    fract = questAbs[idx + 1:]
    
    # Only true if not a string
    if (whole.isdigit() and fract.isdigit()):
        return float(question)
    
    # Input is a string
    return question
    

if __name__ == '__main__':
    first = getNumber("first")
    second = getNumber("second")
    third = getNumber("third")
    
    # Check the variable types
    firstIsStr = (type(first) == str)
    secondIsStr = (type(second) == str)
    thirdIsStr = (type(third) == str)
    
    # Make sure the types are compatible to avoid exceptions
    if (firstIsStr or secondIsStr or thirdIsStr):
        if (firstIsStr != True):
            first = str(first)
        if (secondIsStr != True):
            second = str(second)
        if (thirdIsStr != True):
            third = str(third)
    
    # Main logic
    if (first > second):
        if (first > third):
            print("First is the largest!")
        elif (third > first):
            print("Third is the largest!")
        else:
            print("First and third are tied for largest!")
    elif (second > first):
        if (second > third):
            print("Second is the largest!")
        elif (third > second):
            print("Third is the largest!")
        else:
            print("Second and third are tied for largest!")
    else:
        if ((first > third) and (second > third)):
            print("First and second are tied for largest!")
        elif ((third > first) and (third > second)):
            print("Third is the largest!")
        else:
            print("First, second, and third are all tied for largest!")
    