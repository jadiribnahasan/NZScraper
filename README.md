# NZScraper

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a Linux machine. This guide is tailored for Ubuntu, but the steps should be similar for other distributions.
* You have Python 3.8 or later installed. You can verify your Python version with `python --version`.

## Installing MongoDB

1. Update the packages list:

```bash
sudo apt-get update
```

2. Install MongoDB:

```bash
sudo apt-get install -y mongodb
```

3. Verify that MongoDB has been started on your machine:

```bash
sudo systemctl status mongodb
```

## Setting Up the Project

1. Clone the repository:

    ```bash
   git clone https://github.com/your_username/NZScraper.git
   ```
2. Navigate to the project directory:

    ```bash
   cd NZScraper
   ```
3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

5. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Scripts

1. Run the db_manager script (replace db_manager.py with the actual name of your script):

    ```bash
    python db_manager.py
    ```
2. In a new terminal window, activate the virtual environment and run the scrapper script:

    ```bash
    source venv/bin/activate
    python sc.py
    ```
   
3. In another new terminal window, activate the virtual environment and run the crud_server script:

    ```bash
    source venv/bin/activate
    python crud_server.py
    ```
You should now have the db_manager, scrapper, and crud_server scripts running in separate terminal windows. 


