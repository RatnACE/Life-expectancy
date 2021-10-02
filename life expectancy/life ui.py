import pandas as pd


from joblib import load
re=load("regress.joblib")
sc=load("scaler.joblib")
lr=load("rfr.joblib")





def fxn():
    bravo=(variable.get())
    
    dead= pd.read_csv('life expectancy data.csv',index_col=("Country"))
    
    dead.rename(columns={'Life expectancy ': 'Life Expectancy',
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











    first = dead.loc[[bravo],:]
    
    charlie=bmientry.get()
    
        
    
    
    first['Status'] =re.transform(first['Status'])
    
    cd=pd.DataFrame({"Status":[first["Status"].mean()],
                "Adult Mortality":[adentry.get()],
                "Infant Deaths":[infentry.get()],
                "Alcohol Intake(L)":[alcoholentry.get()],
                "Percentage Expenditure":[expentry.get()],
                "HepB Vaccination %":[hepentry.get()],
                "Measles":[first["Measles"].mean()],
                "BMI":[charlie],
                "Under Five Deaths":[first["Under Five Deaths"].mean()],
                "Pol3 Vaccination %":[polentry.get()],
                "Diphtheria Vaccination %":[dientry.get()],
                "HIV/AIDS": [first["HIV/AIDS"].mean()],
                "GDP":[gdpentry.get()],
                "Thinness 10-19 years":[first["Thinness 10-19 years"].mean()],
                "Thinness 5-9 years":[first["Thinness 5-9 years"].mean()],
              })
    cd=sc.transform(cd)

    jack=(lr.predict(cd))
    denver=Tk()
    denver.resizable(0,0)
    ratnesh=("life expectency of {} is : {} %".format(bravo,jack))
    
    result=Label(denver,text=ratnesh,font=("ARIAL",35,"bold"),fg="white", bg="black")
    result.pack()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   





















from tkinter import *
rio=Tk() 
rio.geometry("500x800")
rio.title("Life Expectency")

OPTIONS = [
'Afghanistan' ,'Albania', 'Algeria', 'Angola', 'Antigua and Barbuda',
 'Argentina' ,'Armenia' ,'Australia' ,'Austria' ,'Azerbaijan' ,'Bahamas',
 'Bahrain' ,'Bangladesh' ,'Barbados' ,'Belarus' ,'Belgium' ,'Belize' ,'Benin'
, 'Bhutan' ,'Bolivia (Plurinational State of)' ,'Bosnia and Herzegovina',
 'Botswana' ,'Brazil' ,'Brunei Darussalam' ,'Bulgaria' ,'Burkina Faso',
 'Burundi' ,"Côte d'Ivoire" ,'Cabo Verde' ,'Cambodia' ,'Cameroon' ,'Canada',
 'Central African Republic' ,'Chad' ,'Chile' ,'China' ,'Colombia' ,'Comoros',
 'Congo' ,'Cook Islands' ,'Costa Rica' ,'Croatia' ,'Cuba' ,'Cyprus' ,'Czechia'
, "Democratic People's Republic of Korea"
 ,'Democratic Republic of the Congo' ,'Denmark' ,'Djibouti' ,'Dominica',
 'Dominican Republic' ,'Ecuador' ,'Egypt' ,'El Salvador' ,'Equatorial Guinea',
 'Eritrea' ,'Estonia' ,'Ethiopia' ,'Fiji' ,'Finland' ,'France' ,'Gabon' ,'Gambia',
 'Georgia' ,'Germany' ,'Ghana' ,'Greece' ,'Grenada' ,'Guatemala' ,'Guinea',
 'Guinea-Bissau' ,'Guyana' ,'Haiti' ,'Honduras' ,'Hungary' ,'Iceland' ,'India',
 'Indonesia' ,'Iran (Islamic Republic of)' ,'Iraq' ,'Ireland' ,'Israel',
 'Italy' ,'Jamaica' ,'Japan' ,'Jordan' ,'Kazakhstan' ,'Kenya' ,'Kiribati',
 'Kuwait' ,'Kyrgyzstan' ,"Lao People's Democratic Republic" 'Latvia',
 'Lebanon' ,'Lesotho' ,'Liberia' ,'Libya' ,'Lithuania' ,'Luxembourg',
 'Madagascar' ,'Malawi' ,'Malaysia' ,'Maldives' ,'Mali' ,'Malta',
 'Marshall Islands' ,'Mauritania' ,'Mauritius' ,'Mexico',
 'Micronesia (Federated States of)' ,'Monaco' ,'Mongolia' ,'Montenegro',
 'Morocco' ,'Mozambique' ,'Myanmar' ,'Namibia' ,'Nauru' ,'Nepal' ,'Netherlands',
 'New Zealand' ,'Nicaragua' ,'Niger' ,'Nigeria' ,'Niue' ,'Norway' ,'Oman',
 'Pakistan' ,'Palau' ,'Panama' ,'Papua New Guinea' ,'Paraguay' ,'Peru',
 'Philippines' ,'Poland' ,'Portugal' ,'Qatar' ,'Republic of Korea',
 'Republic of Moldova' ,'Romania' ,'Russian Federation' ,'Rwanda',
 'Saint Kitts and Nevis' ,'Saint Lucia' ,'Saint Vincent and the Grenadines',
 'Samoa' ,'San Marino' ,'Sao Tome and Principe' ,'Saudi Arabia' ,'Senegal',
 'Serbia' ,'Seychelles' ,'Sierra Leone' ,'Singapore' ,'Slovakia' ,'Slovenia',
 'Solomon Islands' ,'Somalia' ,'South Africa' ,'South Sudan' ,'Spain',
 'Sri Lanka' ,'Sudan' ,'Suriname' ,'Swaziland' ,'Sweden' ,'Switzerland',
 'Syrian Arab Republic' ,'Tajikistan' ,'Thailand',
 'The former Yugoslav republic of Macedonia' ,'Timor-Leste' ,'Togo' ,'Tonga',
 'Trinidad and Tobago' ,'Tunisia' ,'Turkey' ,'Turkmenistan' ,'Tuvalu' ,'Uganda',
 'Ukraine' ,'United Arab Emirates',
 'United Kingdom of Great Britain and Northern Ireland',
 'United Republic of Tanzania' ,'United States of America' ,'Uruguay'
, 'Uzbekistan' ,'Vanuatu' ,'Venezuela (Bolivarian Republic of)' ,'Viet Nam'
 ,'Yemen' ,'Zambia' ,'Zimbabwe'
] #etc


label_head=Label(rio,text="Life Expectency of your country",font=("ARIAL",18,"bold")).place(x=15,y=5)


variable = StringVar(rio)
variable.set(OPTIONS[76]) # default value

w = OptionMenu(rio, variable, *OPTIONS).place(x=345,y=65)



label1=Label(rio,text="Select Country",font=("ARIAL",15)).place(x=35,y=65)


bmientry=Entry(rio,width=20)
bmientry.place(x=345,y=135)
label2=Label(rio,text="Average BMI",font=("ARIAL",15)).place(x=35,y=130)

alcoholentry=Entry(rio,width=20)
alcoholentry.place(x=345,y=200)
label3=Label(rio,text="Avg. Alcohol Intake %",font=("ARIAL",15)).place(x=35,y=195)

expentry=Entry(rio,width=20)
expentry.place(x=345,y=265)
label4=Label(rio,text="Percentage Expenditure",font=("ARIAL",15)).place(x=35,y=260)

hepentry=Entry(rio,width=20)
hepentry.place(x=345,y=330)
label5=Label(rio,text="HepB Vaccination %",font=("ARIAL",15)).place(x=35,y=325)

polentry=Entry(rio,width=20)
polentry.place(x=345,y=395)
label5=Label(rio,text="Polio Vaccination  %",font=("ARIAL",15)).place(x=35,y=390)

dientry=Entry(rio,width=20)
dientry.place(x=345,y=460)
label5=Label(rio,text="Diphtheria Vaccination %",font=("ARIAL",15)).place(x=35,y=455)

gdpentry=Entry(rio,width=20)
gdpentry.place(x=345,y=530)
label5=Label(rio,text="GDP",font=("ARIAL",15)).place(x=35,y=525)

adentry=Entry(rio,width=20)
adentry.place(x=345,y=595)
label5=Label(rio,text="Adult Mortality Rate",font=("ARIAL",15)).place(x=35,y=590)

infentry=Entry(rio,width=20)
infentry.place(x=345,y=660)
label5=Label(rio,text="Infant Death Rate",font=("ARIAL",15)).place(x=35,y=655)

butt=Button(rio,text="Check",command=fxn).place(x=240,y=720)










rio.mainloop()














                   
  






