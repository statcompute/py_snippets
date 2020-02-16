### Define Context ###

In [1]: from pandas import read_csv, DataFrame
In [2]: from pyspark import sql
In [3]: from pysparkling import H2OContext
In [4]: from h2o import import_file, H2OFrame 
In [5]: ss = sql.SparkSession.builder.getOrCreate()
In [6]: hc = H2OContext.getOrCreate(ss)
