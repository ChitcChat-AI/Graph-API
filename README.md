# About

The ChitChat.AI Graph-API is a API-server created with flask and designed to enable researchers to get relevant results of the experiment he run, it creates a network graph and check for interesting graph attributes for the research to analyze after.

# Installation

### Prerequisites
Before you begin, ensure you have met the following requirements:
- Python, pip 


### Steps
To install and run, follow these steps:

1. **Clone the Repository**  

   git clone https://github.com/ChitcChat-AI/Graph-API.git

2. **Navigate to the Project Directory**

   cd Graph-API

3. **Set Up a Virtual Environment (optional but recommended)**
    
    - Create a virtual environment to isolate your dependencies:
      
        python -m venv venv
    - Activate the virtual environment:
      
        on MAC: source venv\bin\activate
      
        on WINDOWS: source venv/Scripts/activate


4. **Install Dependencies**

   pip install -r requirements.txt


5. **Run the Application**

   ./start.sh

6. **Access the Application**

   To create a graph, you need to make a POST request with the messages formatted correctly in the request body. You can utilize the researcher platform to view the results of an experiment, which will trigger the request with the appropriate data format.
