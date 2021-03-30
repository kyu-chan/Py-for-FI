import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from math import log, sqrt, exp
from scipy import stats
from time import time
from random import gauss, seed
import math



class mcs_est:

    def mcs_pure(self,S0,K,r,sigma,M,T,I,seed_num):
        seed(seed_num)
        t0 = time()
        # M은 시간 구간 개수
        dt = T / M

        S = []
        for i in range(I):
            path = []
            for t in range( M + 1 ):
                if t == 0:
                    path.append(S0)
                else:
                    z = gauss(0.0, 1.0)
                    St = path[t-1] * exp( ( r - 0.5 * sigma ** 2) * dt
                                          + sigma * sqrt(dt) * z)
                    path.append(St)
            S.append(path)
        ### 가격 추정
        C0 = exp( -r * T) * sum( [max(path[-1] - K, 0) for path in S]) / I

        tpy = time() - t0
        print("European Option Value %7.3f" % C0)
        print("Duration in Seconds %7.3f" % tpy)


    def mcs_vector_np(self,S0,K,r,sigma,M,T,I,seed_num):
        np.random.seed(seed_num)
        t0 = time()
        # M은 시간 구간 개수
        dt = T / M

        self.S = np.zeros((M+1, I))
        self.S[0] = S0
        for t in range(1, M+1):  ### 1부터 M까지
            z = np.random.standard_normal(I) ## pseudorandom numbers
            self.S[t] = self.S[t-1] * np.exp( ( r - 0.5 * sigma ** 2) * dt
                                    + sigma * math.sqrt(dt) * z) ## 같은 시간 구간에 벡터 연산 적용
        C0 = math.exp(-r * T) * np.sum(np.maximum(self.S[-1] - K, 0)) / I

        tnp = time() - t0
        print("European Option Value %7.3f" % C0)
        print("Duration in Seconds %7.3f" % tnp)
        return self.S
