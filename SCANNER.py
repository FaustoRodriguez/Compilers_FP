keywords = ["int","float","string","for","if","else","while","return","read","write","void"]
specialSymbols =["+","-","*","/","<","<=",">",">=","==","!=","=",";",",","\"",".","(",")","[","]","{","}",]

def isStartofComment(word):
    return "/*" in word
def isEndofComment(word):
    return "*/" in word

def isKeyword(word):
    return word in keywords

def isSpecialSymbol(word):
    return word in specialSymbols

def scan(file):
    lines = open(file,'r')
    output = []
    comment = False
    for line in lines:
        words = line.split()
        for word in words:
            if comment:
                if isEndofComment(word):
                    comment = False
            else:
                if isStartofComment(word):
                    comment = True
                    continue
                else:
                    if isKeyword(word):
                        output.append(keywords.index(word))
                    if isSpecialSymbol(word):
                        output.append(specialSymbols.index(word))
    return output
print(scan("test_code.cmm"))