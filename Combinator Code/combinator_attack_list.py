#!/usr/bin/python3
'''
Created on 17-Sep-2017

@author: hp
'''

def combinator():
   with open('test_password_list.txt') as infile:
        for line in infile.readlines():
            word = line.rstrip('\n')
        
            with open('test_password_list2.txt','r') as salt:    
                for fline in salt.readlines():
                    fline = fline.rstrip('\n')
                    word1 = fline+word
                    with open('new_test_password_list.txt','a') as outfile:
                        print(word1, file = outfile,end = '\n')
                       
        
def main():
    combinator()
    
if __name__ == '__main__':main()           