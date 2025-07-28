import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from datetime import datetime, timedelta

app = Flask(__name__)

# Configure Google Generative AI (Gemini API)
# IMPORTANT: Replace "YOUR_API_KEY" with your actual Gemini API key.
# For production, use environment variables to store API keys.
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "AIzaSyBpRbDtVGwcU0WlyFuhBofEN_Wx8QvLUk8"))

# --- Simulated In-Memory Transaction Data ---
# In a real application, this would come from a database.
transactions_data = [
    {'id': 1, 'type': 'expense', 'amount': 850.00, 'description': 'Restaurant Bill', 'date': '2025-07-27', 'note': 'Dinner with friends at Italian restaurant'},
    {'id': 2, 'type': 'expense', 'amount': 1020.00, 'description': 'Bus Ticket', 'date': '2025-07-26', 'note': 'Bus fare for daily commute'},
    {'id': 3, 'type': 'expense', 'amount': 1500.00, 'description': 'Online Shopping', 'date': '2025-07-25', 'note': 'New shoes from online store'},
    {'id': 4, 'type': 'income', 'amount': 35000.00, 'description': 'Salary Deposit', 'date': '2025-07-20', 'note': 'Monthly salary credited'},
    {'id': 5, 'type': 'expense', 'amount': 2500.00, 'description': 'Electricity Bill', 'date': '2025-07-24', 'note': 'Monthly electricity bill payment'},
    {'id': 6, 'type': 'expense', 'amount': 3000.00, 'description': 'SIP Investment', 'date': '2025-07-23', 'note': 'Investment in SIP via mandate'},
    {'id': 7, 'type': 'expense', 'amount': 750.00, 'description': 'Movie Tickets', 'date': '2025-07-22', 'note': 'Weekend movie and popcorn'},
    {'id': 8, 'type': 'expense', 'amount': 5000.00, 'description': 'Rent Transfer', 'date': '2025-07-21', 'note': 'Rent payment to landlord'},
    {'id': 9, 'type': 'expense', 'amount': 1200.00, 'description': 'Grocery Shopping', 'date': '2025-07-19', 'note': 'Weekly groceries from supermarket'},
    {'id': 10, 'type': 'expense', 'amount': 4000.00, 'description': 'Flight Ticket', 'date': '2025-07-18', 'note': 'Flight booking for vacation'},
    {'id': 11, 'type': 'expense', 'amount': 600.00, 'description': 'Gym Membership', 'date': '2025-07-17', 'note': 'Monthly gym subscription'},
    {'id': 12, 'type': 'expense', 'amount': 300.00, 'description': 'Coffee Shop', 'date': '2025-07-16', 'note': 'Morning coffee'},
    {'id': 13, 'type': 'expense', 'amount': 15.00, 'description': 'Gum', 'date': '2025-07-28', 'note': ''},
    {'id': 14, 'type': 'expense', 'amount': 10.00, 'description': 'Candy', 'date': '2025-07-28', 'note': 'Small treat'},
    {'id': 15, 'type': 'expense', 'amount': 250.00, 'description': 'Book Purchase', 'date': '2025-07-10', 'note': 'Book from local store'},
    {'id': 16, 'type': 'expense', 'amount': 70.00, 'description': 'Bus Fare', 'date': '2025-07-05', 'note': 'Local bus'},
    {'id': 17, 'type': 'expense', 'amount': 2000.00, 'description': 'Stock Buy', 'date': '2025-06-15', 'note': 'Stock purchase'},
    {'id': 18, 'type': 'expense', 'amount': 500.00, 'description': 'Dinner', 'date': '2025-06-20', 'note': 'Dinner out'},
    {'id': 19, 'type': 'expense', 'amount': 5000.00, 'description': 'University Fees', 'date': '2025-07-15', 'note': 'Tuition fees for semester'},
]

