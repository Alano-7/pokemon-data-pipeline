What this is about:
This is a complete ETL pipeline built in python. This mini Pokemon pipeline project shows some data engineering skills by pulling data from an external API, process and clean it as well as automayically uploading it to MySQL

Overwiew:
This pipeline automates the process of collecting and structuring Pokémon data. It:
  *Extracts raw data from the [PokeAPI](https://pokeapi.co/).
  *Transforms the complex, nested JSON responses into a clean, table format.
  *Loads the structured data into a MySQL database for persistent storage and analysis.
  *Analyzes the dataset to very basic insights, like the strongest Pokémon.

Process Flow:
A[PokeAPI] -- Extract via Requests --> B(Raw JSON Data)
B -- Transform via Pandas --> C[Structured DataFrame]
C -- Load via SQLAlchemy --> D[(MySQL Database)]


Tech needed:
*Language: Python 3
*Libraries:
  - `requests` - API HTTP calls
  - `pandas` - Data manipulation and transformation
  - `sqlalchemy` - Database ORM and connection handling
  - `mysql-connector` - MySQL database driver
 *Database: MySQL
 *Version Control: Git & GitHub



Prerequsites:
*Python 3 is installed on your machine.
*MySQL Server installed and running.
 A MySQL database named `pokemon_db` created.
 Git (for cloning).




The installation and setup:
1.  **Clone the repository**
    ```bash
    git clone https://github.com/your-username/pokemon-data-pipeline.git
    cd pokemon-data-pipeline
    ```

2.  **Install Python dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Database Connection**
    Open `Pipeline.py` and update the `db_config` dictionary with your own MySQL credentials:
    ```python
    db_config = {
        "user": "your-username",
        "password": "your-password",
        "host": "localhost",
        "database": "pokemon_db"
    }
    ```

** THIS PROJECT IS FULLY CONTAINERIZED WITH DOCKER.**
THE ENTIRE APPLICATION CAN BE LAUNCHED WITH A SINGLE COMMAND:
docker-compose up

├── Dockerfile           - Defines the application container
├── docker-compose.yml   - Orchestrates the multi-container setup
├── requirements.txt     - Python dependencies
└── Pipeline.py          - Main ETL logic



Learning goals:

This project served as a hands-on exercise to build and understand:
- The end-to-end ETL pipeline concept.
- API interaction and handling JSON responses.
- Data wrangling and transformation with pandas.
- Database management with SQLAlchemy and MySQL.
- Professional practices like error handling and logging.

<img width="711" height="355" alt="image" src="https://github.com/user-attachments/assets/bce4a111-a894-47bc-955f-37382db8daf5" />
***The final Pokémon data stored in the MySQL database after the ETL process.*


*This project is for educational purposes ONLY and is not affiliated with or endorsed by Pokémon.*

 

