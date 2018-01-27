#!/usr/bin/python3
'''
Created on 16-Sep-2017

@author: hp
'''
import hashlib

def h():
    s = hashlib.sha256(b'password')
    hd = s.hexdigest()
    print(hd)
    
   
    
def main():
    h()
    
if __name__ == "__main__":main()  