FROM apache/airflow:3.4.0

USER root

RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean

USER airflow

COPY pipeline/requirements.txt /tmp/requirements.txt
COPY simulator/requirements.txt /tmp/simulator_requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/simulator_requirements.txt