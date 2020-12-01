# -*- coding: utf-8 -*-

import GeneticAlgorithm as ga
import random
import copy

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

all_students = {
    "student1": [53, 63, 65, 63, 94, 42, 58],
    "student2": [13, 53, 69, 24, 42, 19, 48],
    "student3": [40, 7, 10, 82, 64, 86, 2],
    "student4": [51, 19, 36, 75, 92, 92, 14],
    "student5": [73, 82, 22, 29, 72, 74, 77],
    "student6": [73, 82, 22, 29, 72, 74, 77],
    "student7": [43, 23, 76, 98, 44, 21, 78],
    "student8": [65, 22, 14, 35, 63, 43, 48],
    "student9": [40, 7, 10, 82, 64, 25, 21],
    "student10": [51, 19, 36, 75, 92, 92, 53],
    "student11": [73, 78, 54, 24, 72, 35, 45],
    "student12": [55, 25, 22, 78, 63, 40, 64],
    "student13": [36, 64, 63, 63, 24, 60, 24],
    "student14": [63, 26, 88, 26, 34, 64, 22],
    "student15": [58, 34, 11, 44, 72, 23, 74],
    "student16": [85, 25, 56, 33, 6, 5, 45],
    "student17": [53, 86, 86, 77, 64, 2, 88],
    "student18": [24, 27, 35, 46, 2, 45, 95],
    "student19": [34, 35, 97, 58, 35, 45, 59],
    "student20": [86, 76, 24, 98, 75, 63, 85],
}


def create_genom(student_name_list, team_people):
    # ゲノムの作成
    random_play_time = int(len(all_students)/team_people)
    genome_list = [[] for i in range(random_play_time)]
    pop_list = copy.copy(student_name_list)
    for team_numver in range(random_play_time):
        for j in range(team_people):
            genome_list[team_numver].append(pop_list.pop(random.randrange(len(pop_list))))
    return ga.genom(genome_list, 0)

def evaluation(ga):
    # ゲノムの評価
    score = 0
    genom_list = ga.getGenom()
    genom_list_pop = list(map(copy.copy, genom_list))

    # A の選定
    for i in range(len(genom_list_pop)):
        A_list = []
        for j in range(len(genom_list_pop[i])):
            A_list.append(all_students[genom_list_pop[i][j]][0]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += max(A_list)
        genom_list_pop[i].pop(A_list.index(max(A_list)))
    # B の選定
    for i in range(len(genom_list_pop)):
        B_list = []
        for j in range(len(genom_list_pop[i])):
            B_list.append(all_students[genom_list_pop[i][j]][1]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += max(B_list)
        genom_list_pop[i].pop(B_list.index(max(B_list)))
    if genom_list_pop[i] == []:
        return score
    # C の選定
    for i in range(len(genom_list_pop)):
        C_list = []
        for j in range(len(genom_list_pop[i])):
            C_list.append(all_students[genom_list_pop[i][j]][1]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += max(C_list)
        genom_list_pop[i].pop(C_list.index(max(C_list)))
    if genom_list_pop[i] == []:
        return score
    # D の選定
    for i in range(len(genom_list_pop)):
        D_list = []
        for j in range(len(genom_list_pop[i])):
            D_list.append(all_students[genom_list_pop[i][j]][1]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += max(D_list)
        genom_list_pop[i].pop(D_list.index(max(D_list)))
    if genom_list_pop[i] == []:
        return score
    # E の選定
    for i in range(len(genom_list_pop)):
        E_list = []
        for j in range(len(genom_list_pop[i])):
            E_list.append(all_students[genom_list_pop[i][j]][1]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += max(E_list)
        genom_list_pop[i].pop(E_list.index(max(E_list)))
    if genom_list_pop[i] == []:
        return score

    return score

def select(ga, elite):
    # 現行世代個体集団の評価を高い順番にソートする
    sort_result = sorted(ga, reverse=True, key=lambda u: u.evaluation)
    # インスタンスの再生成
    new_instance_result = list(map(copy.copy, sort_result))
    # 一定の上位を抽出する
    result = [new_instance_result.pop(0) for i in range(elite)]
    return result

def next_generation_gene_create(ga, ga_elite):
    # 現行世代個体集団の評価を低い順番にソートする
    next_generation_geno = sorted(ga, reverse=False, key=lambda u: u.evaluation)
    # 追加するエリート集団ぶんを取り除く
    for i in range(0, len(ga_elite)):
        next_generation_geno.pop(0)
    # エリート集団を次世代集団を次世代へ追加します
    next_generation_geno.extend(ga_elite)
    return next_generation_geno


def mutation(ga, genom_mutation, team_people):
    ga_list = []
    for i in ga:
        # 個体に対して一定の確率で突然変異が起きる
        if genom_mutation > (random.randint(0, 100) / 100):
            genom_list = []
            current_genom = i.getGenom()
            for i_ in range(len(current_genom)):
                genom_list.extend(current_genom[i_])
            rand1 = random.randint(0, len(genom_list)-1)
            rand2 = random.randint(0, len(genom_list)-1)
            genom_list[rand1], genom_list[rand2] = genom_list[rand2], genom_list[rand1]
            # 突然変異がおこる

            random_play_time = int(len(all_students)/team_people)
            return_list = [[] for i__ in range(random_play_time)]
            for team_numver in range(random_play_time):
                for j in range(team_people):
                    return_list[team_numver].append(genom_list.pop(0))
            i.setGenom(return_list)
            # return_list に形式を合わせて格納
            ga_list.append(i)
        else:
            ga_list.append(i)
    return ga_list


if __name__ == '__main__':

    # 一番最初の現行世代個体集団を生成します。
    current_generation_individual_group = []
    all_students_name_list = list(all_students.keys())
    for i in range(MAX_GENOM_LIST):
        # 初期ゲノムの作成
        current_generation_individual_group.append(create_genom(all_students_name_list, TEAM_PEOPLE))

    for count_ in range(1, MAX_GENERATION + 1):
        # 現行世代個体集団の遺伝子を評価し、genomClassに代入します
        for i in range(MAX_GENOM_LIST):
            evaluation_result = evaluation(current_generation_individual_group[i])
            current_generation_individual_group[i].setEvaluation(evaluation_result)
        # エリート個体を選択します
        elite_genes = select(current_generation_individual_group, SELECT_GENOM)
        # 次世代個体集団を現行世代、エリート集団から作成します
        next_generation_individual_group = next_generation_gene_create(current_generation_individual_group, elite_genes)
        # 1世代の進化的計算終了。評価に移ります

        # 各個体適用度を配列化します。
        fits = [i.getEvaluation() for i in current_generation_individual_group]

        # 進化結果を評価します
        min_ = min(fits)
        max_ = max(fits)
        avg_ = sum(fits) / len(fits)

        # 現行世代の進化結果を出力します
        print("-----第{}世代の結果-----".format(count_))
        print("  Min:{}".format(min_))
        print("  Max:{}".format(max_))
        print("  Avg:{}".format(avg_))

        # 次世代個体集団全ての個体に突然変異を施します。
        next_generation_individual_group = mutation(next_generation_individual_group, GENOM_MUTATION, TEAM_PEOPLE)
        # 現行世代と次世代を入れ替えます
        current_generation_individual_group = next_generation_individual_group

    # 最終結果出力
    print("最も優れた個体は{}".format(elite_genes[0].getGenom()))
    print("評価は{}".format(elite_genes[0].getEvaluation()))
