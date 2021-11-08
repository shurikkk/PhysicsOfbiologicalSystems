import q6_framework
from multiprocessing import Pool
import json


if __name__ == '__main__':
    res = [{} for ii in range(q6_framework.m)]
    for ii in range(q6_framework.m):
        for i in range(q6_framework.c):
            with Pool(8) as p:
                count = sum(p.map(q6_framework.simulate_single_branch, [j for j in range(q6_framework.n0)]))
                if count not in res[ii]:
                    res[ii][count] = 1
            print(ii, i, count)
    print(res)
    with open('res.dat', 'w') as fl:
        json.dump(res, fl)
