# import main Flask class and request object
from flask import Flask, request, send_from_directory, send_file, current_app
import os
# create the Flask app
app = Flask(__name__)

# button
@app.route('/halavi')
def halavi():
    return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"},{"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"}]'

@app.route('/besari')
def besari():
    return '[{"name":"bb","url":"http://10.0.2.2:5000/uploads/bb1.jpg"},{"name":"mcdonalds","url":"http://10.0.2.2:5000/uploads/mcdonalds.jpg"}]'

@app.route('/asiati')
def asiati():
   return '[{"name":"joya","url":"http://10.0.2.2:5000/uploads/joya.jpg"}]'

#all resto
@app.route('/allResto')
def allResto():
    return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"}, {"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"},{"name":"joya","url":"http://10.0.2.2:5000/uploads/joya.jpg"}, {"name":"bb","url":"http://10.0.2.2:5000/uploads/bb1.jpg"},{"name":"mcdonalds","url":"http://10.0.2.2:5000/uploads/mcdonalds.jpg"}]'

#allResto/halavi/besari/asiati
@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def downloadAllResto(filename):
    uploads = os.path.join(current_app.root_path, 'images/resturants')
    return send_from_directory(directory=uploads, path=filename)


#branche
@app.route('/branche/<nameRestaurant>')
def branche(nameRestaurant):
    if(nameRestaurant=="bb"):
        return '[{"city":"ירושלים","address":"רח בלהלה","phone":"09876543","openin":"שעןת פתיחה:08:00-21:00 "},{"city":"ירושלים","address":"רח בלהלה","phone":"09876543","openin":"שעןת פתיחה:08:00-21:00 "},{"city":"כעיח","address":"רח צפםח","phone":"098743","openin":"שעןת פתיחה:08:00-2:00 "},{"city":"ירושלים","address":"רח בלהלה","phone":"09876543","openin":"שעןת פתיחה:08:00-21:00 "}]'



#דף עם לוגו מסעדה ברקע +כפתורים עם כל הקטגוריות בתפריט
# לכל מסעדה יש קטגוריות שונות ולכן נשלח משתנה שהוא שם המסעדה שלפיו נדע מה להציג
#category
@app.route('/category/<resturantName>/<city>', methods=['GET', 'POST'])
def categoy(resturantName,city):
    if(resturantName=='bb'):
        if(city=='ירושלים'):
            #return '[{"name_soug_menu":"סלטים"},{"name_soug_menu":"ביסים"},{"name_soug_menu":"סנדוויצים"},{"name_soug_menu":"בגטים"},{"name_soug_menu":"ארוחות ילדים"}{"name_soug_menu":"טבעוני"},{"name_soug_menu":"מדיום בורגר"},{"name_soug_menu":"המבורגרים"}]'
            return '[{"name_soug_menu":"המבורגרים"},{"name_soug_menu":"מדיום בורגר"},{"name_soug_menu":"טבעוני"},{"name_soug_menu":"סנדוויצים"},{"name_soug_menu":"בגטים"},{"name_soug_menu":"ארוחות ילדים"},{"name_soug_menu":"ביסים"},{"name_soug_menu":"סלטים"}]'
    elif(resturantName=='landwer'):
        return '[{"url":"http://10.0.2.2:5000/uploads/logo.png","name_soug_menu":"המבורגרים"},{"url":"http://10.0.2.2:5000/uploads/cafe.png","name_soug_menu":"מדיום בורגר"},{"url":"http://10.0.2.2:5000/uploads/cafe.png","name_soug_menu":"טבעוני"}]'
    else:
        return '[{"url":"http://10.0.2.2:5000/uploads/logo.png","name_soug_menu":"המבורגרים"}]'

