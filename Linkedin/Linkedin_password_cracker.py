#!/usr/bin/python3
'''
Created on 19-Sep-2017

@author: hp
'''
import hashlib
def main():
    password_cracker()
    
    
def password_cracker():
    with open('Linkedin_wordlist.txt') as infile:
        for line in infile.readlines():
            word = line.rstrip('\n')
            byte = word.encode()
            hashed_byte = hashlib.sha1(byte)
            hash_generated = hashed_byte.hexdigest()
            hash_generated = hash_generated.replace(hash_generated[:5], '00000')
            
            with open('SHA1.txt') as infile2:
                for sline in infile2.readlines():
                    sline = sline.rstrip('\n')
                    if (sline == hash_generated):
                        with open('Linkedin_cracked_password.txt','a') as outfile:
                            print(hash_generated,word, sep = ' ', file = outfile,end = '\n', flush = True)
                        break    
            

                    
if __name__ == '__main__':main()        