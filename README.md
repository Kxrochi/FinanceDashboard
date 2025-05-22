# Personal Finanace Tracker

A sleek and modern finance dashboard to help you track your money in and out. Built with Flask and modern web technologies.

## Features

### Money Overview
- Track your total income and expenses
- See your current balance
- Monitor your savings rate
- Beautiful dark theme with interactive elements

### Visual Analytics
- Pie chart showing where your money goes
- Bar chart comparing money in vs money out
- Interactive charts with hover effects

### Transaction Management
- Add new transactions with type, amount, category, and description
- View all transactions in a sortable and filterable list
- Delete transactions with confirmation
- Search through your transaction history

### Smart Filtering
- Filter by transaction type (Money In/Money Out)
- Filter by category
- Sort by date or amount
- Search through transactions

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: 
  - HTML5
  - CSS3 with modern features
  - JavaScript (ES6+)
- **Libraries**:
  - Chart.js for data visualization
  - GSAP for smooth animations
  - Font Awesome for icons
  - Bootstrap for responsive layout

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://localhost:5000`

## API Endpoints

### Transactions
- `GET /api/transactions` - Get all transactions
- `POST /api/transactions` - Add new transaction
- `DELETE /api/transactions/<id>` - Delete a transaction

### Summary
- `GET /api/summary` - Get financial summary (totals, categories, etc.)

## Project Structure

```
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── static/            # Static files
│   ├── css/          # Stylesheets
│   └── js/           # JavaScript files
└── templates/         # HTML templates
    └── index.html    # Main dashboard template
```

## Contributing

Feel free to submit issues and enhancement requests!
