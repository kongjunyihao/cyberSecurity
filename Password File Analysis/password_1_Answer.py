pfile = open("password1.txt","r")

No_entries = 0
failedLog = 0
failedUserNo = 0
failedUserName = 'x'
pwd = []
num = 0

while True:
    num += 1
    tuple = pfile.readline()
    if not tuple:
        num -= 1
        break
    use = tuple.split(',')
    if(int(use[6])>failedLog):
        failedLog = int(use[6])
        failedUserNo = use[0]
        failedUserName = use[2]
    pwd.append(use[4])

most_used_pwd = 0
for idx, pword1 in enumerate(pwd):
    curr_No = 0
    for jdx, pword2 in enumerate(pwd):
        if(pword1 == pword2):
            curr_No += 1
    if(curr_No>most_used_pwd):
        most_used_pwd = curr_No
        word = pwd[idx]

print("The number of entries in the password  file is:", num)
print("The most commonly used password is:", word)
print("The user who has most failed login attempts is:"+failedUserNo+". Its name is:"+failedUserName+". It has", failedLog, "attempts")
