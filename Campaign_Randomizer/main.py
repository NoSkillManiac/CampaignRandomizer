# Program: Campaign Randomizer
# Created by Josh Auer
# Conntributors: Dominic Napolitano, Joshua Goodwin, Jonathan Reagan, Alice Keeling, Maura Dickson

from random import randint

setNum = 10
tecNum = 5
magNum = 5
genNum = 5
pccNum = 10

# Define setting
def setting(x):
    return{
        0: "Steampunk",
        1: "Urban Fantasy",
        2: "Post Apocolyptic",
        3: "Modern",
        4: "Planar Travel",
        5: "Wild West",
        6: "Feudal Japan",
        7: "Underwater / High Seas",
        8: "Tribal",
        9: "World in the Sky"
    }.get(x)

# Define Tech / Gun level
def tech_guns(x):
    return{
        0: "Extreme (Everyone has guns)",
        1: "High (Advanced firearms)",
        2: "Average",
        3: "Low",
        4: "None"
    }.get(x)

# Define Magic level
def magic_lev(x):
    return{
        0: "Extreme (Magic items everywhere. Lower cost & spell progression)",
        1: "High (Standard Pathfinder)",
        2: "Medium (6th Level and below. Magic items semi-rare)",
        3: "Low (3rd Level and below. Magic items rare.)",
        4: "None"
    }.get(x)

#Define Genre
def genre(x):
    return{
        0: "Murder Mystery",
        1: "Horror",
        2: "Undead Apocalypse",
        3: "Inter-kingdom Warfare",
        4: "Hunger Games / Tournament"
    }.get(x)

#Define PC alterations
def pcAlt(x):
    return {
        0: "Peasant Campaign",
        1: "EXTREME sizes (Small/Large)",
        2: "Gestalt",
        3: "Sub Intelligence",
        4: "Undead PCs",
        5: "Bandits",
        6: "Class Restriction",
        7: "Multiclass City (X number of levels per class per character)",
        8: "Monster PCs",
        9: "Forced Alignment"
    }.get(x)

#Define PC changes algorithim
# Outputs a string to provide to output based on number of changes made
def pcChange(x):
    pcAlt(x)

#Define Main
def main():
    # Ask for setting alteration
    output = "\n"
    ans = raw_input("Would you like to roll the setting? (y for yes, n for no)")
    if (ans.lower() == 'y'):
        res = randint(0,setNum-1)
        output += "Setting is: " + setting(res) + "\n"
    #Ask for tech alteration
    ans = raw_input("Would you like to roll the tech level? (y for yes, n for no)")
    if (ans.lower() == 'y'):
        res = randint(0, tecNum-1)
        output += "Tech and Guns level is: " + tech_guns(res) + "\n"
    #Ask for magic alteration
    ans = raw_input("Would you like to roll the magic level? (y for yes, n for no)")
    if (ans.lower() == 'y'):
        res = randint(0, magNum-1)
        output += "Magic level is: " + magic_lev(res) + "\n"
    #Ask for Genre alteration
    ans = raw_input("Would you like to roll the genre? (y for yes, n for no)")
    if (ans.lower() == 'y'):
        res = randint(0, genNum-1)
        output += "Genre is: " + genre(res)
    #Ask for PC modification
    ans = raw_input("Would you like to set rules for characters? (y for yes, n for no)")
    if (ans.lower() == 'y'):
        res = randint(0, pccNum - 1)
        output += pcAlt(res)
    print output

main()