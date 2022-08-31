# hermes_api
Microservice to consume Domestic Airports API and Mock Airlines Inc API to return the available flights per date, city of origin and destiny and also return the prices and kilometers of flights.

resource = https://gist.github.com/vitorfavila/6c0fc484b4f55101cbd75074c6fd3573

<hr>

<p align="center">
  <a href="#projeto">About the project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">How to install</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#execução">How to execute it</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#response">Response</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#testes">API TESTS</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
</p>

## <a id="projeto"> 💻 ABOUT THE PROJECT </a>

Microservice to consume Domestic Airports API and Mock Airlines Inc API to return the available flights per date, 
city of origin and destiny and also return the prices and kilometers of flights..

Some functionalities present on this project:

    * TO BE INCLUDED

<br>

🟩 PROJECT STATUS: <b>IN PROGRESS</b> <br>

<hr>

## <a id="tecnologias"> 🧪 TECHNOLOGIES </a>

- Python 
- FLASK
- Pymongo
- API Consumer
- Pytest
- Mutation Tests

<hr>

## <a id="instalacao"> HOW TO INSTALL IT </a> 

<b>- Clone the repo with the following command:</b> `https://github.com/renatamoon/hermes_api.git` <br>

<hr> 

#### On Windows

<b>- Create your virtual environment:</b> `python -m venv venv`<br>
<b>- Activate your virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: If for any reason occurs and error:</b> on powershell execute the following command: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>- Execute requirements with the command: </b>`pip install -r requirements.txt`<br>

<hr> 

#### On Linux:

<b>- Create your virtual environment:</b> `python -m venv venv`<br>
<b>- Activate your virtual environment:</b> `source venv/bin/activate`<br>
<b>- Execute requirements with the command:</b> `pip install -r requirements.txt`<br>

<hr>

Create a project root `.env` file and change your local strings connections to do the properly connection <br>

```commandline
ENV KEYS TO BE INFORMED
```

<hr>

## <a id="execução"> EXECUTE HYPERCORN </a> 

- To Execute the application run the command: `uvicorn main:app --reload` or manually run the `main.py` file.

<hr>

## <a> REQUISITION ROUTER </a> 

- Use the router on your Postman/Insomnia: `http:{your-host}/to_be_informed` ;

## <a> QUERY PARAMS </a> 

- search ... : `....`
- search ... : `...`

<hr>

## <a id="response"> API RESPONSES: </a> 

- Expected return of the route `/to_be_informed` when passing `...` query param:
```
response = {}
```
- Example of expected response of the route when an error happened:

```
{
    "to be posted"
}

```

## <a id="testes"> API TESTS: </a> 

- To get the coverage of the project tests run the command on root path: `pytest --cov-report term-missing --cov-config=.coveragerc --cov=src -v`
- To run the mutatest and get the mutants survivor tolerance, run the command on root path: `bash mutation_test.sh`

- <b>Coverage: </b>
<br>

- <b>Mutation Survivor Tolerance: </b>
