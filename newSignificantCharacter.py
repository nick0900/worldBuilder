import argparse

parser = argparse.ArgumentParser(
    description = "script to create a new character"
)

args = parser.parse_args()

from dbAccess import mydb

mycursor = mydb.cursor()

import helpfuncs
from newSpecies import AddSpecies

print('FirstName: (not required)')
firstName = helpfuncs.StringNoneCheck(input('>'))

print('FamilyName: (not required)')
familyName = helpfuncs.StringNoneCheck(input('>'))

print('Alias: (not required)')
alias = helpfuncs.StringNoneCheck(input('>'))

print('Sex: (not required)')
sex = helpfuncs.StringNoneCheck(input('>'))

height = helpfuncs.StringNoneCheck(helpfuncs.RepeatAskFloat('Height m: (not required)\n>', 0, 0, True))

weight = helpfuncs.StringNoneCheck(helpfuncs.RepeatAskFloat('Weight kg: (not required)\n>', 0, 0, True))

species = None
while True:
    ans = helpfuncs.RepeatAskInt('Species: (not required)\n(1) Add later \n(2) Add existing \n(3) Add new \n>', 1, 3)
    if ans == 1:
        break
    elif ans == 2:
        mycursor.execute("select scientificname from species")
        speciesNames = mycursor.fetchall()
        message = '(0) cancel\n'
        i = 1
        for x in speciesNames:
            message += '(' + str(i) + ') ' + x[0] + '\n'
            i +=1
        message += '>'
        ans = helpfuncs.RepeatAskInt(message, 0, i)
        if ans != 0:
            species = speciesNames[ans - 1][0]
            break
    elif ans == 3:
        species = AddSpecies(mycursor)
        break
species = helpfuncs.StringNoneCheck(species)

age = helpfuncs.StringNoneCheck(helpfuncs.RepeatAskInt('Age years: (not required)\n>', 0, 0, True))

print('Occupation: (not required)')
occupation = helpfuncs.StringNoneCheck(input('>'))

print('Description: (not required)')
description = helpfuncs.StringNoneCheck(helpfuncs.MultiRowTextInput())

mycursor.execute("INSERT INTO Characters (species, sex, height, weight) VALUES (%s, %s, %s, %s)", (species, sex, height, weight))

id = mycursor.lastrowid

mycursor.execute("INSERT INTO SignificantCharacters (characterid, firstname, familyname, alias, age, occupation, characterdescription) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                 (id, firstName, familyName, alias, age, occupation, description))

print('Character inserted with ID: ', id)

mydb.commit()
