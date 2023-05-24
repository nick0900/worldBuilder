import argparse
from dbAccess import mydb

parser = argparse.ArgumentParser(
    description = "Displays some analysis of population"
)

args = parser.parse_args()

mycursor = mydb.cursor()

mycursor.execute("select count(characterid) as popcount from characters")
print('//-----------------------------Population Info--------------------------------//')
print('Total registered population: ' + str(mycursor.fetchone()[0]) + '.')

mycursor.execute("select count(characterid) as popcount from significantcharacters")
print('Significant character entries: ' + str(mycursor.fetchone()[0]) + '.\n')

mycursor.execute("select sex, count(characterid) as popcount from characters group by sex order by count(characterid) desc")
x = mycursor.fetchall()
print("--//Population grouped by sex//--")
message = ''
for entry in x:
    if message != '':
        message += ', '
    message += str(entry[0]) + ': ' + str(entry[1])
print(message + '.\n')

mycursor.execute("select species, count(characterid) as popcount from characters group by species order by count(characterid) desc")
x = mycursor.fetchall()
print("--//Population grouped by species//--")
message = ''
for entry in x:
    if message != '':
        message += ',\n'
    message += str(entry[0]) + ': ' + str(entry[1])
print(message + '.\n')

mycursor.execute("select avg(height) as avgforpop from characters")
print('Population average height: ' + str(mycursor.fetchone()[0]) + '.\n')

mycursor.execute("select avg(weight) as avgforpop from characters")
print('Population average weight: ' + str(mycursor.fetchone()[0]) + '.\n')

print('//----------------------------------------------------------------------------//')

mydb.commit()