#tafrit
@app.route('/taf/<resturantName>/<city>/<category>', methods=['GET', 'POST'])
def tafrit(resturantName,city,category):
    if(resturantName=="bb"):
        if(city=="ירושלים"):
            if(category=="המבורגרים"):
                return '[{"url":"http://10.0.2.2:5000/upload/harif.png","name":"המבורגר חריף"},{"url":"http://10.0.2.2:5000/upload/קלאסי.png","name":"המבורגר קלאסי"},{"url":"http://10.0.2.2:5000/upload/tale.png","name":"המבורגר טלה"},{"url":"http://10.0.2.2:5000/upload/talebait.png","name":"המבורגר טלה הבית"}]'
            elif(category=="בגטים"):
                    return '[{"url":"http://10.0.2.2:5000/upload/חזהעוף.png","name":"בגאט חזה עוף"},{"url":"http://10.0.2.2:5000/upload/סטייק.png","name":"בגאט סטייק"},{"url":"http://10.0.2.2:5000/upload/פורטובלו.png","name":"באגט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/קורנביף.png","name":"בגאט קורנביף "},{"url":"http://10.0.2.2:5000/upload/שניצל-קריספי.png","name":"בגאט שניצל קריספי"}]'
            elif(category=="טורטיות"):
                    return '[{"url":"http://10.0.2.2:5000/upload/חזה-עוף.png","name":"טורטיה חזה עוף"},{"url":"http://10.0.2.2:5000/upload/סטייק.png","name":"טורטיה סטייק"},{"url":"http://10.0.2.2:5000/upload/פורטובלו.png","name":"טורטיה פורטובלו"},{"url":"http://10.0.2.2:5000/upload/המבורגר.png","name":"טורטיה המבורגר "},{"url":"http://10.0.2.2:5000/upload/שניצל-קריספי.png","name":"טורטיה שניצל קריספי"}]'
            elif(category=="מדיום בורגר"):
                    return '[{"url":"http://10.0.2.2:5000/upload/M1.png","name":"המבורגר M1 "},{"url":"http://10.0.2.2:5000/upload/M4.png","name":"המבורגר M2"}]'
            elif(category=="סנדוויצים"):
                        return '[{"url":"http://10.0.2.2:5000/upload/חזה-עוף.png","name":"סנדוויץ חזה עוף"},{"url":"http://10.0.2.2:5000/upload/סטייק.png","name":"סנדוויץ סטייק"},{"url":"http://10.0.2.2:5000/upload/פורטובלו.png","name":"סנדוויץ פורטובלו"},{"url":"http://10.0.2.2:5000/upload/קורנביף.png","name":"סנדוויץ קורנביף "},{"url":"http://10.0.2.2:5000/upload/שניצל-קריספי.png","name":"סנדוויץ שניצל קריספי"}]'
            elif(category=="ארוחות ילדים"):
                    return '[{"url":"http://10.0.2.2:5000/upload/ארוחת-המבורגר.png","name":"ארוחת המבורגר"},{"url":"http://10.0.2.2:5000/upload/ארוחת-שניצלונים.png","name":"ארוחת שניצלונים"}]'
            elif(category=="ביסים"):
                    return '[{"url":"http://10.0.2.2:5000/upload/כנפיים.png","name":"כנפיים"},{"url":"http://10.0.2.2:5000/upload/שניצלונים.png","name":"שניצלונים"},{"url":"http://10.0.2.2:5000/upload/סיגר-הבית.png","name":"סיגר הבית"}]'
            elif(category=="טבעוני"):
                    return '[{"url":"http://10.0.2.2:5000/upload/ביונד.png","name":"המבורגר ביונד"},{"url":"http://10.0.2.2:5000/upload/פורטבלו.png","name":"המבורגר פורטובלו"},{"url":"http://10.0.2.2:5000/upload/פור3.png","name":"בגאט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/פורטובלו.png","name":"טורטיה פורטובלו"}]'
            elif(category=="סלטים"):
                    return '[{"url":"http://10.0.2.2:5000/upload/שוק.png","name":"סלט שוק"},{"url":"http://10.0.2.2:5000/upload/אסייתי.png","name":"סלט אסייתי"},{"url":"http://10.0.2.2:5000/upload/קיסרעלים.png","name":"סלט קיסר עלים}]'


