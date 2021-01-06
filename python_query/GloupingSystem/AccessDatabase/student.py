# pip install neo4j
from neo4j import GraphDatabase, basic_auth

class GetStudentData:

    def __init__(self):
        # インストラクタ
        driver = GraphDatabase.driver("bolt://neo4j", auth=basic_auth("neo4j", "neo4jpw"))
        self.session = driver.session()

    def get_student(self):
        ScoreRecord = {}
        result = self.session.run("MATCH (student:Student60) RETURN student")
        for record in result:
            add_list = [
                record.data()["student"]["A"],
                record.data()["student"]["B"],
                record.data()["student"]["C"],
                record.data()["student"]["D"],
                record.data()["student"]["E"],
                record.data()["student"]["F"],
                record.data()["student"]["G"],
                ]
            ScoreRecord[record.data()["student"]["name"]] = {"node_id": record.values()[0].id,"property": add_list}

        return ScoreRecord

    def get_student_node(self):
        NodeRecord = []
        result = self.session.run("MATCH ()-[node:THINKED]->() RETURN node")
        for record in result:
            relationship = {}
            for r in record.values()[0].values():
                relationship = {"role": r}
            NodeRecord.append([record.values()[0].start_node.id, relationship["role"], record.values()[0].end_node.id])

        return NodeRecord

    def __del__(self):
        # デスストラクタ
        self.session.close()
