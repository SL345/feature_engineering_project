# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(housing_data):
    housing_data.dropna(axis=0,how='any',inplace=True)
    without_out = housing_data[housing_data.MasVnrArea < housing_data.MasVnrArea.quantile(.95)]
    return without_out

