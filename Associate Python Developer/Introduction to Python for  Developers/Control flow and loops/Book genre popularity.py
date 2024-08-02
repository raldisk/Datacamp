for genre, average_sale in genre_sales.items():
    # Filter for the maximum sales value
    if average_sale == 5166000000:
        # Print the genre
        print("Most popular genre: ", genre)
        print("Average sales: ", average_sale)

    # Filter for the minimum sales value
    elif average_sale == 80000000:
        # Print the genre
        print("Least popular genre: ", genre)
        print("Average sales: ", average_sale)
