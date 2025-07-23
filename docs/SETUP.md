# Developer Setup Guide - project-develop-a-financial

This guide outlines the setup process for developers working on `project-develop-a-financial`, a financial services platform.  We recommend using Docker for development, but native setup instructions are also provided.

## Prerequisites

* **Required Software Versions:**
    * Python 3.9+
    * Node.js 16+
    * PostgreSQL 14+ (or compatible database)
    * Docker Desktop (for Docker option)
    * Docker Compose (for Docker option)

* **Development Tools:**
    * Git
    * Text editor or IDE (see recommendations below)

* **IDE Recommendations and Configurations:**
    * **VS Code:**  Highly recommended due to its excellent extension support for Python, JavaScript, and debugging. Install extensions like "Python," "Prettier," "ESLint," and "Docker."
    * **PyCharm:** A powerful Python IDE with good debugging capabilities.  Requires configuration for JavaScript/frontend tools.
    * **WebStorm:** A robust JavaScript IDE, ideal if frontend development is your primary focus.


## Local Development Setup

### Option 1: Docker Development (Recommended)

1. **Clone Repository:**
   ```bash
   git clone <repository_url>
   cd project-develop-a-financial
   ```

2. **Docker Setup:** Ensure Docker Desktop and Docker Compose are installed and running.

3. **Development Docker-Compose Configuration:** The project should contain a `docker-compose.yml` file. This file defines the services (database, backend, frontend) and their configurations.  A sample might look like this:

   ```yaml
   version: "3.9"
   services:
     db:
       image: postgres:14
       environment:
         - POSTGRES_USER=your_db_user
         - POSTGRES_PASSWORD=your_db_password
         - POSTGRES_DB=your_db_name
       ports:
         - "5432:5432"
     backend:
       build: ./backend
       ports:
         - "8000:8000"
       depends_on:
         - db
       environment:
         - DATABASE_URL=postgres://your_db_user:your_db_password@db:5432/your_db_name
     frontend:
       build: ./frontend
       ports:
         - "3000:3000"
       depends_on:
         - backend
   ```

4. **Hot Reload Setup:**  The `docker-compose.yml` should include configurations for hot reloading (e.g., using nodemon for the frontend).  This will automatically rebuild and restart the frontend when you make code changes.

5. **Build and Start:**
   ```bash
   docker-compose up -d --build
   ```


### Option 2: Native Development

1. **Backend Setup:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   ```

3. **Database Setup:** Install PostgreSQL. Create a database using the `psql` command-line tool:
   ```sql
   CREATE DATABASE your_db_name;
   CREATE USER your_db_user WITH PASSWORD 'your_db_password';
   GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
   ```


## Environment Configuration

* **Required Environment Variables:**  The `.env` file (or equivalent) should contain variables like:
    * `DATABASE_URL`:  Connection string to the database.
    * `SECRET_KEY`:  A secret key for security.
    * `API_KEY`:  For third-party API integrations (market data).
    * `DEBUG`:  Set to `true` for development, `false` for production.

* **Local Development .env File Setup:** Create a `.env` file in the root directory with the necessary variables.  **Never commit this file to version control.** Add `.env` to your `.gitignore`.

* **Configuration for Different Environments:**  Use environment variables to manage settings for different environments (development, staging, production).


## Running the Application

* **Start Commands:**
    * **Docker:** `docker-compose up -d --build`
    * **Native:**  Start the backend server (e.g., `python manage.py runserver` if using Django) and the frontend development server (e.g., `npm start`).

* **Access Frontend and Backend:**  The frontend will be accessible at `http://localhost:3000` (or the port specified in `docker-compose.yml` or your setup).  The backend API will be accessible at `http://localhost:8000` (or its specified port).

* **API Documentation Access:**  Use tools like Swagger UI or Postman to explore the API.


## Development Workflow

* **Git Workflow and Branching Strategy:** Use Gitflow or a similar branching strategy (e.g., feature branches for new features, hotfix branches for urgent bug fixes).

* **Code Formatting and Linting Setup:**  Use tools like `black` (Python) and `prettier` (JavaScript) for code formatting and linters like `flake8` (Python) and `eslint` (JavaScript) to catch potential issues.

* **Testing Procedures:** Write unit tests for individual components and integration tests for interactions between components.  Use a testing framework like `pytest` (Python) and `Jest` (JavaScript).

* **Debugging Setup:** Use your IDE's debugging tools.


## Database Management

* **Running Migrations:** Use database migration tools (e.g., Alembic for SQLAlchemy) to manage schema changes.

* **Seeding Development Data:** Create scripts to populate the database with sample data for development.

* **Database Reset Procedures:**  Include scripts to easily reset the database to a clean state.


## Testing

* **Running Unit Tests:**  Execute unit tests using the chosen testing framework (e.g., `pytest` or `Jest`).

* **Running Integration Tests:**  Run integration tests to verify interactions between different parts of the application.

* **Test Coverage Reports:** Generate test coverage reports to track the percentage of code covered by tests.


## Common Development Tasks

* **Adding New API Endpoints:**  Follow the established API design and coding conventions.  Write unit and integration tests.

* **Adding New Frontend Components:**  Use a component-based architecture.  Ensure components are well-tested.

* **Database Schema Changes:**  Use migrations to manage schema changes.  Update related code accordingly.

* **Adding Dependencies:**  Add dependencies to the appropriate `requirements.txt` (backend) or `package.json` (frontend) file.


## Troubleshooting

* **Common Setup Issues:** Check the logs for error messages.  Ensure all dependencies are installed correctly.

* **Port Conflicts Resolution:** Change port numbers in the configuration files if there are conflicts.

* **Dependency Issues:**  Use a virtual environment (Python) and package manager (npm) to manage dependencies.

* **Environment Variable Problems:**  Double-check that the environment variables are set correctly and accessible.


## Contributing

* **Code Style Guidelines:** Adhere to the established code style guidelines (e.g., PEP 8 for Python).

* **Pull Request Process:** Create pull requests for code changes.  Ensure code is reviewed and tested before merging.

* **Issue Reporting:**  Report issues using the project's issue tracker.  Provide detailed descriptions and reproduction steps.


This guide provides a solid foundation for setting up your development environment. Remember to consult the project's specific documentation for detailed instructions and best practices.  Good luck!
