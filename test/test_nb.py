# Databricks notebook source

# MAGIC %run test_run

# COMMAND ----------

print("hello world")

# COMMAND ----------

print("hello world command 2")

# COMMAND ----------

import json
with open("test_json.json","r") as f:
    test_json = json.loads(f.read())
    print(test_json)

# COMMAND ----------

if __name__ == "__main__":
    print("main")
