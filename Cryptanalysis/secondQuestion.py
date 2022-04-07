from collections import Counter

secondQuestion = open("question2.txt","r")
freq = {}

while True:
    qline = secondQuestion.readline()
    if not qline:
        break
    for i in range(len(qline)):
        if qline[i] in freq.keys():
            freq[qline[i]] += 1
        else:
            freq[qline[i]] = 1

freq.pop("?")
freq.pop("\n")

entry_sum = 0
for i,j in freq.items():
    entry_sum += j
for i,j in freq.items():
    freq[i] = j/entry_sum

print(freq)

keywords_dict = {'A':'I','B':'J','C':'K','D':'D','E':'G','F':'L','G':'M',
            'H':'N','I':'E','J':'O','K':'P','L':'U','M':'','N':'C',
            'O':'S','P':'T','Q':'U','R':'H','S':'A','T':'V',
            'U':'B','V':'F','W':'W','X':'X','Y':'Y','Z':'Z'}

output = open("questionAnswer.txt","w")
answer = open("question2.txt","r")

while True:
    aline = answer.readline()
    if not aline:
        break
    str1 = ""
    lineSpace = aline.split('?')
    for i in range(len(lineSpace)):
        for j in range(len(lineSpace[i])):
            for k,v in keywords_dict.items():
                if lineSpace[i][j] == k:
                    str1 += v
        lineSpace[i] = str1
        str1 = ""
    lineOuput = ' '.join(lineSpace)
    output.write(lineOuput)
    output.write("\n")
output.close()