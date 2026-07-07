from pymongo import MongoClient
import streamlit as st

client = MongoClient(st.secrets.mongo_db_key)

db = client["Alveoli"]

patient_data = db["Patient_Data"]
