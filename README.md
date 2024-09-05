## **Introduction**

* The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionise the transportation industry by providing a comprehensive solution for collecting, analysing, and visualising bus travel data. By utilising Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

## **Domain**

* Transportation  
  


## **SKILL-TAKEAWAY**

* Python scripting,Selenium,Data Collection,Data Management using SQL,Streamlit

## **TECHNOLOGY USED**

* Python 3.12  
* MySQL 8.0  
* Streamlit  
* Selenium

**FUNCTIONALITY OVERVIEW**

*   Selenium is an effective tool for automating web browsers, making it ideal for tasks like web scraping. To gather bus details from RedBus, you can utilize Selenium to automate the process of finding buses and extracting the necessary information. This includes interacting with web elements such as search fields and buttons, ensuring the page loads correctly, and retrieving the relevant details from the search results.  
  


**POPULATE THE DATABASE WITH DATA**

*       The gathered bus details were converted into pandas DataFrames. Prior to this, a new database and tables were set up using the MySQL connector. The data was then inserted into the appropriate tables with the help of MySQL. The database could be accessed and managed within the MySQL environment.

**STREAMLIT WEB APPLICATION**

*   With the help of Streamlit, you can create an interactive application similar to RedBus by designing a user-friendly interface that allows users to search for bus routes, view available buses, and get details like departure times and prices

## **PACKAGES AND LIBRARIES**

* pandas as pd  
* mysql.connector  
* import time  
* streamlit as st  
* import datetime  
* from streamlit\_option\_menu import option\_menu  
* from selenium import webdriver



  ![Capture](https://github.com/user-attachments/assets/ee8ffc67-8dea-4d44-a1b3-ac875e58c6a9)
