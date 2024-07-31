# 1/3
import text_analyzer

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

# 2/3
# plot_counts


# 3/3
import text_analyzer

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

# Run help on my_doc's plot method
help(my_doc.plot_counts)

# Plot the word_counts of my_doc
my_doc.plot_counts()
