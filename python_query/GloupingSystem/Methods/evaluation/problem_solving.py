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

    # 超汚い、本来グループごとに算定していくべき
    print_A_dict = {}
    print_B_dict = {}
    print_C_dict = {}
    print_D_dict = {}
    print_E_dict = {}
    # A の選定
    for i in range(len(genom_list_pop)):
        A_list = []
        for j in range(len(genom_list_pop[i])):
            A_list.append(all_students[genom_list_pop[i][j]]["property"][0]*(1+all_students[genom_list_pop[i][j]]["property"][6]/100))
        score += round(max(A_list), 2)
        print_A_dict[i] = int(max(A_list))
        genom_list_pop[i].pop(A_list.index(max(A_list)))
    # B の選定
    for i in range(len(genom_list_pop)):
        B_list = []
        for j in range(len(genom_list_pop[i])):
            B_list.append(all_students[genom_list_pop[i][j]]["property"][1]*(1+all_students[genom_list_pop[i][j]]["property"][6]/100))
        score += round(max(B_list), 2)
        print_B_dict[i] = int(max(B_list))
        genom_list_pop[i].pop(B_list.index(max(B_list)))
    # C の選定
    for i in range(len(genom_list_pop)):
        C_list = []
        for j in range(len(genom_list_pop[i])):
            C_list.append(all_students[genom_list_pop[i][j]]["property"][2]*(1+all_students[genom_list_pop[i][j]]["property"][6]/100))
        score += round(max(C_list), 2)
        print_C_dict[i] = int(max(C_list))
        genom_list_pop[i].pop(C_list.index(max(C_list)))
    # D の選定
    for i in range(len(genom_list_pop)):
        D_list = []
        for j in range(len(genom_list_pop[i])):
            D_list.append(all_students[genom_list_pop[i][j]]["property"][3]*(1+all_students[genom_list_pop[i][j]]["property"][6]/100))
        score += round(max(D_list), 2)
        print_D_dict[i] = int(max(D_list))
        genom_list_pop[i].pop(D_list.index(max(D_list)))
    # E の選定
    for i in range(len(genom_list_pop)):
        E_list = []
        for j in range(len(genom_list_pop[i])):
            E_list.append(all_students[genom_list_pop[i][j]]["property"][4]*(1+all_students[genom_list_pop[i][j]]["property"][6]/100))
        score += round(max(E_list), 2)
        print_E_dict[i] = int(max(E_list))
        genom_list_pop[i].pop(E_list.index(max(E_list)))

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

    if genaration_last & list_last:
        print_list = []
        # 12なのは、12グループあるから。修正を加えたほうがいい
        for i in range(12):
            print_list.append([
                print_A_dict[i],
                print_B_dict[i],
                print_C_dict[i],
                print_D_dict[i],
                print_E_dict[i]
            ])
        with open('student_score.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            for group in print_list:
                writer.writerow(group)

    return score
