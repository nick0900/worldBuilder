import argparse
from dbAccess import mydb
from deleteBasicCharacter import DeleteBasicCharacter

def DeleteSignificantCharacter(cursor, id):
    cursor.execute("select characterExists(%s)", (id,))
    if cursor.fetchone()[0]:
        cursor.execute("select isSignificant(%s)", (id,))
        if cursor.fetchone()[0]:
            cursor.execute("delete from significantcharacters where characterid = %s",(id,))
            print('Deleted significant character data', id)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Deletes the significant character data of a character, not removing the basic data"
    )
    parser.add_argument('-full', help= 'Will remove basic character entry as well as significant', action='store_true')
    parser.add_argument('id', help= 'Character ID', type= int)

    args = parser.parse_args()

    mycursor = mydb.cursor()

    DeleteSignificantCharacter(mycursor, args.id)

    if (args.full):
        DeleteBasicCharacter(mycursor, args.id)

    mydb.commit()