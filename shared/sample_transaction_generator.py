import csv
import random
from datetime import datetime, timedelta

# Define parameters for generating transactions
NUM_TRANSACTIONS = 10000
START_DATE = datetime(2022, 6, 1)
END_DATE = datetime(2022, 12, 31)
ACCOUNTS = ['Checking', 'Savings', 'Joint Account']
COUNTERPARTIES = ['Amazon', 'Uber', 'Walmart', 'Starbucks', 'Grab',
                  'Gojek', 'Fairprice', 'Google', 'ACME']
TAGS = ['Groceries', 'Entertainment', 'Transportation', 'Travel',
        'General Expenses', 'Dining']
LOCATION = ['Singapore', 'Indonesia', 'Japan',
            'Australia']


def generate_transaction(id):
    account = random.choice(ACCOUNTS)
    amount = round(random.uniform(0, 1000), 2)  # round to 2 decimal places
    counterparty = random.choice(COUNTERPARTIES)
    tags = ', '.join(random.sample(TAGS, random.randint(1, len(TAGS))))
    location = random.choice(LOCATION)
    date = START_DATE + \
        timedelta(days=random.randint(0, (END_DATE - START_DATE).days))
    datestring = date.strftime('%Y-%m-%d')
    return [id, account, amount, counterparty, tags, datestring, location]


with open('sample_transactions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id','Account', 'Amount', 'Counterparty',
                    'Tags', 'Date', 'Location'])  # write header row
    for i in range(NUM_TRANSACTIONS):
        transaction = generate_transaction(i)
        writer.writerow(transaction)
