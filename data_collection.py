import yfinance as yf
import pandas as pd

# this class fetch each stock data using their symbol, period, timeframe/interval

class DataFetcher:
    def __init__(self, symbol, period, timeframe):
        self.symbol = symbol
        self.period = period
        self.timeframe = timeframe

    def fetch(self):

        """
        this the function that fetch for the data, change
        the column name to lowercase and save the data into a csv file
        """

        ticker = yf.Ticker(self.symbol).history(period=self.period,
                            interval=self.timeframe, auto_adjust=True)
        ticker.rename(columns = str.lower, inplace = True)
        ticker = ticker[["open", "high", "low", "close", "volume"]]
        ticker.to_csv("variance/data/{0}.csv".format(self.symbol))
        return ticker.head()

# This class analyse the data provided and return with certain output

class AnalyseData:
    def __init__(self,file):
        self.file = file

    def read_data(self):

        """
        this function read the data stored in a csv file
        and compare if the close column is greater than open
        column to create a new column called color
        """

        data = pd.read_csv(self.file)
        data['color'] = (data['close']) > (data['open'])
        data['color'] = data.color.map({True:"green", False:"red"})
        return data.head()

# This class calculate number of crossabove, crossbelow, and generate every cross timestamp       
class CrossInfo:
    def __init__(self,file):
        self.file = file
        data = pd.read_csv(self.file)

# cleaning of data since there are missing figures
        data['0'] = data['0'].fillna((data['0'].mean()))
        data['1'] = data['1'].fillna((data['1'].mean()))
        self.data = data
        self.s1 = list(data['0'])
        self.s2 = list(data['1'])

    def crossabove(self):

        """ this function calculate the total crossabove """

        total = 0
        for value_one,value_two in zip(self.s1, self.s2):
            if value_one > value_two:
                total +=1
        return total

    def crossbelow(self):

        """ this function calculate the total crossbelow """

        total = 0
        for value_one,value_two in zip(self.s1, self.s2):
            if value_one < value_two:
                total +=1
        return total

    def total_cross(self):

        """ this function calculate the total cross """

        total = self.crossabove() + self.crossbelow()
        return total

    def crossabove_datetime(self):

        """ this function generate every crossabove datetime """

        triggers_in_datetime = []
        for value, _ in enumerate(zip(self.s1,self.s2)):
            if self.s1[value] > self.s2[value]:
                triggers_in_datetime.append(self.data.iloc[value,:]['Datetime'])
        return triggers_in_datetime

    def crossbelow_datetime(self):

        """ this function generate every crossbelow datetime """

        triggers_in_datetime = []
        for value, _ in enumerate(zip(self.s1,self.s2)):
            if self.s1[value] < self.s2[value]:
                triggers_in_datetime.append(self.data.iloc[value,:]['Datetime'])
        return triggers_in_datetime

# creating class objects

# tsla = DataFetcher(symbol="TSLA", period="5d", timeframe="5m")
# print(tsla.fetch())

# file = AnalyseData("data/FB.csv")
# print(file.read_data())

# file = CrossInfo("task3.csv")
# print(file.crossabove())
# print(file.crossbelow())
# print(file.total_cross())
# print(file.crossabove_datetime())
# print(file.crossbelow_datetime())