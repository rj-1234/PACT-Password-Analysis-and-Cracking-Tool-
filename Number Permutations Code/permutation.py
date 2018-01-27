#!/usr/bin/python3
'''
Created on 17-Sep-2017

@author: hp
'''
from itertools import permutations, product, repeat

def permutation():

    with open('wordlist.txt','w') as phone_no:
        perms = [''.join(p) for p in permutations('1234567890',6)]
        for i in perms:
            print(i, file = phone_no, end = '\n')
        
def main():
    permutation()
    
if __name__ == '__main__':main()           