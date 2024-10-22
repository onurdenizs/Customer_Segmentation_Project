# tests/test_categorical_encoding.py

import pandas as pd
from scripts.data_exploration import encode_categorical

def test_encode_categorical():
    # Mock dataset with a categorical 'Genre' column
    data = {'CustomerID': [1, 2, 3],
            'Genre': ['Male', 'Female', 'Male'],
            'Age': [25, 32, 47]}
    
    df = pd.DataFrame(data)
    
    # Encode the 'Genre' column
    df_encoded = encode_categorical(df, 'Genre')
    
    # Check that the 'Genre' column has been replaced by numerical columns
    assert 'Genre' not in df_encoded.columns
    assert 'Genre_Male' in df_encoded.columns
    assert 'Genre_Female' in df_encoded.columns
    assert df_encoded.shape[1] == 4  # 3 original columns + 2 encoded

