# 1/3
# Write a regex to obtain user mentions
print(re.findall(r"User_mentions:\d", sentiment_analysis))


# 2/3
# Write a regex to obtain number of likes
print(re.findall(r"likes:\s\d", sentiment_analysis))


# 3/3
# Write a regex to obtain number of retweets
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))
