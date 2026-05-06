import pandas as pd

class SalesAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.df['Revenue'] = self.df['Units Sold'] * self.df['Unit Price']

    def total_revenue(self):
        return self.df['Revenue'].sum()

    def average_units_sold_per_product(self):
        return self.df.groupby('Product')['Units Sold'].mean()

    def revenue_by_product(self):
        return self.df.groupby('Product')['Revenue'].sum()

    def summary(self):
        print("Total Revenue:", self.total_revenue())
        print("\nAverage Units Sold per Product:")
        print(self.average_units_sold_per_product())
        print("\nRevenue by Product:")
        print(self.revenue_by_product())

if __name__ == "__main__":
    analyzer = SalesAnalyzer("sales_data.csv")
    analyzer.summary()
