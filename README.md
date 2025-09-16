# LedgerFlow

## Setup Instructions

**Tested Environment**
- Operating System: Linux 6.16.7-arch1-1
- Python Version: 3.13.7

1. **Install Python dependencies**

   Make sure you have Python 3.13.7 or newer installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file**

   In the root of the project, create a file named `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Run the application with Streamlit**

   Start the app using Streamlit:
   ```bash
   streamlit run src/ledgerflow/main.py
   ```

---