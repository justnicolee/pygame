
from flask import Flask, render_template

game = Flask(__name__)

@game.route('/character1')
def char1():
    character = {
            "name" : "Powerful Knight🛡️",
            "level" : 2,
            "health" : "2000 ❤️❤️",
            "weapon" : "Sword 🗡️",
            "ability": "Uses an extra sword and activates protection for 15 secs ⚔️"
        }
    
    return render_template('index.html', character=character)

@game.route('/character2')
def char2():
    character = {
            "Name" : "Brave Bear 🐻",
            "Level" : 3,
            "Health" : "2500 ❤️❤️🩷",
            "Weapon" : "Log of Wood 🪵",
            "Special Ability": "Doubles in size and strength 💪"
        }
    
    return render_template('index.html', character=character)

@game.route('/character3')
def char3():
    character = {
            "Name" : "Mr Ogre 🧌",
            "Level" : 4,
            "Health" : "3000 ❤️❤️❤️",
            "Weapon" : "Bad Breath 💨",
            "Special Ability": "Activates tornado with breath 🌪️"
        }
    
    return render_template('index.html', character=character)


if __name__ == "__main__":
    game.run(debug=True)