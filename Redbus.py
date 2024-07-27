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
    df_orgin = pd.read_csv("origin.csv")
    origin_list = []
    df_destination = pd.read_csv("destination.csv")
    destination_list = []
    for j,k in df_orgin.iterrows():
        origin_list.append(k['Origin'])
    for l,m in df_destination.iterrows():
        destination_list.append(m['Destination'])
    origin_set = list(set(origin_list))
    destination_set = list(set(destination_list))
    for i,r in df.iterrows():
        lists.append(r["Route_name"])
    
    range_values = st.slider("Select a range of values:", min_value=0, max_value=10000, value=(0, 10000))
    st.write("You selected a range:", range_values)
    
    origin = st.selectbox("Choose From", origin_set)
    destination = st.selectbox("Choose To", destination_set)
    # origin = st.selectbox("Select an option",df)
    conn = connect_mysql()
    my_cursor = conn.cursor()
    col1,col2,col3 = st.columns(3)
    with col1:
        if st.button("Apply for price sort"):
            st.write(f'The values between {range_values[0]} and {range_values[1]}')
            try:
                query=f'''select Bus_name,Bus_type,Start_time,End_time,Total_duration,
                            Price,Seats_Available,Ratings,Route_name,Origin,Destination from bus_routess 
                        where Price Between {range_values[0]} and {range_values[1]} order by Price desc'''
                my_cursor.execute(query)
                out = my_cursor.fetchall()
                def df():
                    df=pd.DataFrame(out,columns=["Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                                            "Price","Seats_Available","Ratings","Route_name","Origin","Destination"])
                    
                    st.write(df)
                    st.write(len(df))
            except:
                st.write("Error: Fetching the database")
    

    with col2:
        if st.button ("Apply for route sort"):
            try:
                query=f'''select Bus_name,Bus_type,Start_time,End_time,Total_duration,
                            Price,Seats_Available,Ratings,Route_name,Origin,Destination from bus_routess 
                        where Origin = {'"'+origin+'"'} AND Destination = {'"'+destination+'"'}'''
                my_cursor.execute(query)
                out = my_cursor.fetchall()
                def df():
                    df=pd.DataFrame(out,columns=["Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                                            "Price","Seats_Available","Ratings","Route_name","Origin","Destination"])
                    
                    st.write(df)
                    st.write(len(df))
            except:
                st.write("Error: Fetching the database")
    with col3:
        if st.button (" Apply for both route and price sort"):
            try:
                query=f'''select Bus_name,Bus_type,Start_time,End_time,Total_duration,
                                Price,Seats_Available,Ratings,Route_name,Origin,Destination from bus_routess 
                            where Origin = {'"'+origin+'"'} AND Destination = {'"'+destination+'"'} AND Price Between {range_values[0]} and {range_values[1]} order by Price desc'''
                my_cursor.execute(query)
                out = my_cursor.fetchall()
                def df():
                    df=pd.DataFrame(out,columns=["Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                                            "Price","Seats_Available","Ratings","Route_name","Origin","Destination"])
                    
                    st.write(df)
                    st.write(len(df))
            except:
                st.write("Error: Fetching the database")

    try:
        df()
    except:
        st.write ("Still DataFrame not fetched")