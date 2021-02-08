# -*- coding: utf-8 -*-
import copy
import csv

def evaluation(ga, all_students, all_student_nodes, genaration_last, list_last):
    # ゲノムの評価
    score = 0
    genom_list = ga.getGenom()
    genom_list_pop = list(map(copy.copy, genom_list))

    genom_list_data = []
    genom_list_node_ids = []
    def get_student_node_data(student_name):
        return all_students[student_name]
    for genom in genom_list:
        genom_list_data.append(list(map(get_student_node_data, genom)))
    for group_list in genom_list_data:
        node_list = []
        for node in group_list:
            node_list.append(node["node_id"])
        genom_list_node_ids.append(node_list)

    difference = 0
    for i in range(len(genom_list_pop)):
        total_0=0
        total_1=0
        if (i%2)==0:
            for j in range(len(genom_list_pop[i])):
                total_0 += sum(all_students[genom_list_pop[i][j]]["property"])
        elif (i%2)==1:
            for j in range(len(genom_list_pop[i])):
                total_1 += all_students[genom_list_pop[i][j]]["property"][0]
        difference += abs(total_0 - total_1)

    score = 10000 - difference/10

    # リレーションペナルティ
    for node_id_list in genom_list_node_ids:
        for relation_node in all_student_nodes:
            if all(map(node_id_list.__contains__, (relation_node[0], relation_node[2]))):
                if relation_node == "like":
                    score += 50
                elif relation_node == "respect":
                    score += 100
                elif relation_node == "hate":
                    score -= 500

    return score
