# -*- coding: utf-8 -*-
import random
import copy

import GenomClass.GeneticAlgorithm as ga
from AccessDatabase.student import get_student
from Methods.create import create_genom
from Methods.select import select, next_generation_gene_create
from Methods.mutation import mutation
from Methods.evaluation.problem_solving import evaluation

# グループの人数 2人以上
TEAM_PEOPLE = 5
# 遺伝子集団の大きさ
MAX_GENOM_LIST = 100
# 遺伝子選択数
SELECT_GENOM = 30
# 遺伝子突然変異確率
GENOM_MUTATION = 0.1
# 繰り返す世代数
MAX_GENERATION = 10

all_students = get_student()

if __name__ == '__main__':

    # 一番最初の現行世代個体集団を生成します。
    current_generation_individual_group = []
    all_students_name_list = list(all_students.keys())
    for i in range(MAX_GENOM_LIST):
        # 初期ゲノムの作成
        current_generation_individual_group.append(create_genom(all_students_name_list, TEAM_PEOPLE, len(all_students)))

    for count_ in range(1, MAX_GENERATION + 1):
        # 現行世代個体集団の遺伝子を評価し、genomClassに代入します
        for i in range(MAX_GENOM_LIST):
            evaluation_result = evaluation(current_generation_individual_group[i], all_students)
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

        # 現行世代の進化結果を出力します
        print("-----第{}世代の結果-----".format(count_))
        print("  Min:{}".format(min_))
        print("  Max:{}".format(max_))
        print("  Avg:{}".format(avg_))

        # 次世代個体集団全ての個体に突然変異を施します。
        next_generation_individual_group = mutation(next_generation_individual_group, GENOM_MUTATION, TEAM_PEOPLE, len(all_students))
        # 現行世代と次世代を入れ替えます
        current_generation_individual_group = next_generation_individual_group

    # 最終結果出力
    print("最も優れた個体は{}".format(elite_genes[0].getGenom()))
    print("評価は{}".format(round(elite_genes[0].getEvaluation(), 2)))
