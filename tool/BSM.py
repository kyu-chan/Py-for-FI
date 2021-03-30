import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from math import log, sqrt, exp
from scipy import stats

class bsm_function:

    def bsm_call_value(self, S0, K, T, r, sigma):
        '''
        :param S0: float 초기 주가 or 지수
        :param K: float 행사가
        :param T: float 만기까지 남은 시간 (연 단위)
        :param r: float 고정 무위험 단기 이자율
        :param sigma: float 변동성 param
        :return: value : float 유러피안 콜 현재 가격, 물론 이론가
        '''
        S0 = float(S0)
        d1 = (log( S0 / K) + ( r + 0.5 * sigma ** 2 ) * T) / ( sigma * sqrt(T) )
        d2 = (log( S0 / K) + ( r - 0.5 * sigma ** 2 ) * T) / ( sigma * sqrt(T) )
        value = (S0 * stats.norm.cdf(d1, 0.0, 1.0)   ##정규분포 cdf
                 - K * exp(-r *T) * stats.norm.cdf(d2, 0.0, 1.0))
        return value

    def bsm_vega(self, S0, K, T, r, sigma):  ##vega 계산
        '''
        :param S0: float 초기 주가 or 지수
        :param K: float 행사가
        :param T: float 만기까지 남은 시간 (연 단위)
        :param r: float 고정 무위험 단기 이자율
        :param sigma: float 변동성 param
        :return: vega : float  BSM을 변동성에 대해 한번 미분한 값
        '''
        S0 = float(S0)
        d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
        vega = S0 * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)
        return vega

    def bsm_call_imp_vol(self, SO, K, T, r, C0, sigma_est, it = 100):  ###내재변동성 계산
        '''
        :param SO: float 초기 주가 or 지수
        :param K: float 행사가
        :param T: float 만기까지 남은 시간 ( 연 단위)
        :param r: float 고정 무위험 단기 이자율
        :param C0: option price
        :param sigma_est: float 변동성 파라미터 초기 추정치
        :param it: integer 반복 계산 횟수
        :return: sigma_est : 수치적으로 추정한 내재 변동성
        '''
        for i in range(it):
            sigma_est -= ((self.bsm_call_value(S0=SO,K=K,T=T,r=r,sigma=sigma_est) - C0)
                / self.bsm_vega(S0=SO,K=K,T=T,r=r,sigma=sigma_est))
        return sigma_est



            




