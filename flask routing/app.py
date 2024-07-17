from flask import Flask

app = Flask(__name__)
@app.route('/home')
def home():
    return '''<html>
    <h1>Welcome to my Photolibary</h1>
    <h3>We have three types of pictures: food,pets and outer space</h3>

    <br><a href = "/food1"> Go to the first food picture! </a><br>
    <a href = "/food3"> Go to the third food picture! </a><br>
    <a href = "/pet2"> Go to the second pet picture! </a><br>
    <a href = "/space1"> Go to the first space picture! </a>

    </html>'''
@app.route('/food1')
def food1():
    return '''<html><img width = "400" height = "400" src = "https://static01.nyt.com/images/2021/02/17/dining/17tootired-grilled-cheese/17tootired-grilled-cheese-superJumbo.jpg?quality=75&auto=webp">
    <br><a href = "/home"> Go back to the home page! </a><br>
    <a href = "/food2"> Go to second food picture </a>
    </html>'''

@app.route('/food2')
def food2():
    return '''<html><img width = "400" height = "400" src = "https://domf5oio6qrcr.cloudfront.net/medialibrary/8371/bigstock-Hamburger-And-French-Fries-263887.jpg">
    <br><a href = "/food1"> Go back to the last food picture!</a><br>
    <a href = "/food3"> Go to the third food picture!</a>
    </html>'''

@app.route('/food3')
def food3():
    return '''<html><img width = "400" height = "400" src = "https://www.eatthis.com/wp-content/uploads/sites/4/2019/06/deep-dish-pizza-chicago.jpg?quality=82&strip=1&w=640">
    <br><a href = "/food2"> Go back to the second food picture!</a><br>
    <a href = "/home"> Go back to the home page! </a>
    </html>'''

@app.route('/pet2')
def pet1():
    return '''<html><img width = "400" height = "400" src = "https://www.alouetteanimalhospital.ca/wp-content/uploads/sites/308/2022/06/pettips.jpg">
    <br><a href = "/home"> Go back to the home page! </a><br>
    <a href = "/pet1"> Go to the first pet picture! </a><br>
    <a href = "/pet3"> Go to the third pet picture! </a>
    </html>'''

@app.route('/pet1')
def pet2():
    return '''<html><img width = "400" height = "400" src = "https://images.saymedia-content.com/.image/c_limit%2Ccs_srgb%2Cq_auto:eco%2Cw_700/MTk3MjI5OTczMDA0NjI0OTc5/cute-pet-names.webp">
    <br><a href = "/pet2"> Go back to the second pet picture! </a>
    </html>'''

@app.route('/pet3')
def pet3():
    return '''<html><img width = "400" height = "400" src = "http://yourdost-blog-images.s3-ap-southeast-1.amazonaws.com/wp-content/uploads/2016/01/03165939/Dogs-360x270.jpg">
    <br><a href = "/pet2"> Go back to the second pet page! </a>
    </html>'''

@app.route('/space1')
def space1():
    return '''<html><img width = "400" height = "400" src = "https://images.pexels.com/photos/41162/moon-landing-apollo-11-nasa-buzz-aldrin-41162.jpeg?auto=compress&cs=tinysrgb&w=600">
    <br><a href = "/home"> Go back to the home page! </a><br>
    <a href = "/space2"> Go to second space picture! </a><br>
    <a href = "/space3"> Go to third space picture! </a>
    </html>'''  

@app.route('/space2')
def space2():
    return '''<html><img width = "400" height = "400" src = "https://c02.purpledshub.com/uploads/sites/48/2023/04/facts-about-space-hero.jpg?w=940&webp=1">
    <br><a href = "/space1"> Go back to the first page picture! </a><br>
    <a href = "/space3"> Go to third space picture! </a>
    </html>'''

@app.route('/space3')
def space3():
    return '''<html><img width = "400" height = "400" src = "https://img.freepik.com/free-photo/ultra-detailed-nebula-abstract-wallpaper-4_1562-749.jpg?size=626&ext=jpg">
    <br><a href = "/space2"> Go back to the second space page! </a><br>
    <a href = "/space1"> Go to the first space picture! </a>
    </html>'''


if __name__ == '__main__':
    app.run(debug=True)