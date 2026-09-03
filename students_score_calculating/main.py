import pandas as pd
import numpy as np

df = pd.read_csv('marksheets.csv')

subjects_cols = [c for c in df.columns if '(' in c]

marks = df[subjects_cols].values
names = df['Student Name'].values
subjects = np.array([c.split(' (')[0] for c in subjects_cols])

