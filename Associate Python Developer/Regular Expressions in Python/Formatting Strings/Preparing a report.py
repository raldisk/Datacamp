# 1/3
from string import Template

# 2/3
# Import Template

# Create a template
wikipedia = Template("$tool is a $description")


# 3/3
# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")

# Substitute variables in template
print(wikipedia.substitute(tool=tool1, description=description1))
print(wikipedia.substitute(tool=tool2, description=description2))
print(wikipedia.substitute(tool=tool3, description=description3))
