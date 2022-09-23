# Databricks notebook source
# MAGIC %sql
# MAGIC 
# MAGIC select * from `house_sale`

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from `house_sale` where zone='南山'

# COMMAND ----------

# MAGIC %sql
# MAGIC select zone, sum(built_in_area)  from house_sale group by zone

# COMMAND ----------


