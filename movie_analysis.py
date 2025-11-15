import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("movies.csv")

# Display first few rows
print(df.head())

# Genre Popularity
genre_count = df['genre'].value_counts()
plt.figure(figsize=(10,4))
genre_count.plot(kind='bar')
plt.title("Genre Popularity")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.show()

# Rating Distribution
plt.figure(figsize=(10,4))
plt.hist(df['rating'], bins=10)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Budget vs Revenue
plt.figure(figsize=(10,5))
plt.scatter(df['budget'], df['revenue'])
plt.title("Budget vs Revenue")
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.show()

# Correlation
correlation = df[['budget', 'revenue', 'rating']].corr()
print("\nCorrelation Matrix:\n", correlation)

# Summary Insights
print("\n🎬 MOVIE INSIGHTS SUMMARY")
print("Most common genre:", genre_count.idxmax())
print("Highest rated movie:", df.loc[df['rating'].idxmax(), 'title'])
print("Highest revenue movie:", df.loc[df['revenue'].idxmax(), 'title'])
