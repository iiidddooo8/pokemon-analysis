import csv
from pathlib import Path 
import matplotlib.pyplot as plt
import numpy as np

CSV_PATH = Path('dataset/pokemon_status.csv')

# csv読み込み
def input_csv():
    with open(CSV_PATH) as f:
        reader = csv.reader(f)
        csv_list = [row for row in reader]
    csv_list.pop(0)
    return csv_list

# 最大、最小抽出
def max_min(p_list):
    max_list = [0]
    min_list = [999999]
    max_name_list = []
    min_name_list = []
    for zukan in p_list:
        #図鑑番号が5文字 かつ 名前の頭に「メガ」がつくポケモンは対象外
        if not len(zukan[0]) == 5 and not zukan[1][:2] == "メガ":
            if not zukan[13] == '':
                num = int(zukan[13])
            if max_list[0] < num:
                max_list = [num]
                max_name_list = [zukan[1]]
            elif min_list[0] > num:
                min_list = [num]
                min_name_list = [zukan[1]]
            elif max_list[0] == num:
                max_list.append(num)
                max_name_list.append(zukan[1])
            elif min_list[0] == num:
                min_list.append(num)
                min_name_list.append(zukan[1])
    
    print("合計値最大ポケモン")
    output_name(max_name_list)
    print("合計値最小ポケモン")
    output_name(min_name_list)
    
# ポケモン名出力
def output_name(name_list):
    for name in name_list:
        print(name)

# グラフ作成
def create_graph(p_list_):
    # 0:ノーマル, 1:ほのお, 2:みず, 3:でんき, 4:くさ, 5:こおり,
    # 6:かくとう, 7:どく, 8:じめん 9:ひこう, 10:エスパー, 11: むし,
    # 12:いわ, 13:ゴースト, 14:ドラゴン, 15:あく, 16:はがね 17:フェアリー
    type_count_list = [0]*18
    for zukan_ in p_list_:
        if not len(zukan_[0]) == 5 and not zukan_[1][:2] == "メガ":
            type_in_list = [zukan_[2], zukan_[3]]
            type_count_list = count_type(type_in_list, type_count_list)
    
    # グラフパラメータ設定
    left = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    height = np.array([type_count_list[0], type_count_list[1], type_count_list[2], type_count_list[3],
                        type_count_list[4], type_count_list[5], type_count_list[6], type_count_list[7],
                        type_count_list[8], type_count_list[9], type_count_list[10], type_count_list[11],
                        type_count_list[12], type_count_list[13], type_count_list[14], type_count_list[15],
                        type_count_list[16], type_count_list[17]])
    labels = ["Nomal", "Fire", "Water", "Electrical", "Grass", "Ice", "Fighting", "Poison", "Ground",
                "Flight", "Psychic", "Bug", "Rock", "Ghost", "Dagon", "Dark", "Steel", "Fairy"]
    plt.bar(left, height, tick_label=labels)
    plt.xticks(rotation=90)
    plt.title('Pokemon type count')
    plt.xlabel('Type')
    plt.ylabel('Quantity')
    plt.show()

# タイプ種別事ごとカウント
def count_type(type_list,count_list):
    for type_ in type_list:
        if type_ == "":
            if type_ == type_list[1]:
                break
        elif type_ == "ノーマル":
            count_list[0] += 1
        elif type_ == "ほのお":
            count_list[1] += 1
        elif type_ == "みず":
            count_list[2] += 1
        elif type_ == "でんき":
            count_list[3] += 1
        elif type_ == "くさ":
            count_list[4] += 1
        elif type_ == "こおり":
            count_list[5] += 1
        elif type_ == "かくとう":
            count_list[6] += 1
        elif type_ == "どく":
            count_list[7] += 1
        elif type_ == "じめん":
            count_list[8] += 1
        elif type_ == "ひこう":
            count_list[9] += 1
        elif type_ == "エスパー":
            count_list[10] += 1
        elif type_ == "むし":
            count_list[11] += 1
        elif type_ == "いわ":
            count_list[12] += 1
        elif type_ == "ゴースト":
            count_list[13] += 1
        elif type_ == "ドラゴン":
            count_list[14] += 1
        elif type_ == "あく":
            count_list[15] += 1
        elif type_ == "はがね":
            count_list[16] += 1
        elif type_ == "フェアリー":
            count_list[17] += 1
    return count_list


if __name__ == '__main__':
    pokemon_list = input_csv()
    max_min(pokemon_list)
    create_graph(pokemon_list)