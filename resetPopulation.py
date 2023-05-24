import argparse
from dbAccess import mydb

def ResetPopulation(cursor):
    cursor.execute("select count(characterid) from characters where not isSignificant(characterid)")
    print(str(cursor.fetchone()[0]), ' basic characters will be removed, do you confirm this?')
    if input('(yes/no):>') == 'yes':
        cursor.execute("call ResetPopulation()")
        print('Population was reset')
    else:
        print('Canceled!')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Deletes all basic character enters"
    )

    args = parser.parse_args()

    mycursor = mydb.cursor()

    ResetPopulation(mycursor)

    mydb.commit()