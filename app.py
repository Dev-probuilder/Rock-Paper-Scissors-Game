from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    computer_choice = ""
    user_choice = ""
    choices = ["Rock", "Paper", "Scissors"]
    
    if request.method == 'POST':
        user_choice = request.form.get('choice')
        computer_choice = choices[randint(0, 2)]
        
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Won!"
        else:
            result = "You Lost!"
    
    return render_template('index.html', choices=choices, result=result, user_choice=user_choice, computer_choice=computer_choice)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)