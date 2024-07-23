# Hubspot list extraction

---
This project contains a simple script that extracts a list of contacts from Hubspot, adds it to 
a pandas DataFrame and finally saves it to a CSV file.

The output is saved into the `files` folder.

You may edit the output to any format you like.

---

## Installation

We offer two different ways to install the project:


### Local installation

Make sure you're using Python 3.9 or higher.

Install requirements

```pip install -r requirements.txt```

### Docker installation

```docker-compose build```


### Environment setup

Add Your Hubspot API key to the .env file along with the ILS IDs of the lists you want to extract.

example .env file (explicitly used with docker-compose:

```bash
HUBSPOT_API_KEY=your_api_key
ILS_LIST_IDS=123456,789012  # must be set as a comma separated list
```

You could also edit the `main.py` file to include the API key and list IDs directly.

```python
HUBSPOT_API_KEY = 'your_api_key'
ILS_LIST_IDS = [123456, 789012]  # must be set as a list
```

---

## Usage

Once everything's set up on a local machine, you can run the script with the following command:

```python main.py```

If you're using Docker, you can run the script with the following command:

```docker-compose run python```

