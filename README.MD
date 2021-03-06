
<h1>Docker: Airflow and PostgreSQL</h1>

<h2>Enviroment:</h2>

  - macOs Big Sur 11.3.1.
  - Docker version 20.10.16.
  - Docker compose version v2.6.0.

<h3>A. Project structure</h3>

+ <strong>docker-compose.yml</strong>: including 4 main services and others
    + postgres (image <strong>postgres:9.6</strong>): Database X, init POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB and data sample.
    + postgresy (image <strong>postgres:9.6</strong>): Database Y, init POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB.
    + webserver (image <strong>apache/airflow:2.3.2</strong>): airflow webserver, connect with Database X. Expose port 8080 to 5884.
    + pgadmin4 (image <strong>pgadmin</strong>): web UI for inspecting Database X & Y.
    + others (redis, airflow-init,...): dependencies of airflow. 
  
+ <strong>db/init.sql</strong>: init table and data sample when creating Database X container.

+ <strong>dags/</strong>: predefined DAGs. Mapping from local folder to /opt/airflow/dags folder. There are two dags:
    + scenario_insert_only: in case that X has only insertion queries, not update. Python script queries only newest rows that be in X but not in Y and insert them to Y.
    + scenario_restore: in case that X has both insertion and updating queries. Python script truncates Y and query all rows of X, then writes to Y.

+ <strong>dags/script/</strong>: python scripts to connect, query and update data on postgre Database X & Y. DAGs will run these scripts.

+ <strong>logs/, plugins/</strong>: init folder for airflow.
  
<h3>B. Running flow</h3>

<ol>
  <li>Clone this repo and <code>cd</code> into <strong>airflow-docker</strong> folder.</li>

  &nbsp;
  <li>Run command: <code>docker-compose up -d</code></li>
  Wait a minute until all containers alread started. 

  &nbsp;
  <li>Go to <strong>localhost:1234</strong>. Login with user: 'huy@gmail.com' and password: 'postgres'.</li>
  <img src="./images/2.png" style="height: 300px; width: 600px;"/>
  <img src="./images/3.png" style="height: 300px; width: 600px;"/>

  &nbsp;
  <li>Add new server connection for Postgre Database X & Y.</li>
  a. Database name, Username and Password all are 'airflow' for X and 'airflowy' for Y.
  <img src="./images/4.png" style="height: 300px; width: 600px;"/>
  <img src="./images/5.png" style="height: 300px; width: 600px;"/>

  &nbsp;

  b. Query table 'transactions' in X and Y.
  <img src="./images/6.png" style="height: 300px; width: 600px;"/>
  <img src="./images/7.png" style="height: 300px; width: 600px;"/>

  &nbsp;
  <li>Go to <strong>localhost:5884</strong>. Login with user: 'airflow' and password: 'airflow'.</li>
  <img src="./images/8.png" style="height: 300px; width: 600px;"/>

  &nbsp;
  <li>Trigger DAGs.</li>

  Turn on task:

  &nbsp;
  <img src="./images/9.png" style="height: 300px; width: 600px;"/>
  
  &nbsp;

  Trigger manual:

  <img src="./images/10.png" style="height: 300px; width: 600px;"/>

  &nbsp;

  Refresh and wait until task sucessful:

  <img src="./images/11.png" style="height: 300px; width: 600px;"/>

  &nbsp;
  
  <li>Query DB Y again. Data in table transactions of X are transered to Y.</li>
  <img src="./images/12.png" style="height: 300px; width: 600px;"/>

  &nbsp;

  <li>Run command: <code>docker-compose stop</code> to stop.</li>
</ol>

<h2>End.</h2>
