import argparse
import helpfuncs
import traceback
from dbAccess import mydb
from newSpecies import AddSpecies

def AlterCharacter(cursor, id):
    cursor.execute("select characterExists(%s)", (id,))
    if cursor.fetchone()[0]:
        field = ['species', 'sex', 'height', 'weight', 'firstname', 'familyname', 'alias', 'age', 'occupation', 'characterdescription']
        while True:
            try:
                cursor.execute("select species, sex, height, weight from characters where characterid = %s", (id,))
                x = cursor.fetchone()

                cursor.execute("select firstname, familyname, alias, age, occupation, characterdescription from significantcharacters where characterid = %s", (id,))
                y = cursor.fetchone()
                
                print('Current info of id: ', id)
                print('Species: ', x[0], '\nSex: ', x[1], '\nHeight: ', x[2], '\nWeight: ', x[3])
                options = 4
                message = '(0): Done\n(1): Species\n(2): Sex\n(3): Height\n(4): weight'

                if  y != None:
                    print('First name: ', y[0], '\nFamily Name: ', y[1], '\nAlias: ', y[2], '\nAge: ', y[3], '\nOccupation: ', y[4], '\nDescription:\n', y[5])
                    options += 6
                    message += '\n(5): First Name\n(6): Family Name\n(7): Alias\n(8): Age\n(9): Occupation\n(10): Description'

                ans = helpfuncs.RepeatAskInt(message + '\n>', 0, options)
                if ans == 0: return
                data = None
                if ans == 1:
                    while True:
                        ans2 = helpfuncs.RepeatAskInt('Species:\n(1) None \n(2) Add existing \n(3) Add new \n>', 1, 3)
                        if ans2 == 1:
                            break
                        elif ans2 == 2:
                            cursor.execute("select scientificname from species")
                            speciesNames = cursor.fetchall()
                            message = '(0) cancel\n'
                            i = 1
                            for x in speciesNames:
                                message += '(' + str(i) + ') ' + x[0] + '\n'
                                i +=1
                            message += '>'
                            ans2 = helpfuncs.RepeatAskInt(message, 0, i)
                            if ans2 != 0:
                                data = speciesNames[ans2 - 1][0]
                                break
                        elif ans2 == 3:
                            data = AddSpecies(cursor)
                            break
                elif ans == 10:
                    print('Description:')
                    data = helpfuncs.MultiRowTextInput()
                else:
                    print(field[ans - 1].capitalize(),':')
                    data = input('>')
                
                data = helpfuncs.StringNoneCheck(data)
                if ans <= 4:
                    cursor.execute("UPDATE characters SET " + field[ans - 1] + " = %s WHERE characterid = %s", (data, id))
                else:
                    cursor.execute("UPDATE significantcharacters SET " + field[ans - 1] + " = %s WHERE characterid = %s", (data, id))
            except:
                traceback.print_exc()
    else:
        print('character of id:', id, ' does not exist')
        
def CompleteCharacter(cursor, id):
    cursor.execute("select characterExists(%s)", (id,))
    if cursor.fetchone()[0]:
        field = ['species', 'sex', 'height', 'weight', 'firstname', 'familyname', 'alias', 'age', 'occupation', 'characterdescription']
        cursor.execute("select species, sex, height, weight from characters where characterid = %s", (id,))
        basicFields = cursor.fetchone()

        cursor.execute("select firstname, familyname, alias, age, occupation, characterdescription from significantcharacters where characterid = %s", (id,))
        extendedFields = cursor.fetchone()

        print('Current info of id: ', id)
        print('Species: ', basicFields[0], '\nSex: ', basicFields[1], '\nHeight: ', basicFields[2], '\nWeight: ', basicFields[3])
        if  extendedFields != None:
            print('First name: ', extendedFields[0], '\nFamily Name: ', extendedFields[1], '\nAlias: ', extendedFields[2], '\nAge: ', extendedFields[3], '\nOccupation: ', extendedFields[4], '\nDescription:\n', extendedFields[5])

        emptyFields = []
        i = 1
        for x in basicFields:
            if x == None:
                emptyFields.append(i)
            i += 1
        for x in extendedFields:
            if x == None:
                emptyFields.append(i)
            i += 1

        for emptyField in emptyFields:
            try:
                data = None
                if emptyField == 1:
                    while True:
                        ans2 = helpfuncs.RepeatAskInt('Species:\n(1) None \n(2) Add existing \n(3) Add new \n>', 1, 3)
                        if ans2 == 1:
                            break
                        elif ans2 == 2:
                            cursor.execute("select scientificname from species")
                            speciesNames = cursor.fetchall()
                            message = '(0) cancel\n'
                            i = 1
                            for x in speciesNames:
                                message += '(' + str(i) + ') ' + x[0] + '\n'
                                i +=1
                            message += '>'
                            ans2 = helpfuncs.RepeatAskInt(message, 0, i)
                            if ans2 != 0:
                                data = speciesNames[ans2 - 1][0]
                                break
                        elif ans2 == 3:
                            data = AddSpecies(cursor)
                            break
                elif emptyField == 10:
                    print('Description:')
                    data = helpfuncs.MultiRowTextInput()
                else:
                    print(field[emptyField - 1].capitalize(),':')
                    data = input('>')
                
                data = helpfuncs.StringNoneCheck(data)
                if emptyField <= 4:
                    cursor.execute("UPDATE characters SET " + field[emptyField - 1] + " = %s WHERE characterid = %s", (data, id))
                else:
                    cursor.execute("UPDATE significantcharacters SET " + field[emptyField - 1] + " = %s WHERE characterid = %s", (data, id))
            except:
                traceback.print_exc()

    else:
        print('character of id:', id, ' does not exist')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Allows you to alter the data of both basic and significant characters."
    )
    parser.add_argument('-empty', help= 'Will present all empty fields for completion', action='store_true')
    parser.add_argument('id', help= 'must be the id of an already existing basic character that is not a significant character yet', type= int)

    args = parser.parse_args()

    mycursor = mydb.cursor()

    if args.empty:
        CompleteCharacter(mycursor, args.id)
    else:
        AlterCharacter(mycursor, args.id)

    mydb.commit()