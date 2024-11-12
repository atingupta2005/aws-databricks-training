# Example Model Training Notebook for Databricks

from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import VectorAssembler

df = spark.read.parquet("s3://your-bucket-name/processed-data/")
assembler = VectorAssembler(inputCols=['feature1', 'feature2'], outputCol='features')
df_transformed = assembler.transform(df)

rf = RandomForestClassifier(labelCol="label", featuresCol="features")
model = rf.fit(df_transformed)

model.save("s3://your-bucket-name/model/")
