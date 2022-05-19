import pandas as pd
from crawler import titles,urls,contents

df = pd.DataFrame(zip(titles,contents,urls), columns=["title","content","link"])
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)