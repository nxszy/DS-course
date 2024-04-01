# https://leetcode.com/problems/rank-scores/description/ 

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    
    scores.sort_values(by="score",inplace=True,ascending=False)
    scores['rank']=(scores["score"].rank(method="dense",ascending=False).astype(int))
    return scores[['score','rank']]
