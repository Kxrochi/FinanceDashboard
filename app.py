from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    type = db.Column(db.String(10), nullable=False)  # 'income' or 'expense'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    return jsonify([{
        'id': t.id,
        'date': t.date.strftime('%Y-%m-%d'),
        'amount': t.amount,
        'category': t.category,
        'description': t.description,
        'type': t.type
    } for t in transactions])

@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    transaction = Transaction(
        amount=float(data['amount']),
        category=data['category'],
        description=data['description'],
        type=data['type']
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction added successfully'})

@app.route('/api/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction deleted successfully'})

@app.route('/api/summary')
def get_summary():
    transactions = Transaction.query.all()
    summary = {
        'total_income': sum(t.amount for t in transactions if t.type == 'income'),
        'total_expenses': sum(t.amount for t in transactions if t.type == 'expense'),
        'by_category': {}
    }
    
    for t in transactions:
        if t.type == 'expense':
            if t.category not in summary['by_category']:
                summary['by_category'][t.category] = 0
            summary['by_category'][t.category] += t.amount
    
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True) 