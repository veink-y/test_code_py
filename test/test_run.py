# Databricks notebook source

print("test_run hello world")

# COMMAND ----------

print("test_run hello world command 2")

# COMMAND ----------

import json
with open("test_json.json") as f:
    test_json = json.loads(f.reads())
    print(test_json)

# COMMAND ----------

if __name__ == "__main__":
    print("main test_run")
