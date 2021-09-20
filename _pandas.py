import numpy as np
import pandas as pd

d = [10,5,62,89]
i = ["Thomas","Emily","Sam","Scott"]
print(pd.Series(d))
print(pd.Series(d, i))
print(pd.Series(d, i, name="score"))
print(pd.Series({k:v for k, v in zip(i, d)}))

d = {"c1": [1,2,3,4], "c2":[5,6,7,8]}
print(pd.DataFrame(d))

d = np.random.rand(10,5)
i = list(range(1,11))
c = ["A","B","C","D","E"]
print(pd.DataFrame(d))
print(pd.DataFrame(d, i))
print(pd.DataFrame(d, i, c))

s1 = pd.Series(["Thomas", 80, "A"], index=["name", "score", "grade"], name=101)
s2 = pd.Series(["Emily", 45, "C"], index=["name", "score", "grade"], name=102)
df = pd.DataFrame([s1, s2])
print(df)
print(df.at[101, "name"])
print(df.at[102, "score"])
print(df.iat[0,0])
print(df.iat[1,1])
print(df["name"])
print(df[["name", "score"]])
print(df["name"][101])
print(df["name"].at[101])
print(df["name"].iat[0])
print(df.loc[101])
print(df.loc[[101, 102]])
print(df.loc[101]["name"])
print(df.loc[101].at["name"])
print(df.loc[101].iat[0])
print(df.iloc[0]["name"])
print(df.iloc[[0,1]]["name"])