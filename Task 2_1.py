import pandas as pd
df = pd.read_csv("01.Data Cleaning and Preprocessing.csv")
print(df)

#shows first few rows
df.head()

df.info()
print("  Showing filtered date values ")
filtered_df = df[df['Y-Kappa'] > 20]

print(filtered_df)



# Handle missing values in 'AAWhiteSt-4 ' by filling with mean
df.fillna(value={'AAWhiteSt-4 ': df['AAWhiteSt-4 '].mean()}, inplace=True)
#Check for missing values using
df.isnull().sum()
df.dropna(inplace=True)

print(df)
df.describe()
mean_of_T_T_column,Standard_deviation_of_Sulphidtyl=df['T-Top-Chips-4 '].mean(), df['SulphidityL-4 '].std()

print("  Mean of T-Top-Chips-4 column")
print( mean_of_T_T_column)
print("  Standard_deviation of SulphidityL-4 column")
print(Standard_deviation_of_Sulphidtyl)