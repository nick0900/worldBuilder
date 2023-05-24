import argparse
import helpfuncs
from dbAccess import mydb
import traceback

def AlterSpecies(cursor):
        while True:
            try:
                cursor.execute("select scientificname from species")
                speciesNames = cursor.fetchall()
                message = 'Choose species to alter:\n(0) Done\n'
                i = 1
                for x in speciesNames:
                    message += '(' + str(i) + ') ' + x[0] + '\n'
                    i +=1
                message += '>'
                ans = helpfuncs.RepeatAskInt(message, 0, i)
                if ans != 0:
                    while True:
                        cursor.execute("select scientificname, speciesdescription from species where scientificname = %s", (speciesNames[ans - 1][0],))
                        entry = cursor.fetchone()
                        print('Current info of ', entry[0], ':\n')
                        print(entry[1])
                        ans2 = helpfuncs.RepeatAskInt('Choose what to alter:\n(0) Done\n(1) Scientific Name\n(2) Description\n>', 0, 2)
                        if ans2 == 0:
                            break
                        elif ans2 == 1:
                            print('Scientific Name:')
                            newName = helpfuncs.StringNoneCheck(input('>'))
                            if newName != None:
                                cursor.execute("UPDATE species SET scientificname = %s WHERE scientificname = %s", (newName, entry[0]))
                                speciesNames[ans - 1] = (newName,)
                        else:
                            print('Species Description:')
                            cursor.execute("UPDATE species SET speciesdescription = %s WHERE scientificname = %s", (helpfuncs.StringNoneCheck(helpfuncs.MultiRowTextInput()), entry[0]))
                else:
                    break
            except:
                traceback.print_exc()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Allows you to alter the name and description of species."
    )
    args = parser.parse_args()

    mycursor = mydb.cursor()

    AlterSpecies(mycursor)

    mydb.commit()