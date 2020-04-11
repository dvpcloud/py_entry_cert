#!/usr/bin/env python3.7

def char_range(start,stop, step=1):

    start_code = ord(start)
    stop_code = ord(stop)

    for character in range(start_code,stop_code+1,step):
        yield chr(character)

assert char_range('a','d') == ['a','b','c','d'], f"Expected ['a','b','c','d'] but got {repr(char_range('a','b'))}"