import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Example transaction data
transactions = [
    ['bread', 'milk', 'beer'],
    ['bread', 'diapers', 'eggs'],
    ['milk', 'diapers', 'beer', 'cola'],
    ['bread', 'milk', 'diapers', 'beer'],
    ['bread', 'milk', 'diapers', 'cola']
]

# Convert the transaction data to a one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Use Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)

# Define a custom Confidence Difference Criterion
confidence_difference_threshold = 0.1
filtered_rules = rules[abs(rules['confidence'] - rules['confidence_lag']) > confidence_difference_threshold]

# Display the filtered association rules based on the custom criterion
print("Filtered Association Rules:")
print(filtered_rules)
