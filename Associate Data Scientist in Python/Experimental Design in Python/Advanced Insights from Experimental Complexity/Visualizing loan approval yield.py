"""Visualizing loan approval yield
In the realm of financial services, understanding the factors that influence loan approval rates is crucial for both lenders and borrowers. A financial institution has conducted a study and collected data on loan applications, detailing the amount requested, the applicant's credit score, employment status, and the ultimate yield of the approval process. This rich dataset offers a window into the nuanced dynamics at play in loan decision-making. You have been asked to dive into the loan_approval_yield dataset to understand how loan amounts and credit scores influence approval yields.

The loan_approval_yield DataFrame, seaborn as sns, and matplotlib.pyplot as plt have been loaded for you."""

# INSTRUCTIONS 1/2: Create a side-by-side bar graph, setting the x-axis to 'LoanAmount', the y-axis to 'ApprovalYield', and differentiating the bars with hues for 'CreditScore'.

# Use Seaborn to create the bar graph
sns.catplot(
    x="LoanAmount",
    y="ApprovalYield",
    hue="CreditScore",
    kind="bar",
    data=loan_approval_yield,
)
plt.title("Loan Approval Yield by Amount and Credit Score")
plt.show()

# INSTRUCTIONS 2/2
# Poor credit scores tend to have similar approval yields across loan amounts, while Good credit scores have more variability.
