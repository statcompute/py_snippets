### Define Context ###

In [1]: from pandas import read_csv, DataFrame
  
In [2]: from pyspark import sql

In [3]: from pysparkling import H2OContext
  
In [4]: from h2o import import_file, H2OFrame 
  
In [5]: ss = sql.SparkSession.builder.getOrCreate()
  
In [6]: hc = H2OContext.getOrCreate(ss)

### Convert Pandas Dataframe to H2OFrame and Spark DataFrame ###

In [7]: p_df = read_csv("Documents/credit_count.txt")
 
In [8]: type(p_df)
Out[8]: pandas.core.frame.DataFrame
 
In [9]: p2s_df = ss.createDataFrame(p_df)
 
In [10]: type(p2s_df)
Out[10]: pyspark.sql.dataframe.DataFrame
 
In [11]: p2h_df = H2OFrame(p_df)
 
### Convert Spark Dataframe to H2OFrame and Pandas DataFrame ###

In [13]: s_df = ss.read.csv("Documents/credit_count.txt", header = True, inferSchema = True)
 
In [14]: type(s_df)
Out[14]: pyspark.sql.dataframe.DataFrame
 
In [15]: s2p_df = s_df.toPandas()
 
In [16]: type(s2p_df)
Out[16]: pandas.core.frame.DataFrame
 
In [17]: s2h_df = hc.as_h2o_frame(s_df)
 
In [18]: type(s2h_df)
Out[18]: h2o.frame.H2OFrame
  
### Convert H2OFrame to Pandas Dataframe and Spark DataFrame ###

In [19]: h_df = import_file("Documents/credit_count.txt", header = 1, sep = ",")
 
In [20]: type(h_df)
Out[20]: h2o.frame.H2OFrame
 
In [21]: h2p_df = h_df.as_data_frame()
 
In [22]: type(h2p_df)
Out[22]: pandas.core.frame.DataFrame
 
In [23]: h2s_df = hc.as_spark_frame(h_df)
 
In [24]: type(h2s_df)
Out[24]: pyspark.sql.dataframe.DataFrame

In [12]: type(p2h_df)
Out[12]: h2o.frame.H2OFrame
