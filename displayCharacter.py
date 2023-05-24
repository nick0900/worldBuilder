import argparse
from dbAccess import mydb

def DisplayCharacter(cursor, id):
    cursor.execute("select characterExists(%s)", (id,))
    if cursor.fetchone()[0]:
        cursor.execute("select firstname, familyname, alias, sex, species, age, height, weight, occupation, characterdescription from significantcharacters sc right join characters c on sc.characterid = c.characterid where c.characterid = %s", (id,))
        data = cursor.fetchone()
        
        cursor.execute("select isSignificant(%s)", (id,))
        significant = cursor.fetchone()[0]
        if significant:
            print('//---------------------------Significant Character----------------------------//')
        else:
            print('//------------------------------Basic Character-------------------------------//')
        
        print('ID:',id)

        if data[0] != None:
            print('Name', data[0], 'given.')

        if data[1] != None:
            print('Of family ' + data[1] + '.')

        if data[2] != None:
            print('Known as ' + data[2] + '.')

        message = ''
        if data[3] != None:
            message += data[3]
        if message != '' and data[4] != None:
            message += ' '
        if data[4] != None:
            message += data[4]
        if message != '' and data[5] != None:
            message += ' '
        if data[5] != None:
            message += str(data[5]) + ' years of age'
        if message != '':
            print(message + '.')

        message = ''
        if data[6] != None:
            message += 'Height: ' + str(data[6])
        if message != '' and data[7] != None:
            message += ', '
        if data[7] != None:
            message += 'Weight: ' + str(data[7])
        if message != '':
            print(message + '.')

        if data[8] != None:
            print('Is a ' + data[8] + '.')

        if data[9] != None:
            print(data[9])

        
        print('//----------------------------------------------------------------------------//')

    else:
        print('character of id:', id, ' does not exist')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Displays all data of a character. Both basic and significant"
    )
    parser.add_argument('id', help= 'Character ID', type= int)

    args = parser.parse_args()

    mycursor = mydb.cursor()

    DisplayCharacter(mycursor, args.id)

    mydb.commit()