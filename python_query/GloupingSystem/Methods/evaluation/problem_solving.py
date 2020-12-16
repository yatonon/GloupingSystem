# -*- coding: utf-8 -*-
import copy

import GenomClass.GeneticAlgorithm as ga

def evaluation(ga, all_students):
    # ゲノムの評価
    score = 0
    genom_list = ga.getGenom()
    genom_list_pop = list(map(copy.copy, genom_list))

    # A の選定
    for i in range(len(genom_list_pop)):
        A_list = []
        for j in range(len(genom_list_pop[i])):
            A_list.append(all_students[genom_list_pop[i][j]][0]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += round(max(A_list), 2)
        genom_list_pop[i].pop(A_list.index(max(A_list)))
    # B の選定
    for i in range(len(genom_list_pop)):
        B_list = []
        for j in range(len(genom_list_pop[i])):
            B_list.append(all_students[genom_list_pop[i][j]][1]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += round(max(B_list), 2)
        genom_list_pop[i].pop(B_list.index(max(B_list)))
    if genom_list_pop[i] == []:
        return score
    # C の選定
    for i in range(len(genom_list_pop)):
        C_list = []
        for j in range(len(genom_list_pop[i])):
            C_list.append(all_students[genom_list_pop[i][j]][1]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += round(max(C_list), 2)
        genom_list_pop[i].pop(C_list.index(max(C_list)))
    if genom_list_pop[i] == []:
        return score
    # D の選定
    for i in range(len(genom_list_pop)):
        D_list = []
        for j in range(len(genom_list_pop[i])):
            D_list.append(all_students[genom_list_pop[i][j]][1]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += round(max(D_list), 2)
        genom_list_pop[i].pop(D_list.index(max(D_list)))
    if genom_list_pop[i] == []:
        return score
    # E の選定
    for i in range(len(genom_list_pop)):
        E_list = []
        for j in range(len(genom_list_pop[i])):
            E_list.append(all_students[genom_list_pop[i][j]][1]*(1+all_students[genom_list_pop[i][j]][6]/100))
        score += round(max(E_list), 2)
        genom_list_pop[i].pop(E_list.index(max(E_list)))
    if genom_list_pop[i] == []:
        return score

    return score
