from flask import Flask, render_template

app = Flask(__name__)

player_x = 2
player_y = 2
max_x = 10
max_y = 10

field_size = 10

@app.route('/')
def index():
    return render_template('index.html', player_x=player_x, player_y=player_y, field_size=field_size)

@app.route('/move/<direction>')
def move(direction):
    global player_x, player_y
    match direction:
        case 'Up':
            if player_y > 0:
                player_y -= 1
        case 'Down':
            if player_y < max_y - 1:
                    player_y += 1
        case 'Left':
            if player_x > 0: 
                player_x -= 1
        case 'Right':
            if player_x < max_x - 1:
                player_x += 1

    return render_template('index.html', player_x=player_x, player_y=player_y, field_size=field_size)
app.run()