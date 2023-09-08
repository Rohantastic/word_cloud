from wordcloud import WordCloud, STOPWORDS
import wikipedia
from PIL import Image
import matplotlib.pyplot as plt

# Define stopwords
stop_words = set(STOPWORDS)

# Fetch Wikipedia summary
search_term = "virat kohli"
info = wikipedia.summary(search_term)

# Create a WordCloud object
wordcloud = WordCloud(stopwords=stop_words, background_color='white').generate(info)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
