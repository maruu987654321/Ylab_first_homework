from itertools import permutations
import itertools

start = (0, 2)
point_2 = (2, 5)
point_3 = (5, 2)
point_4 = (6, 6)
point_5 = (8, 3)

list1 = [point_2, point_3, point_4, point_5]
all_coord = []
new_res = []
result_dict = {}

def SplitList(mylist, chunk_size):
    return [mylist[offs:offs+chunk_size] for offs in range(0, len(mylist), chunk_size)]

def get_result(lst_coord):
    res = 0
    all_coord_ = []
    lst_for_coord = []
    inter_res = []
    lst_value = []
    for indx_ in range(0, len(lst_coord) - 1):
        first_coor = lst_coord[indx_]
        second_coord = lst_coord[indx_+1]
        lst_for_coord.append(first_coor)
        lst_for_coord.append(second_coord)
        res += ((second_coord[0] - first_coor[0]) ** 2 + (second_coord[1] - first_coor[1]) ** 2) ** 0.5
        inter_res.append(res)
    lst_value.append(lst_for_coord)
    lst_value.append(inter_res)
    result_dict[res] = lst_value
    return result_dict


def create_result():
    for i in list(itertools.permutations(list1, len(list1))):
        new_res.append((start,) + i + (start,))

    for item in new_res:
        new_item = list(item)
        result_dict = get_result(new_item)
    
    minval = min(result_dict.keys())
    for elem, elem2 in  zip(SplitList(result_dict[minval][0], 2), result_dict[minval][1]):
        print(f'{elem[0]} -> {elem[1]}[{elem2}] ->', end=' ')
    print(f'= {minval}')

if __name__ == '__main__':
    create_result()