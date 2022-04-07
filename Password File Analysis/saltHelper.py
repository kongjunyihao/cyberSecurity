import hashlib
import multiprocessing as mp

wl = open("wordList.txt","r")
pf = wl.read().splitlines()
plaintext = []
for i in range(len(pf)):
    plaintext.append(pf[i])

pfile = open("password2.txt","r")
ciphertext =  []

while True:
    pline = pfile.readline()
    if not pline:
        break
    tuple = pline.split(',')
    ciphertext.append(tuple[4])

def saltAnalysis(plain,cipher):
    password = 'x'
    saltword = 'x'
    for idx in range(len(plain)):
        for jdx in range(len(plain)):
            if(idx != jdx):
                pwd = plain[idx] + plain[jdx]
                res = hashlib.md5(pwd.encode())
            
                for k in range(len(cipher)):
                    if(hashlib.md5(pwd.encode()).hexdigest() == cipher[k]):
                        password = plain[idx]
                        saltword = plain[jdx]
                        print(password+saltword)
                        break
    print("The salt that was added to each password is:"+saltword)

if __name__ =='__main__':
    plain,cipher = plaintext,ciphertext
    p1 = mp.Process(target = saltAnalysis, args = (plain,cipher,))
    p1.start()
    p1.join()