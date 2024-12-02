import pandas as pd
import statsmodels.api as sm

#Manually inputing data from CFA chapter in a dictionary
data = {
    "Money Supply": [0.0685, 0.116, 0.0575, 0.105, 0.125, 0.135],
    "Inflation Rate": [0.0545, 0.0776, 0.0349, 0.0735, 0.0825, 0.1076]
}

#Moving the data into DataFrame
df = pd.DataFrame(data)

#Changing the labels on the DataFrame 
df.index = ["A", "B", "C", "D", "E", "F"]

#Using straight forward calculations on each column in the DataFrame
ms_avg = df["Money Supply"].mean()
ms_sum = df["Money Supply"].sum()
ms_var = df["Money Supply"].var()
ms_std = df["Money Supply"].std()

ir_avg = df["Inflation Rate"].mean()
ir_sum = df["Inflation Rate"].sum()
ir_var = df["Inflation Rate"].var()
ir_std = df["Inflation Rate"].std()

#Calculating Covariance in two ways calculating directly or creating the Covariance Matrix 
covariance = df["Money Supply"].cov(df["Inflation Rate"])

cov_matrix = df.cov()

#Calculating Correlation in two ways calculating directly or creating the Correlation Matrix
correlation = df["Money Supply"].corr(df["Inflation Rate"])

corr_matrix = df.corr()

#Calculating Linear Regression 
x = df["Money Supply"]
y = df["Inflation Rate"]

x = sm.add_constant(x)

model = sm.OLS(y, x).fit()

#Calculated the Sum of Squared Errors SSE 

residuals = model.resid
sqr_resi = pow(residuals, 2)
sse = sqr_resi.sum()

#Calculate the Standard Error of Estimate

n = len(y)
k = len(model.params)

see = pow((sse / (n - k)), 0.5)

print(model.summary())