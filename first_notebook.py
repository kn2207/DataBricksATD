# Databricks notebook source
print("hello babaji")

# COMMAND ----------

print("I am in 2nd cell")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "hello SQL babaji!"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #First
# MAGIC ##Second Title Type
# MAGIC ### Third Title Type
# MAGIC
# MAGIC text with **bold** and _italized_ is possible in the world
# MAGIC
# MAGIC Ordered List
# MAGIC 1. Kamal
# MAGIC 2. Sindhu
# MAGIC
# MAGIC Unordered List
# MAGIC - Ram
# MAGIC - Lakshmana
# MAGIC - Sita
# MAGIC - Hanuma
# MAGIC
# MAGIC
# MAGIC ![Image of databricks:](https://www.databricks.com/en-website-assets/static/531affffa2d178e994293dbbfabc1289/27289.png)
# MAGIC
# MAGIC | Emp | Dept|
# MAGIC |-----| ----|
# MAGIC |Kamal|Finance|
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %run ./Setup

# COMMAND ----------

print(name)

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %fs ls 'databricks-datasets/'

# COMMAND ----------

dbutils.fs.ls('databricks-datasets/')

# COMMAND ----------

data = dbutils.fs.ls('databricks-datasets/')
display(data)
