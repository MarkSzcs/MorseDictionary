import json
import argparse
import sys
import argparse
import binascii
import secrets
import codecs
import base64


global DICTIONARY_PATH
DICTIONARY_PATH = "morse_dictionary.json"

def initialize_dictionary(path):
    f = open(path, "rb")
    global JMORSE
    global REVJMORSE
    JMORSE = json.load(f)
    REVJMORSE = dict()
    key_list = list(JMORSE.keys())
    val_list = list(JMORSE.values())
    n = len(key_list)
    for i in range(n):
        key = val_list[i]
        val = key_list[i]
        REVJMORSE[key] = val

def encode(plain):
    cypher = ""
    for i in range(len(str(plain))):
        if(plain[i] == " "):
            cypher += " "
        elif plain[i] in JMORSE.keys():
            cypher += JMORSE[plain[i]]
        else:
            pass
    return cypher
            
def decode(cypher): #you should read in the first 5 chars of the input and check if not then drop the last one and so on
    plain = ""
    for i in range(len(str(cypher))):
        temp = ""
        if cypher[i] in JMORSE.values():
            plain += REVJMORSE[cypher[i]]
        elif " ":
            plain += " "
        else:
            temp = cypher[i]
            while(len(temp) > 0):
                if cypher[i] in JMORSE.values():
                    plain += REVJMORSE[temp]
                    i += len(temp)
                    break
                elif(len(temp) or cypher[i] == " "):
                    plain += " "
                    i += len(temp)
                    break
                else:
                    temp += cypher[i+len(temp)]
    return plain
    

def main():
    initialize_dictionary(DICTIONARY_PATH)
    sample_text = "SOS Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    cypher = encode(sample_text.lower())
    print(cypher)
    plain = decode(cypher.lower())
    print(plain)
    
if __name__ == "__main__":
    main()
    
