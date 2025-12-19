from airflow.models import Variable


environment = Variable.get("environment", default_var="dev")
# foo_json = Variable.get("foo_json", deserialize_json=True)
print(f"Environment: {environment}")

# Connection example (uncomment to use)
