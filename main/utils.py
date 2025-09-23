from google import genai


# Function to auto-categorize using a language model
def categorize_transaction(note, client):
    prompt = f"""
    Categorize this expense note into one of these following categories:
    Food, Transportation, Entertainment, Utilities, Education, Health, Shopping, Travel, Other.
    Expense Note: "{note}"
    Provide only the category name as the output.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=prompt
        )
        return response.text
    except Exception as e:
        return "Other"
