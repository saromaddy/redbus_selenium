# importing libraries
import pandas as pd
import mysql.connector
import streamlit as st
# import plotly.express as px
import base64



def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Path to your image
background_image_path = 'imgs/bgimgg.jpg'

# Convert the image to base64
base64_image = get_base64_of_bin_file(background_image_path)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{base64_image}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
def connect_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Saro@123",
            database="redbus"
        )
        print("Connected to MySQL database")
        return conn
    except Exception as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Inject CSS with markdown
st.markdown(page_bg_img, unsafe_allow_html=True)

# Inject CSS with markdown
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='font-size:30px; color:Red;text-align:center;'>Redbus Data Scraping using Selenium Webdriver, Storing in SQL and accessing through Streamlit</h1>", unsafe_allow_html=True)

#about the Developer
def about_the_developer():
    st.header("About the Developer")
    st.image("imgs/saro.jpg", caption="Saravana Kumar T", width=250)
    st.subheader("Contact Details")
    st.write("Email: saromaddymca@gmail.com")
    st.write("Phone: 8940574870")
    st.write("[LinkedIn ID](https://www.linkedin.com/in/sarokumar/)")
    st.write("[github.com](https://github.com/saromaddy)")

def skills_take_away():
    st.header("Skills Take Away From This Project")
    st.caption("Selenium Webdriver")
    st.caption("Python Scripting")
    st.caption("Data Scraping")
    st.caption("Streamlit Application")
    st.caption("Pandas")
    st.caption("Data Management using MySQL")

def objective():
    st.header("Objective")
    st.caption("To Develop a streamlit application to showcase the data scraped from Redbus.in by using Selenium Webdriver stored in MySQL.")

def prerequisites():
    st.header("Prerequisites")
    st.write("1. Python Environment: Install Python on your system.")
    st.write("2. Selenium driver - Chrome")
    st.write("3. Dependencies: Install Streamlit, Pandas, Selenium, mysql_connector")
    st.write("4. SQL Database: Set up MySQL database needs to be configured with the local machine login credentials.")
    st.write("5. Streamlit: Install Streamlit library for running the application.")
        
def required_python_libraries():
    st.header("Required Python Libraries")
    st.write("The following Python libraries are required for the project:")
    libraries = ["Selenium", "pandas", "streamlit", "mysql.connector", "datetime", "re"]
    st.write(libraries)

def Approach():
    st.header("Approach")
    st.write("Data Fetching using selenium")
    st.write("Data Cleansing - Especially null handling after Exploratory Data Analysis")
    st.write("Migrate data to a SQL database using pandas libraries")
    st.write("Query the SQL database")
    st.write("Display data in the Streamlit application")


st.sidebar.header("Navigation Menu")
menu_option = st.sidebar.radio("Choose a page:", ["Home", "Project"])
if menu_option == "Home":
    def main():
        # Main layout
        col1, col2 = st.columns(2)

        with col1:
            st.header("Navigation")
            options = ["About the Developer", "Skills take away From This Project", "Objective", 
                    "Prerequisites", "Required Python Libraries", "Approach"]
            choice = st.radio("Go to", options)

        with col2:
            if choice == "About the Developer":
                about_the_developer()
            elif choice == "Skills take away From This Project":
                skills_take_away()
            elif choice == "Objective":
                objective()
            elif choice == "Prerequisites":
                prerequisites()
            elif choice == "Required Python Libraries":
                required_python_libraries()
            elif choice == "Approach":
                Approach()
    if __name__ == "__main__":
        main()
if menu_option == "Project":
    lists=[]
    df=pd.read_csv("csv_files/df.csv")
    for i,r in df.iterrows():
        lists.append(r["Route_name"])
    
    range_values = st.slider("Select a range of values:", min_value=0, max_value=10000, value=(2000, 4075))
    st.write("You selected a range:", range_values)
    
    conn = connect_mysql()
    my_cursor = conn.cursor()
    query=f'''select * from bus_routes 
            where Price Between {range_values[0]} and {range_values[1]} order by Price desc '''
    my_cursor.execute(query)
    out = my_cursor.fetchall()
    df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
    st.write(df)