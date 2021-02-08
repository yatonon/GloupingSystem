# -*- coding: utf-8 -*-
import random
import copy
import datetime

import numpy as np
import matplotlib.pyplot as plt

import AccessDatabase.student as ADstudent
from Methods.create import create_genom
from Methods.select import select, next_generation_gene_create
from Methods.mutation import mutation
from Methods.evaluation.problem_solving import evaluation as evaluation_problem_solving
from Methods.evaluation.debate import evaluation as evaluation_debate

# グループの人数 2人以上
# dabate の場合は片方の人数となる
TEAM_PEOPLE = 5
# 遺伝子集団の大きさ
MAX_GENOM_LIST = 100
# 遺伝子選択数
SELECT_GENOM = 30
# 遺伝子突然変異確率
GENOM_MUTATION = 0.1
# 繰り返す世代数
MAX_GENERATION = 100
# 型の選択, 課題解決型なら 1,  ディベートなら 2, ディスカッションなら 3
EVALUATION_TYPE = 2
# pdf でデータのプロットをするか
PDF_PLOT = False

GetStudentDataInstance = ADstudent.GetStudentData()
all_students = GetStudentDataInstance.get_student()
all_student_nodes = GetStudentDataInstance.get_student_node()

if __name__ == '__main__':

    # 一番最初の現行世代個体集団を生成します。
    current_generation_individual_group = []
    for i in range(MAX_GENOM_LIST):
        # 初期ゲノムの作成
        current_generation_individual_group.append(create_genom(all_students, TEAM_PEOPLE))

    graph_left_list = []
    graph_height_min_list = []
    graph_height_max_list = []
    graph_height_avg_list = []
    for count_ in range(1, MAX_GENERATION + 1):
        graph_left_list.append(count_)
        # 現行世代個体集団の遺伝子を評価し、genomClassに代入します
        for i in range(MAX_GENOM_LIST):
            if EVALUATION_TYPE == 1:
                evaluation_result = evaluation_problem_solving(current_generation_individual_group[i], all_students, all_student_nodes, MAX_GENERATION==count_, MAX_GENOM_LIST==i+1)
            elif EVALUATION_TYPE == 2:
                evaluation_result = evaluation_debate(current_generation_individual_group[i], all_students, all_student_nodes, MAX_GENERATION==count_, MAX_GENOM_LIST==i+1)

            current_generation_individual_group[i].setEvaluation(evaluation_result)
        # エリート個体を選択します
        elite_genes = select(current_generation_individual_group, SELECT_GENOM)
        # 次世代個体集団を現行世代、エリート集団から作成します
        next_generation_individual_group = next_generation_gene_create(current_generation_individual_group, elite_genes)
        # 1世代の進化的計算終了。評価に移ります

        # 各個体適用度を配列化します。
        fits = [i.getEvaluation() for i in current_generation_individual_group]

        # 進化結果を評価します
        min_ = round(min(fits), 2)
        max_ = round(max(fits), 2)
        avg_ = round(sum(fits) / len(fits), 2)

        graph_height_min_list.append(min_)
        graph_height_max_list.append(max_)
        graph_height_avg_list.append(avg_)

        # 現行世代の進化結果を出力します
        print("-----第{}世代の結果-----".format(count_))
        print("  Min:{}".format(min_))
        print("  Max:{}".format(max_))
        print("  Avg:{}".format(avg_))

        # 次世代個体集団全ての個体に突然変異を施します。
        next_generation_individual_group = mutation(next_generation_individual_group, GENOM_MUTATION, TEAM_PEOPLE, len(all_students))
        # 現行世代と次世代を入れ替えます
        current_generation_individual_group = next_generation_individual_group

    if PDF_PLOT:
        # plot の pdf 化
        graph_left = np.array(graph_left_list)
        graph_height_min = np.array(graph_height_min_list)
        graph_height_max = np.array(graph_height_max_list)
        graph_height_avg = np.array(graph_height_avg_list)

        plt.title("GA max, min, avg plot")
        plt.xlabel("count")
        plt.ylabel("score")
        plt.grid(True)

        plt.plot(graph_left, graph_height_min)
        plt.plot(graph_left, graph_height_avg, color="yellow")
        plt.plot(graph_left, graph_height_max, color="red")
        DIFF_JST_FROM_UTC = 9
        dt_now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
        plt.savefig("../plot_data/" + str(EVALUATION_TYPE) + "_" + dt_now.strftime('%Y-%m-%d_%H:%M:%S') + ".pdf")

    # 最終結果出力
    print("最も優れた個体は{}".format(elite_genes[0].getGenom()))
    print("評価は{}".format(round(elite_genes[0].getEvaluation(), 2)))
