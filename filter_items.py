# Mirah Gordon
# Coding Challenge Submission 

# assume `items` is a list or tuple defined elsewhere
# assume `analysis_function` is defined elsewhere
# below is code that creates a filtered list of items that meet certain conditions
# refactor this code with the objective of making it more pythonic and easier to understand
# making the code more performant is not the main objective
filtered_items = []

for index in range(len(items)):

    item = items[index]

    if item.attribute_a:
        if not analysis_function(item):
            filtered_items.append(item)

    elif item.attribute_b:
        if analysis_function(item):
            filtered_items.append(item)


# my refactoring
filtered_items = []

# instead of looping through the index of the items and individually defining each item at an index point
# we can iterate directly through each item in the items container 
for item in items:

    # instead of using a nested if-statement, we can use the 'and' keyword to check that
    # both condiitons are true and then execute the action (in this case, appending) inside the expression
    if item.attribute_a and not analysis_function(item):
        filtered_items.append(item)

    # the same method can be used for the elif statement
    elif item.attribute_b and analysis_function(item):
        filtered_items.append(item)

# the code is now more concise and more readable, making it more pythonic and easier to understand, per the objective 
