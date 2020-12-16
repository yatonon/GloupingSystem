# pip install neo4j
from neo4j import GraphDatabase, basic_auth
import inspect
import random

AllRecord = []

driver = GraphDatabase.driver("bolt://neo4j", auth=basic_auth("neo4j", "neo4jpw"))
session = driver.session()

result = session.run("MATCH (student:Student20_problem_solving) RETURN student")

for record in result:
    AllRecord.append(record.data()["student"])

print(AllRecord)

session.close()
