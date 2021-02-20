import pandas as pd

from unidata.wall_e import CleanDataFrame
from unidata.wall_e import CleanText

data_test = {"Name":['"#11$@@!!><? AB "', "CD"], "Age":["AB", "CD"] }

df = pd.DataFrame(data=data_test)
print(df)

df = CleanDataFrame.change_to_lowercase(df, "Name")
df = CleanDataFrame.remove_double_quote(df, "Name")
df = CleanDataFrame.remove_special_character(df, "Name")
df = CleanDataFrame.remove_digit(df, "Name")
df = CleanDataFrame.remove_space(df, "Name")
print(df)

test_text = ' #$$22ceAA<<>> " '

test_text = CleanText.change_to_lowercase(test_text)
test_text = CleanText.remove_double_quote(test_text)
print(test_text)

