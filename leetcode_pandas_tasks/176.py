# https://leetcode.com/problems/second-highest-salary/

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    unique_salaries = employee["salary"].drop_duplicates()

    if len(unique_salaries) >= 2:
        second_highest = unique_salaries.sort_values(ascending=False).iloc[1]
    else:
        second_highest = None
        
    result = pd.DataFrame({"SecondHighestSalary": [second_highest]})
    
    return result