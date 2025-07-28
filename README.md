## 👨‍💻 Author

## **Ayodhya Kushwaha**  
## B.Tech, 3rd Year  
## Parul University  
## Focused on designing impactful technology solutions and real-world applications.
🔗 [Connect with me on LinkedIn](https://www.linkedin.com/in/ayodhaya-kushwaha-158643277)


## Google Pay Expense Analyzer (Flask App)
This project is a Flask-based web application that simulates a Google Pay-like interface with a powerful expense analyzer. It helps users visualize their spending habits, categorize transactions automatically, and gain personalized financial insights powered by the Google Gemini API.

Features
Google Pay-like Interface: A clean and intuitive UI mimicking the Google Pay home screen.

<img width="1919" height="1073" alt="image" src="https://github.com/user-attachments/assets/1f450933-68d9-46d2-b157-c7c5ba86516c" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/82d863f8-96c6-469b-b9b6-b5c12c335073" />



Spend Analyzer: A dedicated section to analyze expenses.

<img width="1919" height="1042" alt="image" src="https://github.com/user-attachments/assets/5abfae28-e357-4fe4-9feb-02a685308998" />
<img width="1919" height="1075" alt="image" src="https://github.com/user-attachments/assets/032ec559-10ea-4af6-ac66-0fa8483ecab9" />



Dynamic Category Breakdown: Expenses are automatically categorized (e.g., Food & Dining, Shopping, Investment, Education, Transfers, Travel, Groceries, Other) based on transaction notes and amounts.

Categorization Logic:

Amounts less than ₹20 without a specific note are categorized as "Other."

"Investment" includes "SIP/Stock - Autopay/Mandate."

"Transfers" includes "Whom you transfer."

Interactive Pie Chart: Visual representation of spending distribution across categories.

Sorted Category List: Categories are listed beside the pie chart, ordered by the amount spent (highest first), with "Other" always at the bottom.

Flexible Date Filtering: View expenses by:

This Week

This Month

Custom Date Range (select start and end dates)

AI-Powered Spending Insights: Integrates with the Google Gemini API to provide personalized summaries of spending habits and actionable financial tips.

Technologies Used
Backend: Flask (Python)

Frontend: HTML, CSS (Tailwind CSS for styling), JavaScript

AI/ML: Google Gemini API (gemini-2.0-flash model for text generation)

Project Structure
your_gpay_app/
├── app.py                  # Main Flask application logic, routes, API endpoints
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── index.html          # Google Pay home screen simulation
│   └── expense_analyzer.html # Expense analyzer page
└── static/
    └── css/
        └── style.css       # Optional: Custom CSS (currently empty, Tailwind is inline)

Setup Guide
Follow these steps to get the project up and running on your local machine.

1. Clone the Repository (or create files manually)
If you're getting the code in separate files, create the directory structure as shown above and place the respective code into the files.

2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

# Navigate into your project directory
cd your_gpay_app

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows (Command Prompt):
# venv\Scripts\activate.bat
# On Windows (PowerShell):
# .\venv\Scripts\Activate.ps1

Your terminal prompt should now show (venv) indicating the virtual environment is active.

3. Install Dependencies
With the virtual environment activated, install the required Python packages:

pip install -r requirements.txt

4. Get Your Google Gemini API Key
Go to Google AI Studio.

Sign in with your Google Account.

Look for "Get API key" or "Create API key" and generate a new key.

Copy your API Key.

5. Set the Gemini API Key as an Environment Variable
Important: Never hardcode your API key directly in app.py for production. Use environment variables.

On macOS/Linux:

export GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

On Windows (Command Prompt):

set GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

On Windows (PowerShell):

$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

Replace "YOUR_GEMINI_API_KEY_HERE" with the actual API key you copied.
Note: This command sets the environment variable for the current terminal session only. If you open a new terminal, you'll need to set it again.

6. Run the Flask Application
With the virtual environment still active, run the Flask development server:

flask run

You should see output similar to:

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

7. Access the Application
Open your web browser and navigate to the address provided in the terminal (usually http://127.0.0.1:5000/).

You will see the simulated Google Pay home screen. Click the "Spend Analyzer" button to access the expense analysis dashboard.

Usage
Home Screen: Navigate through the simulated Google Pay sections.

Spend Analyzer:

The pie chart and category list will display expenses for the currently selected period.

Use the "This Week," "This Month," and "Custom Range" buttons to filter transactions.

The category list dynamically sorts by amount spent (highest first), with "Other" always at the bottom.

Click "✨ Get Spending Insights" to receive an AI-generated summary and tip based on the displayed data.

Future Improvements
Database Integration: Replace in-memory transactions_data with a proper database (e.g., SQLite, PostgreSQL, MongoDB) for persistent storage.

User Authentication: Implement user login/registration to manage individual expense data.

Real Transaction Data: Integrate with actual banking APIs (with proper security and user consent) to fetch real transaction data.

More Sophisticated Categorization: Enhance the categorize_transaction logic with more advanced NLP techniques or user-defined rules.

Interactive Charts: Use a JavaScript charting library (e.g., Chart.js, D3.js) for more interactive and visually appealing charts.

Add/Edit Transactions: Allow users to manually add, edit, or delete transactions.


This project is Design By Ayodhya Kushwaha, 3th year B.Tech Student from parul University.
