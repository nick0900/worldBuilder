import argparse
import helpfuncs
from dbAccess import mydb

parser = argparse.ArgumentParser(
    description = "Displays some analysis of population"
)

args = parser.parse_args()

mycursor = mydb.cursor()

print('//-----------------------------Population Info--------------------------------//')

mycursor.execute("select s.scientificname, count(c.species) as speciesCount, avg(c.height) as avgSpeciesHeight, avg(c.weight) as avgSpeciesWeight, s.speciesdescription from species s left join characters c on s.scientificname = c.species group by s.scientificname order by count(c.species) desc")
x = mycursor.fetchall()
message = ''
for i, entry in enumerate(x):
    print('--//' + str(entry[0]) + '// Population: ' + str(entry[1]) + ', average height: ' + str(round(entry[2], 2)) + 'm, average weight: ' + str(round(entry[3], 2)) + 'kg//-- (' + str(i + 1) + ') for description')

print('//----------------------------------------------------------------------------//')

while True:
    ans = helpfuncs.RepeatAskInt('View species description, (0) to exit>', 0, len(x))
    if ans == 0: break
    print('--//' + x[ans - 1][0] + '//--')
    print(x[ans - 1][4] + '--//-----//--')

mydb.commit()