import argparse
from dbAccess import mydb

def DeleteBasicCharacter(cursor, id):
    cursor.execute("select characterExists(%s)", (id,))
    if cursor.fetchone()[0]:
        cursor.execute("select isSignificant(%s)", (id,))
        if not cursor.fetchone()[0]:
            cursor.execute("delete from characters where characterid = %s",(id,))
            print('Deleted basic character data', id)
        else:
            print('character of id:', id, ' is a significant character. use the corresponding delete command to remove')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Deletes the basic character with the given ID. you are not able to delete significant characters with this command"
    )
    parser.add_argument('id', help= 'Character ID', type= int)

    args = parser.parse_args()

    mycursor = mydb.cursor()

    DeleteBasicCharacter(mycursor, args.id)

    mydb.commit()