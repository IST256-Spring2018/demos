import pandas as pd
import matplotlib.pyplot as plt

# Returns a list of Dataframes, we only want the first one
df = pd.read_html("https://ischool.syr.edu/classes/fall-2018/")[0]

# See what we got
print(df.head())

# Add a column for undergrad vs grad
df = df.assign(Number=df['Course'].str[-3:].astype(int))
df.loc[(df['Number'] < 500), 'Level'] = 'Undergrad'
df.loc[(df['Number'] >= 500), 'Level'] = 'Graduate'
print(df)

# Print Percentage of Offerings
print(df["Level"].value_counts(normalize=True))

# What about Friday classes
print(df[ (df["Day"].str.contains("F")) & (df["Level"] == "Undergrad") ])

# What classes start at 8AM
print(df[ (df["Time"].str.contains("8:00am")) & (df["Level"] == "Undergrad") ])

# What are the most offered?
plotdf = df.Course.value_counts().reset_index().rename(columns={'index': 'Course', 'Course': 'Count'})
print(plotdf.head())
sample_plot = plotdf.plot.bar(x ='Course', y = 'Count')
plt.show()
