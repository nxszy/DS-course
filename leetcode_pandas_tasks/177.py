# https://leetcode.com/problems/nth-highest-salary/description/

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    unique_salaries = employee["salary"].drop_duplicates()

    if len(unique_salaries) >= N and N-1 >= 0:
        nth_highest = unique_salaries.sort_values(ascending=False).iloc[N-1]
    else:
        nth_highest = None
        
    result = pd.DataFrame({f"getNthHighestSalary({N})": [nth_highest]})
    
    return result