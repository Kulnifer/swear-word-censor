# this program will censor swearwords in a .txt file
import string

textList = ["HAVE YOU CHECK YOUR", "BUTTHOLE???"]
swearList = ["fuck", "shit"]

def writeLine(textList):
    f = open("TextFiles/text1.txt", "wt")
    f.write("censored ver: \n\n")

    f = open("TextFiles/text1.txt", "at")
    for x in textList:
        f.write(x + "\n")


# read each line and then each word
def read_word():
    for line in f:
        for word in line.split():
            # print(word)
            altword = word.translate(str.maketrans("","",string.punctuation))
            if altword.lower() == swearList[0]:
                print(word)


f = open("TextFiles/text1.txt", "rt")

#for line in f:
    #print(line)
read_word()



f.close()
