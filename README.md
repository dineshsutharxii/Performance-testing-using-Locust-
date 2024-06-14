# Performance Testing with Locust and Python

Welcome to the Performance Testing with Locust and Python repository! This repository contains scripts and configurations for conducting performance testing using [Locust](https://locust.io/), an easy-to-use, distributed, user load testing tool written in Python.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Locust](https://locust.io/)

## Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/dineshsutharxii/Performance-testing-using-Locust-.git
    cd Day1
    ```

2. **Install the required Python packages**

    It's recommended to use a virtual environment to manage dependencies. You can use `venv` for this purpose.

    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

## Usage

1. **Define your Locust tasks**

    Edit the `locust_python_day1.py` to define the behavior you want to test. The file contains example tasks and setup configurations.

2. **Run Locust**

    You can start Locust in standalone mode or in distributed mode. 

    - **Standalone mode**

        ```sh
        locust -f locustfile.py
        ```

        Open your browser and navigate to `http://localhost:8089` to start the test.

    - **Distributed mode**

        Start a master node:

        ```sh
        locust -f locustfile.py --master
        ```

        Start worker nodes:

        ```sh
        locust -f locustfile.py --worker --master-host=127.0.0.1
        ```

        Open your browser and navigate to `http://localhost:8089` to start the test.

3. **Monitor and Analyze Results**

    Once the tests are running, you can monitor real-time metrics such as the number of requests per second, response times, and failure rates on the Locust web interface. After the test is complete, you can download the test results for further analysis.

---

Happy Testing!