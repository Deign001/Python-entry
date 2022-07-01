#!/bin/python3
def split_name(name):
    names = name.split(maxsplit=1)
    return {
        'first_name': first_name,
        'last_name': last_name,
    }
assert split_name("Kevin Bacon") == {
    "first_name": "Kevin",
    "last_name": "Bacon",
},    f"expected {{'first_name': 'Kevin, 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"
    

assert split_name("Victor Von Doom") == {
   "first_name": "Victor",
    "last_name": "Von Doom",
},    f"expected {{'first_name': 'Victor, 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"    

