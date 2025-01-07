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

# Function to set background and font colors
def style_black_and_yellow(value):
    return "background-color: black; color: yellow;"

# Apply the style
df_styled = df.style.map(style_black_and_yellow)

# Display the styled DataFrame (will work in Jupyter Notebook or similar environments)
df_styled
