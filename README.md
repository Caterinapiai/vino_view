# VinoView

VinoView is a webapp built with Python, Flask, FastAPI and Docker that allows you to carry out advanced searches within a vast dataset of various types of wines from all over the world.

## Group Members
- Caterina Piai
- Beatrice Coletti
- Emma Arboit
- Veronica Farinazzo
- Giulia Magrin

## Datasets
You can find the csv files (Red.csv, Rose.csv, Sparkling.csv, White.csv) in the following link: https://www.kaggle.com/datasets/budnyak/wine-rating-and-price 

## Architecture

The project follows a client-server architecture:

- Frontend (Flask):

    Represents the user interface or client side.
    Built with Flask, a lightweight web framework for Python.
    Responsible for rendering web pages and user interactions, including the form for querying the backend.
    
- Backend (FastAPI):

    Represents the server of the application.
    Built with FastAPI, a modern web framework for building APIs with Python.
    Handles requests from the frontend, including querying the datasets and handling advanced search filters.

- Docker Compose:

    Orchestrates the deployment of both frontend and backend as separate containers.
    Ensures seamless communication between frontend and backend containers.
    Simplifies the deployment and management of the entire application.

## Usage
First of all, make sure you have Docker, docker-compose and git installed on your system.

1. Clone the repository and navigate in the directory

    ```bash
    git clone https://github.com/Caterinapiai/vino_view
    cd vino_view
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

This will start both the frontend and backend containers.

3. Open your web browser and navigate to http://localhost:8080 to access the frontend and http://localhost:8081 to access the backend.

4. Use the home page to view top-reviewed wines, newest wines, and oldest wines, or use the advanced search page to search for wines based on your preferred filters, such as type, price, rating, name, year, or country.

5. You can shut down the containers by running

    ```bash
    docker-compose down
    ```

## PEP-8 Compliance

The entire codebase is PEP-8 compliance, you can check it by using the `pycodestyle` tool from the root of the project:

```bash
pycodestyle frontend/app/
```

```bash
pycodestyle backend/app/
```

## Tests
From the **Docker `backend` container's terminal**, you can run the unit tests with the following command:

```bash
pytest --cov=app --cov-report=html tests/
```

A new folder called `htmlcov` will be created, which contains an `ìndex.html` file, which can be opened in a browser to check the coverage details (which is 100%).
