import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("E:\\MACHINE LEARNING\\New folder\\company.csv")
print(data.head())

data.columns= ["satisfaction_level","last_evaluation","number_project",
               "average_montly_hours","time_spend_company","Work_accident",
               "left","Promotion_last_5years","Department","salary"]

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr())
plt.show()

