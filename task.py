#Task5
import pandas as pd
import matplotlib as plt
monthly=pd.read_csv(r'C:\Users\uppal\Desktop\documents\Data Science Final project\Dr. Semmelweis and the Discovery of Handwashing\datasets\monthly_deaths.csv',parse_dates=["date"])
monthly["proportion_deaths"]=monthly["deaths"]/monthly["births"]
ax = monthly.plot(x="date", y="proportion_deaths",label="plot")
ax.set_ylabel("Proportion deaths")
