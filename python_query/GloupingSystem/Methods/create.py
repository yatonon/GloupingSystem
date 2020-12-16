# -*- coding: utf-8 -*-
import random
import copy

import GenomClass.GeneticAlgorithm as ga

def create_genom(student_name_list, team_people, all_students_len):
    # ゲノムの作成
    random_play_time = int(all_students_len/team_people)
    genome_list = [[] for i in range(random_play_time)]
    pop_list = copy.copy(student_name_list)
    for team_numver in range(random_play_time):
        for j in range(team_people):
            genome_list[team_numver].append(pop_list.pop(random.randrange(len(pop_list))))
    return ga.genom(genome_list, 0)
