import pandas as pd
import numpy as np
import random

# Create a DataFrame with random values
data = {
    "Column1": [random.randint(1, 100) for _ in range(10)],
    "Column2": [random.randint(1, 100) for _ in range(10)],
    "Column3": [random.randint(1, 100) for _ in range(10)],
    "Column4": [random.randint(1, 100) for _ in range(10)]
}
df = pd.DataFrame(data)

# Convert some values to NaN
df.iloc[2, 1] = np.nan
df.iloc[5, 3] = np.nan
df.iloc[8, 0] = np.nan

# Function to highlight NaN values
def highlight_nan(value):
    if pd.isna(value):
        return "background-color: yellow"
    return ""

# Apply the function using Styler.map
df_styled = df.style.map(highlight_nan)

# Display the styled DataFrame (will work in Jupyter Notebook or similar environments)
df_styled