# --- Helper function for transaction categorization (copied from JS logic) ---
def categorize_transaction(note, amount):
    lower_note = note.lower()

    if amount < 20 and lower_note == '':
        return 'Other'

    if any(keyword in lower_note for keyword in ['restaurant', 'cafe', 'dinner', 'lunch', 'food', 'coffee']):
        return 'Food & Dining'
    if any(keyword in lower_note for keyword in ['bus', 'train', 'metro', 'fuel', 'taxi']):
        return 'Transport'
    if any(keyword in lower_note for keyword in ['shop', 'mall', 'clothes', 'shoes', 'online store', 'book']):
        return 'Shopping'
    if any(keyword in lower_note for keyword in ['flight', 'hotel', 'vacation', 'trip']):
        return 'Travel'
    if any(keyword in lower_note for keyword in ['grocery', 'supermarket', 'vegetables', 'milk']):
        return 'Groceries'
    if any(keyword in lower_note for keyword in ['investment', 'stock', 'mutual fund', 'sip']):
        return 'Investment'
    if any(keyword in lower_note for keyword in ['education', 'tuition', 'course', 'school', 'college']):
        return 'Education'
    if any(keyword in lower_note for keyword in ['transfer', 'rent', 'loan payment', 'send money']):
        return 'Transfers'

    return 'Other'

# --- Flask Routes ---

@app.route('/')
def index():
    """Serves the main Google Pay-like home page."""
    return render_template('index.html')

@app.route('/expense-analyzer')
def expense_analyzer():
    """Serves the expense analyzer page."""
    return render_template('expense_analyzer.html')

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    """
    API endpoint to fetch filtered transactions.
    Supports 'filter_type' (week, month, custom) and 'start_date', 'end_date' for custom.
    """
    filter_type = request.args.get('filter_type')
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    filtered_transactions = []
    current_date = datetime.now()

    if filter_type == 'week':
        # Calculate start and end of the current week (Sunday to Saturday)
        start_of_week = current_date - timedelta(days=current_date.weekday() + 1) # Monday is 0, Sunday is 6. So Sunday is day 6.
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_week = start_of_week + timedelta(days=6)
        end_of_week = end_of_week.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        for t in transactions_data:
            t_date = datetime.strptime(t['date'], '%Y-%m-%d')
            if start_of_week <= t_date <= end_of_week:
                filtered_transactions.append(t)

    elif filter_type == 'month':
        # Calculate start and end of the current month
        start_of_month = current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        # Last day of the current month
        next_month = current_date.replace(day=28) + timedelta(days=4) # Go to next month
        end_of_month = next_month - timedelta(days=next_month.day)
        end_of_month = end_of_month.replace(hour=23, minute=59, second=59, microsecond=999999)

        for t in transactions_data:
            t_date = datetime.strptime(t['date'], '%Y-%m-%d')
            if start_of_month <= t_date <= end_of_month:
                filtered_transactions.append(t)

    elif filter_type == 'custom' and start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999) # Include whole end day

            for t in transactions_data:
                t_date = datetime.strptime(t['date'], '%Y-%m-%d')
                if start_date <= t_date <= end_date:
                    filtered_transactions.append(t)
        except ValueError:
            return jsonify({"error": "Invalid date format"}), 400
    else:
        # Default to all transactions if no filter or invalid filter
        filtered_transactions = transactions_data

    return jsonify(filtered_transactions)

@app.route('/api/insights', methods=['POST'])
def get_insights():
    """
    API endpoint to generate spending insights using the Gemini API.
    Expects JSON payload with 'totalSpent', 'totalIncome', 'balance', 'expenseCategories'.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    total_spent = data.get('totalSpent')
    total_income = data.get('totalIncome')
    balance = data.get('balance')
    expense_categories = data.get('expenseCategories')

    if None in [total_spent, total_income, balance, expense_categories]:
        return jsonify({"error": "Missing required data fields"}), 400

    # Construct the prompt for the Gemini API
    prompt = f"""Analyze the following monthly financial data and provide a concise summary of spending habits, along with one actionable tip for improvement.
    Total Spent: ₹{total_spent:.2f}
    Total Income: ₹{total_income:.2f}
    Balance: ₹{balance:.2f}
    Expense Categories:
    {chr(10).join(expense_categories)}

    Please provide your analysis and tip in a friendly, encouraging tone."""

    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        insight_text = response.text
        return jsonify({"insight": insight_text})
    except Exception as e:
        app.logger.error(f"Error calling Gemini API: {e}")
        return jsonify({"error": f"Failed to generate insights: {str(e)}"}), 500

if __name__ == '__main__':
    # For development, you can run with debug=True
    # For production, use a production-ready WSGI server like Gunicorn or uWSGI
    app.run(debug=True)
