import airflow
from airflow import DAG
from airflow.operators import dummy,python


my_dag = DAG("new_dag_for_DS")
op = dummy.DummyOperator(task_id="task", dag=my_dag)


