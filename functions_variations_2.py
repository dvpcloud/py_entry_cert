#!/usr/bin/env python3.7

def is_palindrome(palin_word):
    if isinstance(palin_word,str):
        reverse_string = palin_word[::-1]
        if palin_word == reverse_string:
            return True
        else:
            return False
    elif isinstance(palin_word,int):
        #num = list(palin_word)
        num = str(palin_word)
        print(num)
        reverse_num = num[::-1]
        if num == reverse_num:
            return True
        else:
            return False
         

assert is_palindrome("malayalam") == True, f"Exptected true but got {is_palindrome('malayalam')}"

assert is_palindrome(10101) == True, f"Expected true but got {is_palindrome(10101)}"

#is_palindrome(10101)

def build_list(item, count=1):
    list_t_return = []    
    for _ in range(count):
        list_t_return.append(item)
        #list_t_return += item
        print(list_t_return)
    return list_t_return

assert build_list('Apple',3) == ["Apple","Apple","Apple"], f"Expected ['Apple','Apple','Apple'] but received { repr(build_list('Apple',3))}"



