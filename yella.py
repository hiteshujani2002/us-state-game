import  pandas as pd

data = pd.read_csv("50_states.csv")

# print(data["state"])

alaska_row = data[data["state"] == "Alaska"]
print(alaska_row['x'])
print(alaska_row['state'])

# print(alaska_row)

