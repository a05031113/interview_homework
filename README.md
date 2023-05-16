# qsearch

## 1.

```python
def calculator(input):
    input = input.replace(" ", "")

    operands = []
    operators = []

    def apply_operator():
        operator = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            result = operand1 / operand2
        operands.append(result)

    index = 0
    while index < len(input):
        if input[index].isdigit():
            start = index
            while index < len(input) and input[index].isdigit():
                index += 1
            operand = int(input[start:index])
            operands.append(operand)
        elif input[index] in "+-*/":
            while operators and operators[-1] in "*/":
                apply_operator()
            operators.append(input[index])
            index += 1
        elif input[index] == "(":
            operators.append(input[index])
            index += 1
        elif input[index] == ")":
            while operators and operators[-1] != "(":
                apply_operator()
            operators.pop()
            index += 1
        else:
            index += 1

    while operators:
        apply_operator()

    return operands[0]

```

Or used eval():

```python
def calculator(a):
    return eval(a)
```

## 2.

API handling function is in /application/controller/api.py  
Use query string to get PNG. e.g: http://34.125.91.37:3000/api/image?height=500&width=500

## 3.

Google Cloud logging
https://cloudlogging.app.goo.gl/4eLwTpDSEybfea8y9

## 4.

```
python3 -m pytest
```

## 5.

Function to send request to GA4 Measurement Protocol

```python
def track_api_execution():
    api_secret = os.getenv("api_secret")
    measurement_id = "G-CRTZZ2HL4S"
    url = 'https://www.google-analytics.com/mp/collect?measurement_id=' + \
        api_secret+'&api_secret='+measurement_id

    payload = {
        'client_id': uuid.uuid4(),
        'events': [{
            'name': 'qsearch',
            'params': {}
        }]
    }
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code != 200:
        print('Failed to send API execution data to Google Analytics.')
```

## 6.

- RDB

  - Advantage:
    1. Structured data: RDB organizes data in tables with rows and columns, making it suitable for structured data.
    2. ACID properties: RDB follows ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring transactional integrity.
    3. Data consistency: RDB enforces integrity constraints such as primary keys and foreign keys, ensuring data consistency.
    4. Powerful query performance: RDB's SQL query engine is typically optimized for complex queries and can efficiently execute them.
  - Disadvantage:
    1. Static schema: RDB requires defining the structure and relationships of tables during the design phase, making it less flexible when modifying the schema.
    2. Limited scalability: RDB may have limitations in handling large-scale data or high concurrency situations, requiring sharding or vertical partitioning for scalability.
    3. Higher cost: RDB's strict data modeling and integrity constraints can result in higher development and maintenance costs.

- NoSQL DB
  - Advantage:
    1. Flexible data model: NoSQL databases offer various data models (document, key-value, column, graph) to choose from based on the application's requirements.
    2. High scalability: NoSQL databases are designed for scalability, easily handling large-scale data and high concurrency through horizontal scaling.
    3. High performance: NoSQL databases often provide high performance for quick read and write operations, meeting the needs of certain applications.
    4. High availability: NoSQL databases typically support features like master-slave replication or distributed architectures, ensuring high availability and fault tolerance.
  - Disadvantage:
    1. Weaker consistency: NoSQL databases may sacrifice strong consistency for high performance and scalability, making them less suitable for applications requiring strict consistency.
    2. Learning curve: Due to the diverse data models and features, developers need to learn different APIs and query languages for different NoSQL databases.
    3. Weaker query capabilities: Compared to the SQL query engines of RDB, NoSQL databases may have weaker query capabilities, especially for complex relational queries.

## 7.

- Internet
  - How does the Internet work? Basic understand
  - What is HTTP? Understand
  - Browsers and how they work? Not really understand
  - DNS and how it works? Basic understand
  - What is Domain Name? Basic understand
  - What is hosting? Not really
- Learn a Language
  - Python
  - Go
  - JavaScript
- Version Control Systems
  - Git
- Repo hosting services
  - GitHub
- OS and General Knowledge
  - Terminal Usage
  - Basic Terminal Commands
- Relational Databases
  - MySQL
- NoSQL Databases
  - MongoDB
  - Redis
- More about Databases
  - ORMs
  - ACID
  - Transactions
- Scaling Databases
  - Database Indexes
- Learn about APIs
  - Authentication
    - Cookie Based
    - Token Auth
    - JWT
  - REST
- Caching
  - Redis
- Web Security Knowledge
  - HTTPs
  - CORS
  - SSL/TLS
- Testing
  - Unit Testing
- CI/CD basic understand
- Containerization vs Virtualization
  - Docker
- WebSocket
- Web Servers
  - Nginx
