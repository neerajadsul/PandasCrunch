import pandas as pd


df = pd.read_csv('./data/fire_dept_salaries.csv')

fire_dept_employees = df[df['JobTitle'].str.contains('FIRE')]
police_dept_employees = df[df['JobTitle'].str.contains('POLICE')]

fire_to_police_ratio = fire_dept_employees['Id'].count()/police_dept_employees['Id'].count()

print(f'Ratio of number of employees between fire and police dept is: {round(fire_to_police_ratio, 1)}')

print(f'Mean salary of police department: {round(police_dept_employees["BasePay"].mean())}')
print(f'Mean salary of fire department: {round(fire_dept_employees["BasePay"].mean())}')


