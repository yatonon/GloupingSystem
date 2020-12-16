# -*- coding: utf-8 -*-
import random
import GenomClass.GeneticAlgorithm as ga

def mutation(ga, genom_mutation, team_people, all_students_len):
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

            random_play_time = int(all_students_len/team_people)
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
