from airflow.providers.ssh.operators.ssh import SSHOperator

run_command = SSHOperator(
    task_id='run_command',
    ssh_conn_id='my_ssh_connection',
    command='echo "Hello, world!"',
    dag=my_dag,
)