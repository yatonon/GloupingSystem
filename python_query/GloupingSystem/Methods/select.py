# -*- coding: utf-8 -*-
import copy

import GenomClass.GeneticAlgorithm as ga

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
