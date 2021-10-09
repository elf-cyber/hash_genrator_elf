#bin/usr/python3
#Created by : @e_f_l_6_6_6
import hashlib 
import colorama
import time
from bunner import *
import os
import random
 
banner()
os.system('termux-open-url https://t.me/elf_security_cyber')    
time.sleep(5)
while True:
    print(f"{colorama.Fore.RED}[{colorama.Fore.YELLOW}-{colorama.Fore.RED}]loding...!")
    os.chdir("/sdcard")
    f = open("look_at_me.txt","w+")
    c = 50
    for i in range(c):
        printed = '''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%ELF_666%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

        f.write("[-]thank you for follow me "+printed+" \n\nmy channel telgram:@elf_security_cyber "+printed+"\n\n pelese sub me!")
        f.close()
    if c == 50:
       break

if os.name =='nt':
    print("channel : @elf_security_cyber")
else:    

    os.system('termux-open-url https://t.me/elf_security_cyber')    

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')    
buuner()
a = '''
\t   _______________________________________________________________________
\t   |                              _    __                                |
\t   |                        ___  | |  / _|                               |
\t   |                       / _ \ | | | |_                                |
\t   |                      |  __/ | | |  _|                               |
\t   |                      \__\__ |_|_| |                                 |
\t   |                     _________________                               |
\t   |  [¥]14 metod hashed [-]                                             |
\t   |  [£]model hash  [-]                                                 |
\t   |  [&]md5         [1]                                                 |
\t   |  [&]sha1        [2]                                                 |
\t   |  [&]sha224      [3]                                                 |
\t   |  [&]sha256      [4]                                                 |
\t   |  [&]sha384      [5]                                                 |
\t   |  [&]sha512      [6]                                                 |
\t   |  [&]blake2b     [7]                                                 |
\t   |  [&]blake2s     [8]                                                 |
\t   |  [&]sha3_224    [9]                                                 |
\t   |  [&]sha3_256    [10]                                                |
\t   |  [&1]sha3_384   [11]                                                |
\t   |  [&]sha3_512    [12]                                                |
\t   |  [&]shake_128   [13]                                                |
\t   |  [&]shake_256   [14]                                                |
\t   |                                                                     |
\t   _______________________________________________________________________
    
  '''
i = random.randint(1,10)

if i == 1:
    print(colorama.Fore.GREEN+a)
if i == 2: 
    print(colorama.Fore.RED+colorama.Cursor.BACK()+a)
if i ==3 :
    print(colorama.Fore.BLUE+colorama.Style.DIM+a)    
if i == 4:
    print(colorama.Fore.CYAN+colorama.Cursor.BACK(a))
if i == 5:
    print(colorama.Fore.YELLOW+a)
if i == 6:
    print(colorama.Fore.LIGHTWHITE_EX+colorama.Style.DIM+a)
if i == 7:
    print(colorama.Fore.MAGENTA+a)
if i == 8:
    print(colorama.Fore.LIGHTCYAN_EX+a)    
if i == 9:
    print(colorama.Fore.CYAN+colorama.Style.DIM+a)
if i ==10:
    print(colorama.Fore.LIGHTBLACK_EX+colorama.Style.DIM+a)




def hash_md5():
    bunner_1()   
    input(colorama.Fore.GREEN+'enter the named for hashed.md5 : ')
    m = hashlib.md5()
    a = m.hexdigest()
    print(m.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("md5.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+'\n'+p)
            rxt3.close()
    else:
       txt = open("md5.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

def hash_sha1():
    bunner_2()
    input(colorama.Fore.GREEN+'enter the named for hashed.sha1 : ')
    a = hashlib.sha1()
    b = a.hexdigest()
    print(a.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("sha1.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+b+"\n"+p)
            rxt3.close()
    else:
      txt = open("sha1.txt","a")
      for i in range(1):
          txt.write("[-]your hashed : \n"+a+"\n"+p)
          txt.close()
   
def hash_sha224():
    bunner_3()   
    input(colorama.Fore.GREEN+'enter the named for hashed sha224  : ')
    b = hashlib.sha224()
    a = b.hexdigest()
    print(b.hexdigest()) 
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("sha224.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("your hashed :\n"+a+'\n'+p)
            rxt3.close()
    else:
       txt = open("sha224.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

    
    
def hash_sha256():
    bunner_4()
    input(colorama.Fore.GREEN+'enter the named for hashed sha256 : ')
    c = hashlib.sha256()
    a = c.hexdigest()
    print(c.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("sha256.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("sha256.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()



def hash_sha384():
    bunner_5()
    input(colorama.Fore.GREEN+'enter the named for hashed.sha384 : ')
    e = hashlib.sha384()
    a = e.hexdigest()
    print(e.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("sha384.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("sha384.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

    
def hash_sha512():
    bunner_1()   
    result = input(colorama.Fore.GREEN+'enter the naemd for hashed.sha512 : ')
    f = hashlib.sha3_512()
    a = f.hexdigest()
    print(f.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("sha512.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("sha512.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

    
    
def hash_blake2b():
    bunner_2()   
    input(colorama.Fore.GREEN+'enter the named for hashed.blake2b : ')
    g = hashlib.blake2b()
    a = g.hexdigest() 
    print(g.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("blake2b.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("blake2b.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

    
    
def hash_blake2s():
    bunner_4()   
    input(colorama.Fore.GREEN+'enter the named for hashed.blake2s : ')
    h = hashlib.blake2s()
    a = h.hexdigest()
    print(h.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("blake2s.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("blake2s.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

    
    
    
def hash_sha3_224():
    bunner_3()   
    input(colorama.Fore.GREEN+'enter the named for hashed.sha3224  : ')    
    j = hashlib.sha3_224()
    a = j.hexdigest()
    print(j.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("sha3_224.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("sha3_224.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

    
    
def hash_sha3_256():
    bunner()   
    input(colorama.Fore.GREEN+'enter the named for hashed.sha3_256 : ')
    k = hashlib.sha3_256()    
    a = k.hexdigest()
    print(k.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("sha3_256.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("sha3_256.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

def hash_sha3_384():
    bunner_5()   
    input(colorama.Fore.GREEN+'enter the named for hashed.sha3_384 : ') 
    l = hashlib.sha3_384()
    a = l.hexdigest()
    print(l.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("sha3_384.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("sha3_384.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

def hash_sha3_512():
    bunner_2()   
    input(colorama.Fore.GREEN+'enter the named for hashed.sha3_512 : ')
    q = hashlib.sha3_512()
    a = q.hexdigest()
    print(q.hexdigest())
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("sha3_512.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("sha3_512.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()
    
def hash_shake_128():
    bunner_4()   
    input(colorama.Fore.GREEN+'enter the named for hashed.shake_123 : ')
    w = hashlib.shake_128()
    a = w.hexdigest()
    print(w.hexdigest()) 
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("shake_128.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("shake_128.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()

def hash_shake_256():
    bunner_1()   
    input("enter the name for hash shake_256")
    r = hashlib.shake_256()
    a = r.hexdigest
    print(r.hexdigest())    
    res = input('save to sdcard and new file? ')
    if res == 'yes':    
        os.chdir('/sdcard')
        rxt3 = open("shake_256.txt","w+")     
        p = "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"     
        for i in range(1):
            rxt3.write("[-]your hashed : \n"+a+"\n"+p)
            rxt3.close()
    else:
       txt = open("shake_256.txt","a")
       for i in range(1):
           txt.write("[-]your hashed : \n"+a+"\n"+p)
           txt.close()



a1 = '1'
a2 = '2'
a3 = '3'
a4 = '4'
a5 = '5'
a6 = '6'
a7 = '7'
a8 = '8'
a9 = '9'
a10 = '10'
a11 = '11'
a12 = '12'
a13 = '13'
a14 = '14'

for i in range(0 ,1):
    b1 = input(colorama.Fore.CYAN+colorama.Back.BLACK+'enter the number [1 & 14] : ')
    if b1 == a1 :
        hash_md5()
    if b1 == a2 :
        hash_sha1()
    if b1 == a3 : 
        hash_sha224()
    if b1 == a4 : 
        hash_sha256()
    if b1 == a5 : 
        hash_sha384()
    if b1 == a6 : 
        hash_sha512()    
    if b1 == a7 : 
        hash_blake2b()
    if b1 == a8 :
        hash_blake2s()
    if b1 == a9 : 
        hash_sha3_224()
    if b1 == a10 :
        hash_sha3_256()
    if b1 == a11 : 
        hash_sha3_384()
    if b1 == a12 :
        hash_sha3_512()
    if b1 == a13 :           
        hash_shake_128()
    if b1 == a14 :
        hash_shake_256()
    if b1 == 'exit':
        break
os.system('termux-open-url https://t.me/elf_security_cyber')    











