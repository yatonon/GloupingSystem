# pip install neo4j
from neo4j import GraphDatabase, basic_auth
import inspect
import random

AllRecord = []

driver = GraphDatabase.driver("bolt://neo4j", auth=basic_auth("neo4j", "aaaaaaaa"))
# driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo4j"))
session = driver.session()

result = session.run("MATCH (student:Student) RETURN student")

for record in result:
    AllRecord.append(record.data()["student"])

# for x in inspect.getmembers(AllRecord[0], inspect.ismethod):
#   print(x[0])

TeamPeople = 3
RandomPlayTime = int(len(AllRecord)/TeamPeople)

result = {}

for teamNumber in range(RandomPlayTime):
    teamName = "team" + str(teamNumber + 1)
    result[teamName] = []
    for i in range(TeamPeople):
        result[teamName].append(AllRecord.pop(random.randrange(len(AllRecord))))

print("team1"+"\n")
print(result["team1"])
print("team2"+"\n")
print(result["team2"])
print("team3"+"\n")
print(result["team3"])

session.close()
