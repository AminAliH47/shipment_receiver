# Shipment receiver project

In this project, you can see and filter the shipping list and its articles.

**Requirement**:

To run this project, you need **Docker** on your OS and a **HTTP Proxy.**

## Running project

First, you clone the project from Git.

### Create .env file

Then you create the `.env` file in the main root of the project and fill in the values from the example below:

```
VERSION=0.1.0
DEBUG=True
TZ=Asia/Tehran

POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=shipments
POSTGRES_USER=amin
POSTGRES_PASSWORD=123456@Aa

REDIS_HOST=redis
REDIS_PORT=6379

WEATHER_API_URL=https://api.tomorrow.io/
WEATHER_APIKEY=K02qYOgr8eYlwl0p11OxD6sbmoKBzfeW

HTTP_PROXY=
```

Set `HTTP_PROXY` value equal to your http proxy.
**We do this so that we can install pip packages.**

### Run project

After that you should run `docker compose build` in the terminal.

Then, type the command `docker compose up -d` in the terminal.

**Our project is running now.**

### Load CSV data

Now we need to enter the data of the CSV file into the database.

To do this, just enter the `docker compose run load_data` command in your terminal.

### Test project

You can now testing project.

Just import the following cURL command into your Postman:

```cURL
curl --location 'http://127.0.0.1:9001/api/v1/shipments/?tracking_number=TN12345678&carrier=DHL'
```

Also, to test your project, you can enter `docker compose run test` command in your terminal so that automatic tests will be run for you.
