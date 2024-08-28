# Project Name: Dunnossauro FastAPI

## Description
Dunnossauro FastAPI is a fast and efficient web framework for building APIs with Python. It is designed to be easy to use, highly performant, and scalable. This project aims to provide a boilerplate template for creating FastAPI projects with best practices and common features already implemented.

## Features
- FastAPI: Utilizes the FastAPI framework for building high-performance APIs.
- SQLAlchemy: Integrates SQLAlchemy for database operations and ORM.
- JWT Authentication: Implements JWT-based authentication for secure API access.
- Docker: Provides Docker support for easy deployment and containerization.
- Testing: Includes a comprehensive testing suite using Pytest for ensuring code quality and reliability.
- Documentation: Generates API documentation automatically using Swagger UI.

## Installation
1. Clone the repository: `git clone https://github.com/ricardohsm/dunnossauro_fastapi.git`
2. Navigate to the project directory: `cd dunnossauro_fastapi`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
    - Windows: `venv\Scripts\activate`
    - Unix/Linux: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`

## Configuration
1. Rename the `.env.example` file to `.env`.
2. Open the `.env` file and update the configuration variables according to your environment.

## Usage
1. Start the application: `python main.py`
2. Access the API documentation at `http://localhost:8000/docs`.

## Testing
1. Run the test suite: `pytest`

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
