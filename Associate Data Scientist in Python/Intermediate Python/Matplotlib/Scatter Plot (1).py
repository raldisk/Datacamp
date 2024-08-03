# Change the line plot below to a scatter plot
plt.plot(gdp_cap, life_exp)
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale("log")

# Show plot
plt.show()
