# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
data = np.array(data)
print(data.shape)
#print(data)
#Code starts here
census = np.concatenate((data,new_record))
print(census.shape)
#step 2
age = census[:,0]
#print(age)
print(age.shape)
max_age = np.max(age)
print('max age is : ' + str(max_age))
min_age = np.min(age)
print('min age is : ' + str(min_age))
age_mean = age.mean()
print('mean_age age is : ' + str(age_mean))
age_std = np.std(age)
print('std age is : ' + str(age_std))


#step 3
race = census[:,2]

race_0 = np.extract(race == 0, race)
race_1 = np.extract(race == 1, race)
race_2 = np.extract(race == 2, race)
race_3 = np.extract(race == 3, race)
race_4 = np.extract(race == 4, race)
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
number_of_citizens = [len_0,len_1,len_2,len_3,len_4]
min_citizen = min(number_of_citizens)
print(min_citizen)
minority_race = number_of_citizens.index(6)
print(minority_race)


# step_4

senior_citizens = census[census[:,0]>60]
#print(senior_citizens)
senior_citizens_len = len(senior_citizens)
working_hours_sum = sum(senior_citizens[:,6])
# print(working_hours_sum)
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)
#step 5
high = census[census[:,1]>10]
print(type(high))
avg_pay_high = high.mean(axis=0)[7]
low = census[census[:,1]<=10]
#print(low)
avg_pay_low = low.mean(axis=0)[7]
print(avg_pay_high)
print(avg_pay_low)











