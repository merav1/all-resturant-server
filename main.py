from flask import Flask, request, send_from_directory, send_file, current_app
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from waitress import serve


# create the Flask app
app = Flask(__name__)
count=1
cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://allrestaurant-7ab8f-default-rtdb.firebaseio.com/'
    })

# button
@app.route('/halavi')
def halavi():
    ref = db.reference('/menu/halavi')
    return str(ref.get())

@app.route('/besari')
def besari():
    ref = db.reference('/menu/besari') 
    return str(ref.get())

@app.route('/asiati')
def asiati():
    ref = db.reference('/menu/asiati') 
    return str(ref.get())

#all resto
@app.route('/allResto')
def allResto():
    ref = db.reference('/menu/allResto') 
    return str(ref.get())
    # return '[{"name":"cafe-Cafe","url":"http://speedclient.herokuapp.com/uploads/cafecafe.bmp"}, {"name":"landwer","url":"http://speedclient.herokuapp.com/uploads/landwer.bmp"},{"name":"joya","url":"http://speedclient.herokuapp.com/uploads/joya.bmp"}, {"name":"bb","url":"http://speedclient.herokuapp.com/uploads/bb1.bmp"},{"name":"mcDonalds","url":"http://speedclient.herokuapp.com/uploads/mcdonalds.bmp"}]'

#allResto/halavi/besari/asiati
@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def downloadAllResto(filename):
    uploads = os.path.join(current_app.root_path, 'images/resturants')
    return send_from_directory(directory=uploads, path=filename)


#branche
@app.route('/branche/<nameRestaurant>')
def branche(nameRestaurant):
    ref = db.reference('/branche'+'/'+nameRestaurant) 
    #print(str(ref.get()))
    return str(ref.get())



#דף עם לוגו מסעדה ברקע +כפתורים עם כל הקטגוריות בתפריט
# לכל מסעדה יש קטגוריות שונות ולכן נשלח משתנה שהוא שם המסעדה שלפיו נדע מה להציג
#category

@app.route('/category/<resturantName>/<city>', methods=['GET', 'POST'])
def category(resturantName,city):
    ref = db.reference('/category'+'/'+resturantName+'/'+city)
    #print(str(ref.get()))
    return str(ref.get())


#tafrit
@app.route('/taf/<resturantName>/<city>/<category>', methods=['GET', 'POST'])
def tafrit(resturantName,city,category):
    ref = db.reference('/taf'+'/'+resturantName+'/'+city+'/'+category)
    #print(str(ref.get()))
    return str(ref.get())

#tafrit
@app.route('/order', methods=[ 'POST'])
def order():
    data=request.data
    jres=json.loads(data)
    
    ref=db.reference('/orders')
    ref.push({
        str(count) : {
            jres["details"]["resturantname"] : {
                jres["details"]["city"] : {
                    "time" : jres["details"]["time"],
                    "manot" : jres["manot"]
                }
            }
        }
    })
    count=count+1
    print(data)
    return ""


#tafrit
#image,name resto - michtane, 
@app.route('/upload/<typeres>/<filename>', methods=['GET', 'POST'])
def downloadtaf(typeres,filename):
    upload = os.path.join(current_app.root_path, 'images/BurgersBar/'+typeres)
    return send_from_directory(directory=upload,path=filename)

@app.route('/upload1/<typeres>/<filename>', methods=['GET', 'POST'])
def downloadtafl(typeres,filename):
    upload1 = os.path.join(current_app.root_path, 'images/landwer/'+typeres)
    return send_from_directory(directory=upload1,path=filename)

@app.route('/upload2/<typeres>/<filename>', methods=['GET', 'POST'])
def downloadtaf2(typeres,filename):
    upload2 = os.path.join(current_app.root_path, 'images/Japanika/'+typeres)
    return send_from_directory(directory=upload2,path=filename)

#tafrit
@app.route('/background/<resturantName>')
def backgroundpic(resturantName):
    uploads = os.path.join(current_app.root_path, 'resturants') #lama resturant??
    return send_from_directory(directory=uploads, path=resturantName)


#details
@app.route('/detail/<resturantName>/<city>/<category>/<mana>')
def detail(resturantName,city,category,mana):
    ref = db.reference('/detail'+'/'+resturantName+'/'+city+'/'+category+'/'+mana)
    #print(str(ref.get()))
    return str(ref.get())


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    # run app in debug mode on port 5000
    #app.run(debug=True, port=5000)
    serve(app,host="0.0.0.0",port=port)