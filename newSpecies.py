import argparse
from dbAccess import mydb
import helpfuncs

def AddSpecies(cursor):
    while True:
        print('ScientificName: (required unique)')
        name = helpfuncs.StringNoneCheck(input('>'))
        if name == None:
            print('Name cant be null')
        else:
            cursor.execute("select * from species where scientificname = %s", (name,))
            if len(cursor.fetchall()) != 0:
                print('Species already exists')
            else:
                break

    print('Description: (not required)')
    description = helpfuncs.StringNoneCheck(helpfuncs.MultiRowTextInput())
    cursor.execute("INSERT INTO species (scientificname, speciesdescription) VALUES (%s, %s)", (helpfuncs.StringNoneCheck(name), helpfuncs.StringNoneCheck(description)))

    return name

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "script to create a new species"
    )
    args = parser.parse_args()

    mycursor = mydb.cursor()
    AddSpecies(mycursor)
    mydb.commit()
