import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('q20_soccer.csv')

# Top 5 players by goals
top5_goals = df.nlargest(5, 'goals')[['name','goals']]
print("Top 5 Players by Goals Scored:")
print(top5_goals.to_string(index=False))

# Top 5 players by salary
top5_salary = df.nlargest(5, 'weekly_salary')[['name','weekly_salary']]
print("\nTop 5 Players by Weekly Salary:")
print(top5_salary.to_string(index=False))

# Average age and players above average
avg_age = df['age'].mean()
print(f"\nAverage Age: {avg_age:.2f}")
above_avg = df[df['age'] > avg_age][['name','age']]
print(f"\nPlayers above average age ({avg_age:.2f}):")
print(above_avg.to_string(index=False))

# Bar chart - position distribution
pos_count = df['position'].value_counts()
plt.figure(figsize=(8, 5))
pos_count.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Player Distribution by Position')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.tight_layout()
plt.savefig('q20_positions.png')
plt.show()
print("\nBar chart saved as q20_positions.png")
