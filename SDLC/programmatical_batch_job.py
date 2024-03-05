# import pandas as pd
# import pytorch
# import matplotlib.pyplot as plt
from dt.scheduler.api import DAG, Schedule, Task

REPORT_NAMES = {'repo', 'fi_us', 'db_cd'}

with DAG(Name='Daily Reports', Tag='dev', Schedule=Schedule(at_minutes=[15], at_hours=[0])) as dag:
    create_reports = [
        Task(
            Name=f'create–{report}', 
            Image='reports image', 
            ConfigurationJson={'report_name': report_name},
            dag=dag,
            Entrypoint='reports.batch.report'
        ) 
        for report_name in REPORT_NAMES
    ] 
    publish_reports = Task(
        Name='publish', 
        Image='reports image', 
        dag=dag,
        Entrypoint='reports.batch.report'
    ) 
    create_reports >> publish_reports
    dag.save()
