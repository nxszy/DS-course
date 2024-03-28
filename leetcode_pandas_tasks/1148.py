# https://leetcode.com/problems/article-views-i/description

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    self_viewers = views[views["author_id"] == views["viewer_id"]]

    unique = self_viewers["author_id"].unique()

    return pd.DataFrame(unique, columns=["id"]).sort_values(by=["id"])