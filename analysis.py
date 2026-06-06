import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("product_reviews.csv")

# Function for sentiment analysis
def get_sentiment(review):

    analysis = TextBlob(str(review))

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"

    elif polarity < 0:
        return "Negative"

    else:
        return "Neutral"

# Add sentiment column
df["Sentiment"] = df["Review"].apply(get_sentiment)

# Save updated CSV
df.to_csv("updated_product_reviews.csv", index=False)

# Sentiment count
sentiment_counts = df["Sentiment"].value_counts()

# Create bar chart
plt.figure(figsize=(6,4))

plt.bar(sentiment_counts.index, sentiment_counts.values)

# Chart title
plt.title("Customer Review Sentiment Analysis")

# X-axis label
plt.xlabel("Sentiment")

# Y-axis label
plt.ylabel("Number of Reviews")

# Show chart
plt.show()