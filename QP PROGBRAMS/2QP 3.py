import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    "Column1": [10, 20, np.nan, 40, 50],
    "Column2": [np.nan, 22, 33, 44, np.nan],
    "Column3": [np.nan, 25, 35, 45, 55]
}
df = pd.DataFrame(data)

# Detect missing values
missing_values = df.isnull()

# Display the DataFrame with True for missing values and False otherwise
print("Missing Values Detection:")
print(missing_values)
