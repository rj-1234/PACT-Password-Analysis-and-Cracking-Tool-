#!/usr/bin/python3
'''
Created on 19-Sep-2017

@author: hp
'''
def main():
    password_cracker()
    
    
def password_cracker():
    with open('yahoo_wordlist.txt') as infile:
        for line in infile.readlines():
            line = line.rstrip('\n')  
            matcher(line)
            
def matcher(str):
        with open('password.file') as infile2:    
            for xline in infile2.readlines():
                xline = xline.rstrip('\n')
                sline = xline.split('.com:',1)[-1]
                if (sline == str):
                    with open('yahoo_cracked_passwords.txt','a') as yahoo_cracked:
                        xline = xline.split(":",1)[-1]
                        print(xline, str, sep =' ', file = yahoo_cracked, end = '\n')
                        break
                    break
                
            
                       
                                    
                    
if __name__ == '__main__':main()        