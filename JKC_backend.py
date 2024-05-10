from flask import Flask, render_template
import csv

app = Flask(__name__)

# JKC back end route.
@app.route('/')
def JKC():

    # Read the CSV file and sends data.
    data = []
    with open('data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:

            # Convert price to float and date to a string (you may need to adjust date parsing based on your CSV format)

            # Casts str price to float.
            row['price'] = float(row['price'])

            # Date format : XX/XX/XXXX
            row['date'] = row['date']

            # Holds weather the price is a sale price or not.
            row['note'] = row['notes']

            data.append(row)

    # Pass data to the HTML template
    return render_template('JKC_index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
