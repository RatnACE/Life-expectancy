import pandas as pd




df= pd.read_csv('life expectancy data.csv')


df.rename(columns={'Life expectancy ': 'Life Expectancy',
                   'infant deaths': 'Infant Deaths',
                   'percentage expenditure': 'Percentage Expenditure',
                   'Measles ': 'Measles',
                   ' BMI ': 'BMI',
                   'under-five deaths ': 'Under Five Deaths',
                   'Diphtheria ': 'Diphtheria Vaccination %',
                   ' HIV/AIDS': 'HIV/AIDS',
                   ' thinness  1-19 years': 'Thinness 10-19 years',
                   ' thinness 5-9 years': 'Thinness 5-9 years',
                   'Income composition of resources': 'Resources Income Composition',
                   'Total expenditure': 'Total Expenditure',
                   'Polio': 'Pol3 Vaccination %',
                   'Hepatitis B': 'HepB Vaccination %', 
                   'Alcohol': 'Alcohol Intake(L)'
                  },inplace=True)



df['Country'] = df['Country'].astype('string')
df['Status'] = df['Status'].astype('string')





null_col = ('Life Expectancy', 'Adult Mortality', 'Alcohol Intake(L)', 'HepB Vaccination %', 'BMI', 'Pol3 Vaccination %', 'Total Expenditure', 'Diphtheria Vaccination %', 'GDP', 'Population', 'Thinness 10-19 years', 'Thinness 5-9 years', 'Resources Income Composition', 'Schooling')
data_valid = []
for year in list(df.Year.unique()):
    year_data = df[df.Year == year].copy()
    for col in null_col:
        year_data[col] = year_data[col].fillna(year_data[col].dropna().mean()).copy()
    data_valid.append(year_data)
df = pd.concat(data_valid).copy()




from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Status'] =le.fit_transform(df['Status'])











x = df.drop(['Country', 'Year', 'Life Expectancy', 'Population', 'Total Expenditure','Resources Income Composition','Schooling'], axis=1)
y=df['Life Expectancy']


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)

from sklearn.ensemble import RandomForestRegressor
lr = RandomForestRegressor(random_state=0)
lr.fit(x_train, y_train)

y_pred = lr.predict(x_train)

from sklearn.metrics import r2_score
print(r2_score(y_train,y_pred))



from joblib import dump, load
dump(le,"regress.joblib")
dump(sc,"scaler.joblib")
dump(lr,"rfr.joblib")





