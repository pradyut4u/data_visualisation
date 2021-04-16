import pandas as pd
import plotly.graph_objects as pgo
import plotly.express as pe
import csv
df=pd.read_csv("dvhw.csv")
a = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
fig=pe.scatter(a,x="student_id",y="level",size="attempt",color="attempt")
fig.show()