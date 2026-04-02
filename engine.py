import pandas as pd
import numpy as np

class QuantaFlowEngine:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.report = []

    def auto_audit(self):
        """Scans the data for issues."""
        null_counts = self.df.isnull().sum()
        self.report.append(f"Audit Complete: Found {null_counts.sum()} missing values.")
        return null_counts

    def smart_impute(self):
        """Automatically fills missing data."""
        for col in self.df.columns:
            if self.df[col].isnull().sum() > 0:
                if self.df[col].dtype in ['int64', 'float64']:
                    # Fill numbers with Median
                    self.df[col] = self.df[col].fillna(self.df[col].median())
                    self.report.append(f"Fixed {col}: Used Median")
                else:
                    # Fill text with Mode
                    self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
                    self.report.append(f"Fixed {col}: Used Mode")
        return self.df

   
    # ... previous functions (auto_audit, smart_impute) are above ...

    def remove_outliers(self, column):
        """Removes values that are mathematically too far from the average."""
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        before = len(self.df)
        self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
        after = len(self.df)
        
        self.report.append(f"Outliers: Removed {before - after} rows from {column}")
        return self.df
    def encode_categorical(self, column):
        """Converts text categories into numbers (0, 1, 2...)."""
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        self.df[column] = le.fit_transform(self.df[column].astype(str))
        self.report.append(f"Encoded {column}: Converted text to numeric labels.")
        return self.df

    def get_final_report(self):
        """This remains at the very bottom as your summary tool."""
        return "\n".join(self.report)