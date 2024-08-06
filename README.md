# Redbus_selenium

Project Requirements:

* Selenium
* Selenium.webdriver
* Pandas
* Exploratory Data Analysis
* MySQL - (mysql.connector (python))
* base64
* basic html (for fetching the data from the website using selenium)
* Good internet (to avoid null values or loss of data while the data is being scraped from redbus)

# Procedures followed
1. Scrap the www.redbus.in using selenium Webdriver
  1.a 10 State Bus SRTC needs to be scraped minimum
  1.b Along the routes, all the private bus details need to be scrapped
2. Scraped Data needs to be stored in MySQL using mysql.connector python
  2.a EDA - Exploratory Data Analysis
  2.b Treating the null values and outliers if any
  2.c All the data will be pushed to mysql using basic mysql query
3. Develop a streamlit app (browser-based) to fetch the stored data; this app should have the facility to filter the data. 
  3.a The streamlit application has majorly two segments, one is about the developer which I did just to practice the streamlit
  3.b The project segment has the options to list the dataset as a pandas data frame upon querying
  3.c There are three queries written one is price sort with given price range, second is to sort the data using the origin and destination and third is the combination of the first two.

# Key Learnings
1. Python
2. Selenium
3. HTML ,CSS (basics to identify the tags)
4. Exploratory Data Base management 
5. MySQL
6. Database Management
7. Streamlit