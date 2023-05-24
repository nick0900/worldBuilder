import argparse
from dbAccess import mydb

def ListSignificantCharacters(cursor):
    cursor.execute("select firstname, familyname, alias, sex, species, occupation, sc.characterid from significantcharacters sc join characters c on sc.characterid = c.characterid")
    x = cursor.fetchall()
    
    
    print('//--------------------------Significant Characters----------------------------//')
    
    for data in x:
        print('ID: ' + str(data[6]) + ' --//' + str(data[2]) + ' ' + str(data[0]) + ', ' + str(data[1]) + ': '
                + str(data[3]) + ', ' + str(data[4]) + ', ' + str(data[5]) + './/--')
    
    print('//----------------------------------------------------------------------------//')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Lists all significant character entries, use displaycharacter with the corresponding id for more detailed information of an entry."
    )

    args = parser.parse_args()

    mycursor = mydb.cursor()

    ListSignificantCharacters(mycursor)

    mydb.commit()