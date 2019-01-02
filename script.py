import pandas as pd
import matplotlib.pyplot as plt
#Use split apply combine 
#Read the csv file using panda
df = pd.read_csv("data.csv")
#Take only the two columns that interest us, purpose and interest rate
temp = df[['purpose', 'int_rate']]
#Group them by purpose into another dataframe, take the average interest rate, and reset the index. This is important since the order is changing
results = temp.groupby('purpose')['int_rate'].mean().reset_index()
#Rename the columns, this is to change int_rate into avg_rate
results.columns = ['purpose', 'avg_rate']
#Print the results
print(results)

#This is for the bar chart.
#take the results and put them into something that can be plotted
#Set zorder to 3 in order to have horizontal grid be behind the bars.
#For the x axis, take the various purposes from the results
ax = results.plot(x="purpose", y='avg_rate', kind='bar', title='Average interest rate depending on purpose', figsize=(20,10), fontsize=12, legend=False, width=0.8, zorder = 3)

#Label the x and y axis
ax.set_xlabel("purpose", fontsize=12)
ax.set_ylabel("mean(int_rate)", fontsize=12)

#Rotate the x axis labels horizontally
plt.xticks(rotation = 0)

#Change the colors of the grid and the background color of the chart
ax.set_facecolor('lavender')
ax.yaxis.grid(zorder=0, color='white')
#Display the graph
plt.show()




