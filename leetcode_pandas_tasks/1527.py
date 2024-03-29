import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    dia = patients[patients["conditions"].str.match(r'.*(^| )DIAB1.*')]
    # str.contains(r'\bDIAB1') 

    return dia 