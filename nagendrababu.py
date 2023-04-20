from awsglue.transforms import *

#Orders Tranformation
def tansform(df):
  df = SelectFields.apply(df, paths=['ord','purch_amt']) 
  return df