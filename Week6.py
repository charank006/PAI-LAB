from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
})

# Define Bayesian Network structure
model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('TrafficJam', 'ArriveLate')
])

# Fit model (learn CPDs)
model.fit(data)

# Print CPDs
print("Conditional Probability Distributions:\n")
for cpd in model.get_cpds():
    print(cpd)
    print()

# Inference
inference = VariableElimination(model)

query_result = inference.query(
    variables=['ArriveLate'],
    evidence={'Rain': 'Yes'}
)

print("Inference Result (P(ArriveLate | Rain=Yes)):\n")
print(query_result)