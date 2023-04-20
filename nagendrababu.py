from awsglue.transforms import *

#Orders Tranformation
def tansform(df):
  df = SelectFields.apply(df, paths=['ordsss','purch_amt']) 
  return df