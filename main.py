from engine import QuantaFlowEngine
import pandas as pd
import numpy as np

# 1. Create a quick "Dirty" CSV for testing
data = {
    'Marks': [85, 90, np.nan, 70, 5000], 
    'City': ['Delhi', np.nan, 'Mumbai', 'Delhi', 'Mumbai']
}
pd.DataFrame(data).to_csv("my_test_data.csv", index=False)

# 2. Run Quanta-Flow
qf = QuantaFlowEngine("my_test_data.csv")
qf.auto_audit()
qf.smart_impute()
qf.remove_outliers('Marks')
qf.encode_categorical('City')
print("--- Quanta-Flow Success! ---")
print(qf.get_final_report())
print("---Cleaned Data Preview---")
print(qf.df.head())