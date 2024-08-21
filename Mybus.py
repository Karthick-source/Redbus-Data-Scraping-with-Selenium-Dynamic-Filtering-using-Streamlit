import pandas as pd
import mysql.connector
import streamlit as st
from streamlit_option_menu import option_menu


# Function to fetch data from MySQL based on filters
def fetch_bus_data(state, route, bus_type, fare_range, departing_time):
    db_connection = mysql.connector.connect(host="localhost", user="root", password="root", database="bus_routes")
    my_cursor = db_connection.cursor()

    # Define fare range based on selection
    fare_min, fare_max = {"50-500": (50, 500), "501-2000": (501, 2000), "2000 and above": (2001, 5000)}[fare_range]

    # Define bus type condition
    bus_type_condition = {
        "Sleeper": "Bus_type LIKE '%Sleeper%'",
        "Semi-Sleeper": "Bus_type LIKE '%Semi Sleeper%'",
        "Others": "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi Sleeper%'"
    }[bus_type]

    query = f'''
        SELECT * FROM bus_routes.bus_details 
        WHERE Price BETWEEN {fare_min} AND {fare_max}
        AND Route_name = "{route}"
        AND {bus_type_condition}
        AND Departing_time >= '{departing_time}'
        ORDER BY Price, Departing_time DESC
    '''
    my_cursor.execute(query)
    out = my_cursor.fetchall()
    db_connection.close()

    df = pd.DataFrame(out, columns=[
        "ID", "Route_name", "Bus_name", "Bus_type", "Duration", "Ratings", "Seat_available", "Price", "Departing_time", "Reaching_time", "Route_link"
    ])
    return df

# Load CSV files into lists
def load_route_data(file_path):
    df = pd.read_csv(file_path)
    return df['Route_name'].tolist()

# File paths for CSVs
file_paths = {
    "Andhra Pradesh": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\andhra.csv",
    "Kerala": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\kerala.csv",
    "Telangana": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\telangana.csv",
    "Kadamba": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\kadamba.csv",
    "Rajasthan": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\Rajasthan.csv",
    "South Bengal": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\south_bengal.csv",
    "Himachal": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\himachal.csv",
    "Assam": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\assam.csv",
    "Uttar Pradesh": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\uttar_pradesh.csv",
    "West Bengal": "C:\\Users\\admin\\Desktop\\REDBUS_CSV\\west_bengal.csv"
}

# Load all routes
routes = {}  # Create an empty dictionary to store routes

# Loop through each state in the file_paths dictionary
for state in file_paths:
    # Load the route data for the current state using the CSV file path
    route_list = load_route_data(file_paths[state])
    
    # Add the state and its corresponding routes to the routes dictionary
    routes[state] = route_list


# Set Streamlit page config
st.set_page_config(layout="wide")

# Streamlit option menu for navigation
web = option_menu(
    menu_title="MyBus",
    options=["Home", "States and Routes"],
    icons=["house", "map"],
    orientation="horizontal",
    menu_icon="cast",
    styles={
        "container": {"padding": "5!important", "background-color": "#f0f0f0"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#FF4B4B"},
    }
)

# Home page
if web == "Home":
    
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #1F77B4;'>Transforming Transportation with Data-Driven Insights</h3>", unsafe_allow_html=True)

    st.markdown("<h2 style='color: #1F77B4;'>Domain: Transportation</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #1F77B4;'>Objective:</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data...</p>", unsafe_allow_html=True)

    st.markdown("<h2 style='color: #1F77B4;'>Skill-take:</h2>", unsafe_allow_html=True)
    st.markdown("<p>Selenium, Python, Pandas, MySQL, mysql-connector-python, Streamlit.</p>", unsafe_allow_html=True)

    st.markdown("<h2 style='color: #1F77B4;'>Developed by: D Karthick </h2>", unsafe_allow_html=True)

# States and Routes page
if web == "States and Routes":
    col1, col2, col3 = st.columns([2, 3, 2])

    with col1:
        S = st.selectbox("Select State", list(routes.keys()), key="state_select", help="Choose a state to filter the bus routes.")
        
    with col2:
        selected_route = st.selectbox(f"Available Routes in {S}", routes[S], key="route_select")

    with col3:
        st.button("Get Route Info", key="get_route_info", help="Click to retrieve the bus routes.")

    col1, col2 = st.columns(2)

    with col1:
        select_type = st.radio("Choose Bus Type", ("Sleeper", "Semi-Sleeper", "Others"), key="bus_type", help="Select the type of bus.")
    with col2:
        select_fare = st.radio("Choose Fare Range", ("50-500", "501-2000", "2000 and above"), key="fare_range", help="Select the fare range.")

    TIME = st.time_input("Select Departure Time", key="departure_time", help="Choose the preferred departure time.")

    # Displaying data based on selection
    if st.button("Show Results", key="show_results"):
        df_result = fetch_bus_data(S, selected_route, select_type, select_fare, TIME)
        st.dataframe(df_result)