#tafrit
#image,name resto - michtane, 
@app.route('/upload/<typeres>/<filename>', methods=['GET', 'POST'])
def downloadtaf(typeres,filename):
    uploads = os.path.join(current_app.root_path, 'images/bb/'+typeres)
    return send_from_directory(directory=uploads, path=filename)

#tafrit
@app.route('/background/<resturantName>')
def backgroundpic(resturantName):
    uploads = os.path.join(current_app.root_path, 'resturants') #lama resturant??
    return send_from_directory(directory=uploads, path=resturantName)


#details
@app.route('/detail/<resturantName>/<city>/<category>/<mana>')
def detail(resturantName,city,category,mana):
    if(resturantName=="bb"):
        if(city=="ירושלים"):
            if(category=="המבורגרים"):
                if(mana=="המבורגר חריף"):
                    return '{"url":"http://10.0.2.2:5000/upload/harif.png","name":"המבורגר חריף","description":"fghjk","price":"24"}'
                if(mana=="המבורגר קלאסי"):
                    return '[{"url":"http://10.0.2.2:5000/upload/קלאסי.png","name":"המבורגר קלאסי","description":"fghjk","price":"24"}]'
                if(mana=="המבורגר טלה"):
                    return '[{"url":"http://10.0.2.2:5000/upload/tale.png","name":"המבורגר טלה","description":"fghjk","price":"24"}]'
                if(mana=="המבורגר טלה הבית"):
                    return '[{"url":"http://10.0.2.2:5000/upload/talebait.png","name":"המבורגר טלה הבית","description":"fghjk","price":"24"}]'
            elif(category=="ארוחות ילדים"):
                if(mana=="ארוחת-המבורגר"):
                    return '[{"url":"http://10.0.2.2:5000/upload/ארוחות-המבורגר.png","name":"ארוחת-המבורגר","description":"fghjk","price":"24"}]'
                if(mana=="ארוחת-שניצלונים"):
                    return '[{"url":"http://10.0.2.2:5000/upload/ארוחות-שניצלונים.png","name":"ארוחת-שניצלונים","description":"fghjk","price":"24"}]'

#panier
@app.route('/panier')
def panier():
    return '[{"url":"http://10.0.2.2:5000/upload/harif.png","nameM":"המבורגר חריף","nameP":"8","nameQ":"4"}]'

@app.route('/upload/<filename>', methods=['GET', 'POST'])
def downloadPanier(filename):
    uploads = os.path.join(current_app.root_path, 'images/bb/המבורגרים')
    return send_from_directory(directory=uploads,path=filename)

@app.route('/upload/<filename>', methods=['GET', 'POST'])
def downloadPanier1(filename):
    uploads = os.path.join(current_app.root_path, 'images/bb/ארוחות ילדים')
    return send_from_directory(directory=uploads,path=filename)

@app.route('/upload/<filename>', methods=['GET', 'POST'])
def downloadPanier2(filename):
    uploads = os.path.join(current_app.root_path, 'images/bb/טבעוני')
    return send_from_directory(directory=uploads,path=filename)

#effacer?
@app.route('/food/<filename>')
def food(filename):
    if(filename == "cafe-cafe"):
        return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"},{"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"},{"name":"joya","url":"http://10.0.2.2:5000/uploads/joya.jpg"},{"name":"bb","url":"http://10.0.2.2:5000/uploads/bb1.jpg"},{"name":"mcdonalds","url":"http://10.0.2.2:5000/uploads/mcdonalds.jpg"}]'
    else:
        return '[{"name":"cafe-cafe","url":"http://10.0.2.2:5000/uploads/cafecafe.jpg"}]'



#ma ze????
@app.route('/<resturnat>/<filename>', methods=['GET', 'POST']) #שם המסעדה +מנה
def download1(resturant,filename):
    uploads = os.path.join(current_app.root_path, 'images/'+resturant)
    return send_from_directory(directory=uploads, path=filename) 






if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)