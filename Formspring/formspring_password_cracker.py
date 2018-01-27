#!/usr/bin/python3
'''
Created on 19-Sep-2017

@author: hp
'''
import hashlib
from itertools import  product, repeat

def main():
    with open('salt_file.txt','w') as salt:
        perms = [''.join(p) for p in product('0123456789',repeat = 2)]
                
        for i in perms:
            print(i, file = salt, end = '\n')
    password_cracker()
    
    
def password_cracker():                
    with open('formspring_wordlist.txt') as infile:
        for line in infile.readlines():
            word = line.rstrip('\n')
        
            with open('salt_file.txt','r') as salt:    
                for fline in salt.readlines():
                    fline = fline.rstrip('\n')
                    word1 = fline+word
                    print(word1)    
                    byte = word1.encode()
                    
                    hashed_byte = hashlib.sha256(byte)
                    hash_generated = hashed_byte.hexdigest()
                    
                        
                        
                    with open('formspring.txt') as infile2:
                        for sline in infile2.readlines():
                            sline = sline.rstrip('\n')
                            if (sline == hash_generated):
                                with open('formspring_cracked_passwords.txt','a') as outfile:
                                    print(hash_generated,word, sep = ' ', file = outfile,end = '\n', flush = True)
                                break    
            

                    
if __name__ == '__main__':main()        