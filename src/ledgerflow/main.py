import logic

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

from google import genai

load_dotenv()

client = genai.Client()

# Initialize csv file
csv_file = "expenses.csv"
if os.path.exists(csv_file):
    data = pd.read_csv(csv_file)
else:
    data = pd.DataFrame(columns=["Date", "Category", "Note", "Amount", "Income/Expense"])
    
st.title("LedgerFlow - Personal Finance Manager")

with st.form("expense_form"):
    date = st.date_input("Date")
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    
    predicted_category = ""
    if description:
        predicted_category = logic.auto_categorize(description, client)
        
    category = st.text_input(
        "Category (auto predicted, but you can edit)",
        value = predicted_category
    )
    
    submitted = st.form_submit_button("Add Expense")
    
    if submitted:
        new_expense = {"Date": date, "Description": description, "Amount": amount, "Category": category}
        data = pd.concat([data, pd.DataFrame([new_expense])], ignore_index=True)
        data.to_csv(csv_file, index=False)
        st.success(f"Added: {description} - {amount} ({category})")
        
    st.subheader("All Expenses")
    st.dataframe(data)
    
    if not data.empty:
        st.subheader("Expense Breakdown by Category")
        
        category_totals = data.groupby("Category")["Amount"].sum()
        
        # Bar Chart
        fig, ax = plt.subplots()
        category_totals.plot(kind='bar', ax=ax)
        ax.set_ylabel("Amount")
        st.pyplot(fig)
        
        # Pie Chart
        st.subheader("Category Distribution")
        fig2, ax2 = plt.subplots()
        category_totals.plot(kind="pie", autopct='%1.1f%%', ax=ax2)
        st.pyplot(fig2)