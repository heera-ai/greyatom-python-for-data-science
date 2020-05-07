# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
#print(bank_data.head(2))
categorical_var = bank_data.select_dtypes(include = 'object')
print(categorical_var.shape)
numerical_var = bank_data.select_dtypes(include = 'number')
print(numerical_var.shape)

#step 2
bank_data.drop('Loan_ID',axis = 1,inplace = True)
banks = bank_data
# print(banks.shape)
# print(banks.isnull().sum())
bank_mode = banks.mode()
# print(bank_mode)
bank_mode_list = list( bank_mode.iloc[0])
print(bank_mode_list)
features = list(banks.columns)
print(features)

def fills(df,values,feature):
    i = 0
    while i <12:
        df[feature[i]].fillna(value = values[i],inplace =True)
        i += 1
        

fills(banks,bank_mode_list,features)
print(banks.isnull().sum().values.sum())

# step 3
avg_loan_amount = pd.pivot_table(banks,values = ['LoanAmount'],index = ['Gender', 'Married', 'Self_Employed'],aggfunc = 'mean')
#print(avg_loan_amount)


#step4
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
# print(loan_approved_se)

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
# print(loan_approved_nse)
Loan_Status_Total = 614 #given data
percentage_se = (len(loan_approved_se)/Loan_Status_Total)*100
#print(percentage_se)

percentage_nse = (len(loan_approved_nse)/Loan_Status_Total)*100
#print(percentage_nse)

#step 5
def time_converter(months):
    years = months/12
    return years

loan_term = banks['Loan_Amount_Term'].apply(time_converter)
# print(loan_term)
big_loan_term = (loan_term >= 25).sum()
# print(big_loan_term)


# step 6:
loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)





