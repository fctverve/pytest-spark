# Run like this:
# PYTEST_SPARK_JARS=etc/pytest-spark-jars-example.jar pytest --spark_home=$SPARK_HOME test/test_spark_jars.py

def test_spark_session_java_function(spark_session):
	from pyspark.sql.types import IntegerType

	spark_session.udf.registerJavaFunction("JavaStringLength", "pytest.spark.jars.example.StringLength", IntegerType())
	assert spark_session.sql("SELECT JavaStringLength('hello') AS length").head().length == 5

	spark_session.stop()

def test_spark_context_java_function(spark_context):
	from pyspark.sql import SQLContext
	from pyspark.sql.types import IntegerType

	sqlContext = SQLContext(spark_context)
	sqlContext.registerJavaFunction("JavaStringLength", "pytest.spark.jars.example.StringLength", IntegerType())
	assert sqlContext.sql("SELECT JavaStringLength('hello') AS length").head().length == 5

	spark_context.stop()