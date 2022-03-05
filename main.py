# import main Flask class and request object
from flask import Flask, request, send_from_directory, send_file, current_app
import os
# create the Flask app
app = Flask(__name__)


@app.route('/allResto')
def json_example():
    return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"},{"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"},{"name":"joya","url":"http://10.0.2.2:5000/uploads/joya.jpg"},{"name":"bb","url":"http://10.0.2.2:5000/uploads/bb1.jpg"},{"name":"mcdonalds","url":"http://10.0.2.2:5000/uploads/mcdonalds.jpg"}]'

@app.route('/halavi')
def json_example1():
    return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"},{"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"}]'

@app.route('/besari')
def json_example2():
    return '[{"name":"bb","url":"http://10.0.2.2:5000/uploads/bb1.jpg"},{"name":"mcdonalds","url":"http://10.0.2.2:5000/uploads/mcdonalds.jpg"}]'

@app.route('/asiati')
def json_example3():
    return '[{"name":"joya","url":"http://10.0.2.2:5000/uploads/joya.jpg"}]'

@app.route('/food/<filename>')
def food(filename):
    if(filename == "cafe-cafe"):
        return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"},{"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"},{"name":"joya","url":"http://10.0.2.2:5000/uploads/joya.jpg"},{"name":"bb","url":"http://10.0.2.2:5000/uploads/bb1.jpg"},{"name":"mcdonalds","url":"http://10.0.2.2:5000/uploads/mcdonalds.jpg"}]'
    else:
        return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"}]'


@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, 'images/resturants')
    return send_from_directory(directory=uploads, path=filename)

@app.route('/manot/<resturantName>')
def json_example6(resturantName):
    if(resturantName=="mcdonalds"):
        return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"},{"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"},{"name":"joya","url":"http://10.0.2.2:5000/uploads/joya.jpg"},{"name":"bb","url":"http://10.0.2.2:5000/uploads/bb1.jpg"},{"name":"mcdonalds","url":"http://10.0.2.2:5000/uploads/mcdonalds.jpg"}]'
    elif(resturantName=="bb"):
        return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"},{"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"},{"name":"joya","url":"http://10.0.2.2:5000/uploads/joya.jpg"},{"name":"bb","url":"http://10.0.2.2:5000/uploads/bb1.jpg"},{"name":"mcdonalds","url":"http://10.0.2.2:5000/uploads/mcdonalds.jpg"}]'

@app.route('/<resturnat>/<filename>', methods=['GET', 'POST'])
def download(resturant,filename):
    uploads = os.path.join(current_app.root_path, 'images/'+resturant)
    return send_from_directory(directory=uploads, path=filename)

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = '/images/cafecafe.png'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
