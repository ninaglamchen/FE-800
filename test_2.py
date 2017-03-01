import pandas as pd
from save_price_data_to_csv import save_price_data
from Black_Litterman import *
import pandas as pd

def main():
    # ETFs = {'VTI': "US STOCKS", 'ITOT': "US STOCKS", 'SCHB': "US STOCKS", 'VEA': "FOREIGN \
    # DEVELOPED STOCKS", 'IXUS': "FOREIGN DEVELOPED STOCKS", 'SCHF': "FOREIGN DEVELOPED STOCKS",
    #         'VWO': "EMERGING MARKET STOCKS", 'IEMG': "EMERGING MARKET STOCKS", 'SCHE': "EMERGING MARKET\
    # STOCKS", 'VIG': "DIVIDEND GROWTH STOCKS", 'DVY': "DIVIDEND GROWTH STOCKS", 'SCHD': "DIVIDEND\
    # GROWTH STOCKS", 'VGSH': "US GOVERNMENT BONDS", 'IEF': "US GOVERNMENT BONDS", 'TLT': "US\
    # GOVERNMENT BONDS", 'MUB': "MUNICIPAL BONDS", 'TFI': "MUNICIPAL BONDS", 'PZA': "MUNICIPAL \
    # BONDS", 'SCHP': "TREASURY INFLATION-PROTECTED SECURITIES (TIPS)", 'TIP': "TREASURY \
    # INFLATION-PROTECTED SECURITIES (TIPS)", 'IPE': "TREASURY INFLATION-PROTECTED SECUR\
    # ITIES (TIPS)", 'XLE': "NATURAL RESOURCES", 'DJP': "NATURAL RESOURCES",
    #         'VDE': "NATURAL RESOURCES"}
    # data = save_price_data(ETFs)
    print("start")
    csv_file_path = r"C:\My Files\Study\17 Spring\800 - Special Problems in FE (MS)\Code\FE-800\csv\test.csv"

    data = pd.read_csv(filepath_or_buffer=csv_file_path,index_col=0).dropna()
    views = np.array([[2],[1]])
    blacklitterman_test = BlackLitterman(data, views, 1/967)
    blacklitterman_test.run()

    result = pd.DataFrame()
    result.insert(len(result.columns), "sample_stock_return",np.mean(blacklitterman_test.stock_return))
    result.insert(len(result.columns),"equilibrium expected return", blacklitterman_test.equilibrium_expected_return)
    result.insert(len(result.columns),"weights", blacklitterman_test.weights)
    print(result)

    # result.to_csv("result_.csv")

if __name__ == "__main__":
    main()
    print("success!")
