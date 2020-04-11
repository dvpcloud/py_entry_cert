#!/usr/bin/env python3.7

def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    #first_name = names[0]
    #last_name = names[-1]

    return {
        'firstname' : first_name,
        'lastname': last_name,
    }

assert split_name("somefirst test somelast") == {
    "firstname": "somefirst",
    "lastname": "test somelast",
}, f"Expected {{'firstname':'somefirst', 'lastname':'somelast'}} but received {split_name('somefirst somelast')}"