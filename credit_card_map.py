import sys
import pandas as pd

df = pd.read_csv(sys.stdin)

print(df.iloc[1,6])

for index, row in df.iterrows():

    ID = row['ID']

    y = row['IS_DEFAULT']

    for i in range(6, 12):

        value_at_xi = row[i]

        output = "%s\t%s" % (f"{ID},{value_at_xi},{y}","")

        print(output)