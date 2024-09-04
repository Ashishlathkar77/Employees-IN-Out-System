import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Function to load data from a CSV file or create a new DataFrame if the file doesn't exist
def load_data():
    if os.path.exists("attendance_log.csv"):
        return pd.read_csv("attendance_log.csv")
    else:
        return pd.DataFrame(columns=["Employee ID", "Name", "Action", "Timestamp"])

# Function to save data to a CSV file
def save_data(data):
    data.to_csv("attendance_log.csv", index=False)

# Streamlit application
def main():
    st.title("Employee In & Out Marking System")

    # Load the data
    data = load_data()

    # Input employee details
    employee_id = st.text_input("Employee ID")
    employee_name = st.text_input("Employee Name")

    # Mark In/Out buttons
    if st.button("Mark In"):
        mark_attendance(data, employee_id, employee_name, "In")
    if st.button("Mark Out"):
        mark_attendance(data, employee_id, employee_name, "Out")

    # Display attendance log
    st.subheader("Attendance Log")
    st.dataframe(data)

    # Save data to CSV
    save_data(data)

    # Provide download link for the CSV file
    st.subheader("Download Attendance Log")
    st.download_button(label="Download CSV", data=data.to_csv(index=False), file_name="attendance_log.csv", mime="text/csv")

def mark_attendance(data, employee_id, employee_name, action):
    """Function to mark attendance."""
    if employee_id and employee_name:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data.loc[len(data)] = [employee_id, employee_name, action, timestamp]
        st.success(f"Marked {action} for {employee_name} at {timestamp}")
    else:
        st.error("Please enter both Employee ID and Name")

if __name__ == "__main__":
    main()
