import pandas as pd

df = pd.read_csv("pokemon_data.csv")

# print(df)

# print(df.head(3))
# #first three rows with header

# df_xlsx = pd.read_excel("pokemon_data.xlsx")
# print(df_xlsx)
# #read excel document

# df = pd.read_csv("pokemon_data.txt", delimiter = "\t")
# print(df)
# #read txt document, required to specify delimiter which is tab

# print(df.columns)
# # print headers

# print(df["Name"])
# #print specific column

# print(df["Name"][0:5])
# #print specific column with specific row

# print(df[["Name", "Type 1", "HP"]])
# #print multiple columns (no need to be in order)

# print(df.iloc[1])
# #print specific row

# print(df.iloc[1:4])
# #print multiple rows

# print(df.iloc[1,4])
# #print specific cell

# for index, row in df.iterrows():
#     print(index, row)
# #print each row as a block

# for index, row in df.iterrows():
#     print(index, row["Name"])
# #print each row with corresponding specific column

# print(df.loc[df["Type 1"] == "Fire"])
# #print rows with specific value of a specific column

# print(df.describe())
# #print high level stat inference

# print(df.sort_values("Name"))
# #print rows with alphabetically sorted specific column

# print(df.sort_values("Name", ascending = False))
# #print rows with alphabetically sorted specific column in descending order

# print(df.sort_values(["Type 1", "HP"]))
# #print sorted rows with respect to the first specified column and then the second specified column

# print(df.sort_values(["Type 1", "HP"], ascending = [1,0]))
# #print sorted rows with different orders (1 = ascending, 2 = descending)

# df["total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]
# print(df)
# #create a new colum to df and print

# df["total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]
# print(df.drop(columns = ["total"]))
# #drop specific column

# df["total"] = df.iloc[:, 4:10].sum(axis = 1)
# print(df)
# #create column by adding the value of other existing columns 
# #(axis = 1 is adding the values horizontally, axis = 0 is adding the values vertically)

# df["total"] = df.iloc[:, 4:10].sum(axis = 1)
# cols =list(df.columns)
# df = df[cols[1:4] + [cols[-1]] + cols[4:12]]
# print(df.head(5))
# #rearrange columns

# df.to_csv("modified.csv")
# #create and modify csv file

# df.to_csv("modified.csv", index = False)
# #create and modify csv file without index

# df.to_excel("modified.xlsx", index = False)
# #create and modify excel file without index

# df.to_csv("modified.txt", index = False, sep = "\t")
# #create and modify txt file without index

# search = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")]
# print(search)
# search.to_csv("newdata.csv")
# #filter multiple values in specific columns (use "&" as "and", use "|" as "or")
# # , and then create and modify a new file

# search = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")]
# search = search.reset_index()
# print(search)
# #add new index to new list

# search = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")]
# search.reset_index(drop = True, inplace = True)
# print(search)
# #add new index, drop old index and replace dataframe directly

