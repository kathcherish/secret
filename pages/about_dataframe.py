import pandas as pd

data = pd.read_excel('source.xlsx')

print(data)

criteria1 = data ['Category'] == 'Food'
criteria2 = data['Store'] == 'Indomaret'
criteria3 = data['Price'] > 25000
criteria4 = (data['Price'] > 15000) & (data['Price'] < 50000)
criteria5 = (criteria1) & (criteria2) & (criteria4)

print(data[criteria5])
print(data[criteria5].sort_values('Price',ascending=True))