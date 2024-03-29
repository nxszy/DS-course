# https://leetcode.com/problems/fix-names-in-a-table/description/

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    users["name"] = users["name"].apply(lambda n: n.capitalize())
    return users.sort_values(by=["user_id"])