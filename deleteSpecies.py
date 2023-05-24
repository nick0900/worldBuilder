import argparse
from dbAccess import mydb

def DeleteSpecies(cursor, name):
    cursor.execute("select isSpecies(%s)", (name,))
    if cursor.fetchone()[0]:
        cursor.execute("delete from species where scientificname = %s",(name,))
        print('Deleted species', name)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Deletes a species"
    )
    parser.add_argument('name', help= 'Scientific name of the species')

    args = parser.parse_args()

    mycursor = mydb.cursor()

    DeleteSpecies(mycursor, args.name)

    mydb.commit()