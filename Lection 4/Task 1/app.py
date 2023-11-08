from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def calculator_form():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    
    match operation:
        case 'add':
           result = num1 + num2
        case'subtract':
           result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
             if num2 == 0:
               return "Division by zero is not allowed."
             else:
               result = num1 / num2    
    return f"Result: {result}"

app.run()
