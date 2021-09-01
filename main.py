# this program will censor swearwords in a .txt file
import string

censor = "*"
swearList = ["fuck", "shit", "bitch", "nigga", "cunt"]
censoredList = []


def write_line(text_list, file_name):
    file_name = file_name + " (censored)"
    f = open("TextFiles/" + file_name, "wt")
    f.write("censored ver: \n\n")

    f = open("TextFiles/" + file_name, "at")
    for x in text_list:
        f.write(x)


def censor_word(word):
    censored_word = word
    altword = word.translate(str.maketrans("", "", string.punctuation))
    for swearWord in swearList:
        if swearWord in altword.lower():
            censored_word = word[:2] + censor + word[3:]
    return censored_word


# read each line and then each word
def read_word():
    f = open("TextFiles/text1.txt", "rt")
    for line in f:
        for word in line.split():
            # print(word)
            censoredWord = censor_word(word)
            # replace swearword with censored swearword
            line = line.replace(word, censoredWord)
        censoredList.append(line)
    f.close()


read_word()
write_line(censoredList, "text1.text")

