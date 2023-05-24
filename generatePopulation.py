import argparse
from dbAccess import mydb
import random
from datetime import datetime
from addBasicCharacter import AddBasicCharacter

random.seed(datetime.now().timestamp())

parser = argparse.ArgumentParser(
    description = "Generate and add basic characters"
)
parser.add_argument('count', help= 'Number of generated characters', type= int)

args = parser.parse_args()

mycursor = mydb.cursor()

mycursor.execute("select scientificname from species")
speciesNames = mycursor.fetchall()

for i in range(args.count):
    species = speciesNames[random.randint(0,len(speciesNames) - 1)][0]
    height = random.normalvariate(1.5, 0.3)
    weight = random.normalvariate(70, 30)
    sex = random.choice(['Male', 'Female'])
    AddBasicCharacter(mycursor, species, sex, height, weight)

print('Characters added!')
mydb.commit()