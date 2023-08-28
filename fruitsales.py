import pandas as pd

fruit_sales_df = pd.DataFrame({"Apples" : [35, 41], "Bananas" : [21, 34]}, index = ("2017 Sales", "2018 Sales"))

fruit_sales_df.to_csv("fruit.csv")