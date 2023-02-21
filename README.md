# NETgenerator
A random generator for Cyberpunk RED 's NET dimension. I'll try to code a random NET infrastructure for cyberpunk RED, mostly in python. When the python version suits me well i'll maybe make it in rust to learn the language.

# Description

The generator aims to randomize a NET architecture, ruled by the GM's needs. It can be for instance a floor cap, overall difficulty level, infrastructure cost... 
The overall goal is to let the GM play on the generated program and to progress on its instance. 
The GM prompt a difficulty and or requirement for his NET architecture, such as a set number of node, of file ...

# main program goal

The user needs to launch only main program. Main should ask for either launching a NET generation or editing the data base.
Editing data base is here to add encounter to the basic ones.
The NET generation is complety random or abide by a set of rule selected by the GM. Then it'll give an overview of the current generated NET. GM can take it or change it. When the NET satisfies the GM's needs, the GM will "play" on the current NET.
GM enters in the first floor and progress in each floor with their Netrunners. The program will ask if Netrunners bypass encounter such as nodes, files, password ... and then it will ask which "door" the Netrunners take if their is a branch entry.
If Netrunner encounters BlackICE program, the programm will ask who's playing, Netrunner or BlackICE. The program will play for BlackICE,
GM can discard the program play if they want to roll the dice themselves. 

# floor.py
floor.py defines the class floor and the class NET. <floor> acts like a node of a graph countaining data. It has a supposed unique id, a level which is its graph deepness, its children, and what's inside. NET is a set of floor and applies the same attribute to each of its elements.

# net_building.py

Construct an empty NET randomly




# Depedencies
- pyhton 3.11
- numpy

# TO DO
- data storage (to continue)
- part that can add data or remove data (for homebrew content). SHOULD NOT TOUCH DEFAULT TABS
- filling floor program
- printing program
- main program