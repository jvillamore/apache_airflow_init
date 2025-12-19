import airflow.providers.postgres.operators.postgres import PostgresOperator

populate_pet_table = PostgresOperator(task_id="populate_pet_table",
                                      postgres_conn_id="my_postgres_connection",
                                      sql="sql_/pet_table.sql")
