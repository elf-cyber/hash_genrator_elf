#bin/usr/python3
#created by : @e_f_l_6_6_6
import hashlib 
import colorama 
import time
from bunner import *
import os 
os.system('clear' or 'cls' )
buuner()
time.sleep(3)
print(Fore.RED+colorama.Back.BLACK+colorama.Style.DIM+'''
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
    
  ''')
def hash_md5():
    bunner_1()   
    result = input(colorama.Fore.GREEN+'enter the named for hashed.md5 : ')
    m = hashlib.md5()
    m.hexdigest()
    print(m.hexdigest())

def hash_sha1():
    bunner_2()
    result = input(colorama.Fore.GREEN+'enter the named for hashed.sha1 : ')
    a = hashlib.sha1()
    a.hexdigest()
    print(a.hexdigest())
        
def hash_sha224():
    bunner_3()   
    result = input(colorama.Fore.GREEN+'enter the named for hashed sha224  : ')
    b = hashlib.sha224()
    b.hexdigest()
    print(b.hexdigest()) 

def hash_sha256():
    bunner_4()
    result = input(colorama.Fore.GREEN+'enter the named for hashed sha256 : ')
    c = hashlib.sha256()
    c.hexdigest()
    print(c.hexdigest())

def hash_sha384():
    bunner_5()
    result = input(colorama.Fore.GREEN+'enter the named for hashed.sha384 : ')
    e = hashlib.sha384()
    e.hexdigest()
    print(e.hexdigest())

def hash_sha512():
    bunner_1()   
    result = input(colorama.Fore.GREEN+'enter the naemd for hashed.sha512 : ')
    f = hashlib.sha3_512()
    f.hexdigest()
    print(f.hexdigest())

def hash_blake2b():
    bunner_2()   
    result = input(colorama.Fore.GREEN+'enter the named for hashed.blake2b : ')
    g = hashlib.blake2b()
    g.hexdigest() 
    print(g.hexdigest())

def hash_blake2s():
    bunner_4()   
    result = input(colorama.Fore.GREEN+'enter the named for hashed.blake2s : ')
    h = hashlib.blake2s()
    h.hexdigest()
    print(h.hexdigest())
    
def hash_sha3_224():
    bunner_3()   
    result = input(colorama.Fore.GREEN+'enter the named for hashed.sha3224  : ')    
    j = hashlib.sha3_224()
    j.hexdigest()
    print(j.hexdigest())
    
def hash_sha3_256():
    bunner()   
    result = input(colorama.Fore.GREEN+'enter the named for hashed.sha3_256 : ')
    k = hashlib.sha3_256()    
    k.hexdigest()
    print(k.hexdigest())
    
def hash_sha3_384():
    bunner_5()   
    result = input(colorama.Fore.GREEN+'enter the named for hashed.sha3_384 : ') 
    l = hashlib.sha3_384()
    l.hexdigest()
    print(l.hexdigest())

def hash_sha3_512():
    bunner_2()   
    result = input(colorama.Fore.GREEN+'enter the named for hashed.sha3_512 : ')
    q = hashlib.sha3_512()
    q.hexdigest()
    print(q.hexdigest())
    
def hash_shake_128():
    bunner_4()   
    result = input(colorama.Fore.GREEN+'enter the named for hashed.shake_123 : ')
    w = hashlib.shake_128()
    w.hexdigest()
    print(w.hexdigest()) 

def hash_shake_256():
    bunner_1()   
    result = input(colorama.Fore.GREEN+'enter the namwd for hashed.shake_256 : ')
    r = hashlib.shake_256()
    r.hexdigest()
    print(r.hexdigest())    

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
    b1 = input(Fore.CYAN+Back.BLACK+'enter the number [1 & 14] : ')
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












