# 1/3
# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\s\w+\sago", date))

# 2/3

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))


# 3/3
# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))
