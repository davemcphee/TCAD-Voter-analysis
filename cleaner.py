import pandas as pd
from pandas import Series

df = pd.read_csv('VoterRegOpenDataWithHistory.csv', encoding="ISO-8859-1")
#df = pd.read_csv('sample.csv', encoding="ISO-8859-1")
print("Original frame has %i rows\n" % (len(df)))

# select only people in Austin, right?
atx = df.loc[df['RSCITY'] == 'AUSTIN']
print("Austin only frame has %i rows\n" % (len(atx)))

# Add a SCORE column, set to 0
atx['SCORE'] = Series(0, index=atx.index)

# define scoring rows - having data in this row gets you a point
elections = ['P14VOTED', 'GA14VOTED', 'PR14VOTED', 'G14VOTED', 'GR14VOTED', 'GA15VOTED', 'G15VOTED']

counter = 0
for index, row in atx.iterrows():
	if (counter % 1000 == 0):
		print("At row %s" % (counter))	# keep us up to date

	for column in elections:
		if (row[column] != 0):
			atx.loc[index, 'SCORE'] += 1
	counter += 1

atx.to_csv('Scores.csv')