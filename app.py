from flask import Flask, render_template, redirect, url_for
from Pages.assignment4 import assignment4

app = Flask(__name__)

# create new blueprint -> move relevant url to assignment4 routes
app.register_blueprint(assignment4)

@app.route('/')
def Home_page():
    return render_template('home.html')

@app.route('/contact')
def Contact_Page():
    return render_template('contact.html')

@app.route('/home')
def Home_page2():
    return render_template('home.html')


@app.route('/assignment3_1')
def assignment3_1():
    return render_template('assignment3_1.html',Hobbies = ['Basketball','Soccer','friends','Resturants'], Favorite_NBA_Players = ['Kobe', 'MJ', 'Lebron','Luka', 'Shaquil'])

@app.route('/assignment3_1/redirect')
def assignment3_1_redirect():
    return redirect('/assignment3_1')

@app.route('/assignment3_1/url_for')
def assignment3_1_url_for():
    return redirect(url_for('assignment3_1'))



if __name__ == '__main__':
    app.run(debug=True)

