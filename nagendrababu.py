from awsglue.transforms import *

#Orders Tranformation
def tansform(df):
  df = SelectFields.apply(df, paths=['baaaaSbu','purch_amt']) 
  return df