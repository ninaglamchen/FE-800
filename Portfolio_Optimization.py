import numpy as np

class PortfolioOptimization:
    def mean_variance_optimization(self, BlackLitterman):
        mu = np.matrix(BlackLitterman.combined_return)
        Q = np.matrix(BlackLitterman.combined_covariance_matrix)
        l = np.matrix(np.repeat([1], self.num))
        c = np.matrix([1])
        O = np.matrix([0])

        A = np.concatenate((Q, l), axis=0)
        B = np.concatenate((np.transpose(l), O), axis=0)
        C = np.column_stack((A, B))
        D = np.concatenate(((self.risk_aversion * np.transpose(mu)), c), axis=0)

        E = np.dot(np.linalg.inv(C), D)
        self.weights = np.delete(E, len(E) - 1, 0)

    def efficient_frontier(self):
        pass

    def portfolio_performance(self, weights):
        pass

