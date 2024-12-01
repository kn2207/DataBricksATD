-- Databricks notebook source
create table Employee
(id int, name string, sal double);

-- COMMAND ----------

select * from employee;

-- COMMAND ----------

insert into employee
values
(1, "Kamal", 100),
(2, "Sindhu", 100),
(3, "Kutties", 10000000),
(4, "Babaji", 1000000000000)

-- COMMAND ----------

describe detail employee

-- COMMAND ----------

-- MAGIC %fs ls 'dbfs:/user/hive/warehouse/employee'

-- COMMAND ----------

describe history employee;

-- COMMAND ----------

select * from employee;

-- COMMAND ----------

update employee set sal = 100000 where name like 'K%';

-- COMMAND ----------

describe detail employee;

-- COMMAND ----------

-- MAGIC
-- MAGIC %fs ls 'dbfs:/user/hive/warehouse/employee'
