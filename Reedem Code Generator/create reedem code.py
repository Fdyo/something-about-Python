__author__ = 'Fdyo'
#coding: utf-8
from random import choice
import string

def create_code(code_numbers):
    code_key = ''
    for code_number in range(code_numbers):
        code_key += choice(string.ascii_uppercase+string.digits)
    return code_key

def get_code_keys(code_numbers, counts):
    code_keys = []
    for count in range(counts):
        code_keys.append(create_code(code_numbers))
    return code_keys

filename = 'code_keys.txt'
with open(filename, 'w') as f_obj:
    code_keys = get_code_keys(30, 30)
    for code_key in code_keys:
        remind = 'Your reedem code is ' + code_key
        f_obj.write(remind + '\n' )