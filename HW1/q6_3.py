import q6_framework
from multiprocessing import Pool
import json


if __name__ == '__main__':
    res = [0] * q6_framework.c

    for i in range(q6_framework.c):
        for j in range(q6_framework.n0):
            tmp_res = q6_framework.find_first_appearance_generation(j)
    print(res)
    with open('res.dat', 'w') as fl:
        json.dump(res, fl)
