# Personal Finance Tracker

A web-based application to track your personal finances, including income, expenses, and savings. The application provides features for categorizing transactions, viewing spending patterns, and generating financial summaries.

## Features

- Add and delete transactions
- Categorize expenses
- View total income and expenses
- Track balance
- Visualize spending patterns with charts
- Categorize expenses by type
- Responsive design for all devices

## Setup

1. Make sure you have Python 3.7+ installed on your system.

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. **Adding Transactions**
   - Select the transaction type (Income/Expense)
   - Enter the amount
   - Choose a category
   - Add an optional description
   - Click "Add Transaction"

2. **Viewing Summary**
   - The dashboard shows total income, expenses, and current balance
   - Pie chart displays expenses by category
   - Bar chart compares income vs expenses

3. **Managing Transactions**
   - View all transactions in the table below
   - Delete transactions using the delete button
   - Transactions are automatically sorted by date

## Technologies Used

- Backend: Flask (Python)
- Database: SQLite
- Frontend: HTML, CSS, JavaScript
- Charts: Chart.js
- UI Framework: Bootstrap 5 