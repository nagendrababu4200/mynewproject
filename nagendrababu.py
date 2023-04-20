from awsglue.transforms import *

#Orders Tranformation
def tansform(df):
  df = SelectFields.apply(df, paths=['ord_no','purch_amt']) 
  return df