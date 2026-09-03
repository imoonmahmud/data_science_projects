import pandas as pd
import numpy as np
import csv

df = pd.read_csv('marksheets.csv')
subjects_cols = [c for c in df.columns if '(' in c]

marks = df[subjects_cols].values
names = df['Student Name'].values
student_id = df['Student ID']
subjects = np.array([c.split(' (')[0] for c in subjects_cols])

totals = np.sum(marks, axis=1)
averages = np.average(marks, axis=1)
ranks = np.argsort(averages)[::-1]


with open('results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    header = ['Rank', 'Student ID', 'Student Name', 'Total', 'Average', 'Grade']
    writer.writerow(header)

    for rank, idx in enumerate(ranks, 1):
        avg = averages[idx]
        grade = 'A+' if avg >= 80 else 'A' if avg >= 70 else 'B' if avg >= 60 else 'C'
        writer.writerow([
                    rank,
                    student_id[idx],
                    names[idx],
                    totals[idx],
                    round(avg, 1),
                    grade])
