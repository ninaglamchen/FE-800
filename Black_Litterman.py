import numpy as np
import pandas as pd
from data import *

# def get_stock_return(stock_price: pd.DataFrame, if_print=False):
#     # stock_return = (stock_price - stock_price.appendleft(0)) / stock_price
#     # self.stock_return = self.stock_return - benchmark
#     stock_return = stock_price.shift(1) / stock_price - 1
#     stock_return = stock_return.dropna()
#     if if_print:
#         print("Return Matrix is \n", stock_return)
#     return stock_return


# def get_equal_weighted_return(stock_price_matrix: pd.DataFrame):
#     equal_weighted_return = stock_price_matrix.stack().mean()
#     return equal_weighted_return


# def get_equal_weighted_std(stock_price_matrix: pd.DataFrame):
#     equal_weighted_std = np.std(stock_price_matrix.mean())
#     print(equal_weighted_std)
#     return equal_weighted_std


class BlackLitterman:
    def __init__(self, Data, views):
        # original data
        self.stock_price = Data.get_stock_price()
        self.num = len(Data.price)  # number of stocks
        self.stock_return = Data.returns
        self.covariance_matrix = None

        # input for the Implied Excess Equilibrium Return
        self.risk_aversion = Data.get_risk_aversion()
        self.capital_weights = pd.read_csv(r"C:\My Files\Study\17 Spring\800 - Special Problems in FE (MS)\Code\FE-800\csv\weight.csv",index_col=0,header=None)
        # self.covariance_matrix_excess = None
        self.equilibrium_expected_return = None

        # input for the Combined Expected Return
        self.views = views

        # result of Black-Litterman
        self.combined_return = None
        self.combined_covariance_matrix = None

        # result of mean-variance portfolio optimization
        self.weights = None

    # def get_stock_return(self, if_print = False):
    #     stock_return = (self.stock_price - self.stock_price.shift(1)) / self.stock_price.shift(1)
    #     # self.stock_return = self.stock_return - benchmark
    #     if if_print:
    #         print("Return Matrix is \n", stock_return)

    def get_covariance_matrix(self, if_print = False):
        # self.stock_return = get_stock_return(self.stock_price)
        self.covariance_matrix = np.cov(self.stock_return, rowvar=False)

        if if_print:
            print("Covariance Matrix is \n", self.covariance_matrix)

    def get_equilibrium_expected_return(self, if_print = False):
        self.get_covariance_matrix()
        self.equilibrium_expected_return = self.risk_aversion * np.dot(self.covariance_matrix, self.capital_weights)
        if if_print:
            print("Equilibrium Expected Return is \n", self.equilibrium_expected_return)

    def get_combined_return(self):
        # tau: a scalar
        # Sigma: the covariance matrix of excess returns (N * N)
        # P: a matrix that identifies the assets involved in the views(K * N or 1 * N)
        # Omega: a diagonal covariance matrix of error terms from the expressed views representing the uncertainty in each view(K * K)
        # Pi: Implied Equilibrium Return(N * 1)
        # Q: view vector

        self.get_equilibrium_expected_return()
        P = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) # need a function
        K = len(self.views)  # need a function
        var = []
        for i in range(K):
            var.append(self.risk_aversion*(P[i].dot(self.covariance_matrix.dot(P[i].transpose()))))
        Omega = np.diag(var)

        #Omega = np.diag((np.repeat([1],[self.num]))) # need a function

        tau_Sigma_inv = np.linalg.inv(self.risk_aversion * self.covariance_matrix)
        P_Omega_inv_P = (P.transpose().dot(np.linalg.inv(Omega))).dot(P)
        tau_Sigma_inv_Pi = np.dot(tau_Sigma_inv,self.equilibrium_expected_return)
        P_Omega_inv_Q = (P.transpose().dot(np.linalg.inv(Omega))).dot(self.views)

        self.combined_return = np.dot(np.linalg.inv(tau_Sigma_inv + P_Omega_inv_P),(tau_Sigma_inv_Pi + P_Omega_inv_Q))
        self.combined_covariance_matrix = self.covariance_matrix + np.linalg.inv(tau_Sigma_inv + P_Omega_inv_P)

    def mean_variance_optimization(self, expected_return, covariance_matrix):
        mu = np.matrix(expected_return)#.transpose()
        Q = np.matrix(covariance_matrix)
        l = np.matrix(np.repeat([1], self.num))
        c = np.matrix([1])
        O = np.matrix([0])

        A = np.concatenate((Q, l), axis=0)
        B = np.concatenate((np.transpose(l), O), axis=0)
        C = np.column_stack((A, B))
        D = np.concatenate(((self.risk_aversion * np.transpose(mu)), c), axis=0)

        E = np.dot(np.linalg.inv(C), D)
        self.weights = np.delete(E, len(E)-1, 0)

    def efficient_frontier(self):
        pass

    def portfolio_performance(self,weights):
        pass

    def run(self):
        self.get_combined_return()
        self.mean_variance_optimization(self.combined_return,self.combined_covariance_matrix)
        self.mean_variance_optimization(np.mean(self.stock_return), self.covariance_matrix)


def main():
    pass

if __name__ == "__main__":
    main()
