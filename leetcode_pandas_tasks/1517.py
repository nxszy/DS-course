# https://leetcode.com/problems/find-users-with-valid-e-mails/description/

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    
    valid_users = users[users["mail"].str.match(r"^[a-zA-Z][\w\.-]*@leetcode\.com$")]

    return valid_users