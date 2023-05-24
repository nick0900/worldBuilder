import argparse
from dbAccess import mydb
import helpfuncs
import sys

parser = argparse.ArgumentParser(
    description = "script to make a significant character of a basic character"
)
parser.add_argument('id', help= 'must be the id of an already existing basic character that is not a significant character yet', type= int)

args = parser.parse_args()

mycursor = mydb.cursor()

id = args.id
mycursor.execute("select characterExtendable(%s)", (id,))
if not mycursor.fetchone()[0]:
  sys.exit("id not extendable, either doesn't exist or is already a significant character")

mycursor.execute("select species, sex, height, weight from characters where characterid = %s", (id,))
x = mycursor.fetchone()

print('Current Basic info of id: ', id)
print('Species: ', x[0], '\nSex: ', x[1], '\nHeight: ', x[2], '\nWeight: ', x[3])

print('FirstName: (not required)')
firstName = helpfuncs.StringNoneCheck(input('>'))

print('FamilyName: (not required)')
familyName = helpfuncs.StringNoneCheck(input('>'))

print('Alias: (not required)')
alias = helpfuncs.StringNoneCheck(input('>'))

age = helpfuncs.StringNoneCheck(helpfuncs.RepeatAskInt('Age years: (not required)\n>', 0, 0, True))

print('Occupation: (not required)')
occupation = helpfuncs.StringNoneCheck(input('>'))

print('Description: (not required)')
description = helpfuncs.StringNoneCheck(helpfuncs.MultiRowTextInput())

mycursor.execute("INSERT INTO SignificantCharacters (characterid, firstname, familyname, alias, age, occupation, characterdescription) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                 (id, firstName, familyName, alias, age, occupation, description))

mydb.commit()