import numpy as np


class Data:
    def __init__(self, data):
        self.price = data
        self.risk_free_rate = 0.51/100
        self.returns = self.get_stock_return()

    def get_price_from_database(self):
        pass

    def set_risk_free_rate(self,risk_free_rate):
        self.risk_free_rate = risk_free_rate

    def get_stock_price(self):
        return self.price

    def get_stock_return(self, if_print=False):
        stock_returns = self.price.shift(1) / self.price - 1  # need test
        # self.stock_return = self.stock_price.apply(get_stock_return)
        stock_returns = stock_returns.dropna()
        if if_print:
            print("Return Matrix is \n", stock_returns)
        return stock_returns

    def get_equal_weighted_return(self, if_print=False):
        equal_weighted_return = self.returns.stack().mean()
        if if_print:
            print("Equal weighted portfolio return (benchmark): ", equal_weighted_return)
        return equal_weighted_return

    def get_equal_weighted_std(self, if_print=False):
        equal_weighted_std = np.std(self.returns.mean())
        if if_print:
            print("Equal weighted portfolio std (benchmark): ",equal_weighted_std)
        return equal_weighted_std

    def get_risk_aversion(self, if_print=False):
        risk_aversion = (Data.get_equal_weighted_return() - self.risk_free_rate)/ (Data.get_equal_weighted_std() ** 2)
        if if_print:
            print("risk aversion coefficient is ",risk_aversion)
        return risk_aversion









def main(self):
    pass

if __name__ == "__main__":
    pass

