import argparse
import helpfuncs
from dbAccess import mydb

def AddBasicCharacter(cursor, species, sex, height, weight):
    cursor.execute("INSERT INTO Characters (species, sex, height, weight) VALUES (%s, %s, %s, %s)", 
                   ( helpfuncs.StringNoneCheck(species), helpfuncs.StringNoneCheck(sex),
                    helpfuncs.StringNoneCheck(height), helpfuncs.StringNoneCheck(weight)))
    return cursor.lastrowid

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "script to add basic character data"
    )
    parser.add_argument('species', help= "Mind the spelling")
    parser.add_argument('sex')
    parser.add_argument('height', help= 'meter', type= float)
    parser.add_argument('weight', help= 'kg', type= float)

    args = parser.parse_args()

    mycursor = mydb.cursor()

    print('Character inserted with ID: ', AddBasicCharacter(mycursor, args.species, args.sex, args.height, args.weight))
    
    mydb.commit()
