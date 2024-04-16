# ChimpSync - Mailchimp data Importer 


## Overview

ChimpSync is a Python application designed to facilitate the transfer of contact data from Mailchimp to Ometria's API. It streamlines the process by retrieving contact data from Mailchimp client accounts and converting it into the format accepted by Ometria’s API. 
This allows for efficient importing of contact data into Ometria.


## How it works 
The application operates in a straightforward manner, following these essential steps:

**1) Retrieve Contacts from Mailchimp:**
The application makes a request to the Mailchimp API to obtain the list of contacts for a specified client account.
The retrieved contact information includes details such as email addresses, names, and any other relevant data stored in the Mailchimp database.


**2) Data Transformation:**
Once the contact data is obtained from Mailchimp, the application parses and processes this information into a format compatible with the application. This is a direct transformation 
since the format is also compatible with Ometria API.
Data transformation involves mapping Mailchimp fields to corresponding fields accepted by the Ometria API, ensuring seamless integration between the two platforms. 


**3) Export to Ometria API:**
After the conversion process, the transformed contact data is exported to the Ometria API via a POST request.
During the initial export, all contact data is transferred to Ometria to establish the baseline for further updates.
Subsequent exports occur every 2 hours, ensuring that any new or updated contact information in Mailchimp is synchronized with Ometria.


## How to run it locally 

### Using Docker 

**1) Docker Installation:** Ensure Docker is installed and running on your local machine. 

**2) Build Docker Image:** In the project directory, run the following command to build the Docker image:

```
docker build -t <name-the-image> .
```

**3) Run Docker Container:** Once the image is built, run the following command to start the Docker container:

```
docker run -it <name-of-image>
```

### Using the terminal 

**1) Python Virtual Environment Setup:** First, ensure you have Python installed on your machine. 
Then, create a virtual environment by running:

```
python -m venv venv
```

**2) Activate Virtual Environment:** Activate the virtual environment based on your operating system:

**Windows:**
```
venv\Scripts\activate
```

**Unix or MacOS**
```
source venv/bin/activate
```

**3) Install Dependencies:** Install the required dependencies listed in requirements.txt using pip:

```
pip install -r requirements.txt
```

**4) Run Application:** Finally, execute the main Python script to run the application:

```
python main.py
```

#### Running the tests

In the *src* directory, run the following command: 
```
$ python -m unittest discover -s tests
```
