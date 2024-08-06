# Backend du site de l'EPL

Brief description of the project.

## Features

- Informational support on the institutional structure and organization
- Informational support on training programs and courses
- Informational support on recruitment procedures and competitions
- Informational support on campus life and activities
- Informational support on national and international academic partners
- Informational support on national and international business partners
- Informational support on research, innovation, transfer, and services
- Access to an extranet space reserved for internal resources
- Interface for dialogue and sharing of experiences or testimonials with mobility students (blog and forums)
- Interface for collecting data from new candidates (contact form)
- Shared calendar management, including group calendar management via email or in collaboration with telecom operators (via SMS)
- Back office for monitoring site activities (retrieving forms, updating mailing lists, uploading documents and partner resources, etc.)
- Integration with third-party systems (EPL social media accounts)
- Email messaging for EPL staff (management of EPL accounts)
- Directory, internal help desk

## Prerequisites

- Python 3.8+
- PostgreSQL
- [Poetry](https://python-poetry.org/)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kekelidiane/Backend_site.git
    cd Backend_site
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows: `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    Or, if you use Poetry:
    ```sh
    poetry install
    ```

4. Configure the environment variables. Create a `.env` file at the root of the project and add the following variables:
    ```env
    DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
    ```

5. Initialize the database:
    ```sh
    alembic upgrade head
    ```

## Starting the Server

To start the development server:
    ```sh
    uvicorn app.main:app --reload
    ```

## Running Tests

To run the tests, use:
    ```sh
    pytest
    ```

## Project Structure

Project referral

## API Documentation

To access the interactive API documentation, start the server and open your browser at the following addresses:

- Swagger documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Contributing

Contributions are welcome! Please read the `CONTRIBUTING.md` file for details on our code of conduct and the process for submitting pull requests.

## License

Not yet 