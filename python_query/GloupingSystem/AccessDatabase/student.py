# pip install neo4j
from neo4j import GraphDatabase, basic_auth

def get_student():
    AllRecord = []

    driver = GraphDatabase.driver("bolt://neo4j", auth=basic_auth("neo4j", "neo4jpw"))
    session = driver.session()

    result = session.run("MATCH (student:Student20_problem_solving) RETURN student")

    for record in result:
        AllRecord.append(record.data()["student"])

    ScoreRecord = {}

    for record in AllRecord:
        add_list = [
            record["A"],
            record["B"],
            record["C"],
            record["D"],
            record["E"],
            record["F"],
            record["G"],
            ]
        ScoreRecord[record["name"]] = add_list

    session.close()

    return ScoreRecord
