import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/movies.csv")

# Genre count
genre_count = df['genre'].value_counts()

# Rating distribution
rating_dist = df['rating']

# Correlation analysis
correlation = df[['budget', 'revenue', 'rating']].corr()

print("Correlation Matrix:")
print(correlation)

# VISUALIZATION
plt.figure(figsize=(10,4))
genre_count.plot(kind='bar')
plt.title("Genre Popularity")
plt.ylabel("Number of Movies")
plt.show()

plt.figure(figsize=(10,4))
plt.hist(df['rating'], bins=10)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10,4))
plt.scatter(df['budget'], df['revenue'])
plt.title("Budget vs Revenue")
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.show()
