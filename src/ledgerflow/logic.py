from google import genai

def add_expense(date, category, note, amount, transaction_type="Expense"):
    global data
    new_entry = {
        "Date": date,
        "Category": category,
        "Note": note,
        "Amount": amount,
        "Income/Expense": transaction_type
    }
    data = data.append(new_entry, ignore_index=True)
    print(f" Added: {note} - {amount} ({category})")

def view_expenses(n=5):
    return data.tail(n)

def summarize_expenses(by="Category"):
    summary = data[data["Income/Expense"]=="Expense"].groupby(by)["Amount"].sum()
    return summary.sort_values(ascending=False)

# Function to auto-categorize using a language model
def auto_categorize(note, client):
    prompt = f"""
    Categorize this expense note into one of these following categories:
    Food, Transportation, Entertainment, Utilities, Education, Health, Shopping, Travel, Other.
    Expense Note: "{note}"
    Provide only the category name as the output.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", contents=prompt
        )
        return response.text
    except Exception as e:
        return "Other"

    
    