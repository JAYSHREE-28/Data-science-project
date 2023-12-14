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

# Define a custom Confidence Quotient Criterion
confidence_quotient_threshold = 2.0  # Adjust based on your specific definition

# Calculate the Confidence Quotient for each rule
rules['confidence_quotient'] = rules['confidence'] / rules['antecedent support']

# Filter rules based on the custom Confidence Quotient Criterion
filtered_rules = rules[rules['confidence_quotient'] > confidence_quotient_threshold]

# Display the filtered association rules based on the custom criterion
print("Filtered Association Rules:")
print(filtered_rules)
