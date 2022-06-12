import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred,{
'databaseURL' : 'https://allrestaurant-7ab8f-default-rtdb.firebaseio.com/'})

ref = db.reference('/menu')
ref.set(    {
    
    'besari':
    [{"name":"BurgersBar","url":"http://10.0.2.2:5000/uploads/BurgersBar.jpg"},{"name":"McDonalds","url":"http://10.0.2.2:5000/uploads/McDonalds.jpeg"}]
    ,'halavi':
    [{"name":"Cafe-Cafe","url":"http://10.0.2.2:5000/uploads/cafe-cafe.jpeg"},{"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"}]
    ,'asiati':
    [{"name":"Japanika","url":"http://10.0.2.2:5000/uploads/japanika.jpg"}]
    ,'allResto':
    [{"name":"Cafe-Cafe","url":"http://10.0.2.2:5000/uploads/cafe-cafe.jpeg"}, {"name":"landwer","url":"http://10.0.2.2:5000/uploads/landwer.jpg"},{"name":"Japanika","url":"http://10.0.2.2:5000/uploads/japanika.jpg"}, {"name":"BurgersBar","url":"http://10.0.2.2:5000/uploads/BurgersBar.jpg"},{"name":"McDonalds","url":"http://10.0.2.2:5000/uploads/McDonalds.jpeg"}]
})

ref = db.reference('/branche')
ref.set(   {
    'BurgersBar':
   [{"city":"אשדוד","address":"הגדוד העברי","phone":"079-674-4316","openin":"א-ה: 11:00-00:00"},{"city":"ירושלים","address":"מלחה","phone":"079-5912242","openin":"א-ה: 11:00-23:30"},{"city":"רעננה","address":"מרכז טאגור","phone":"079-591-2242","openin":"א-ה: 11:00-23:00"},{"city":"נתניה","address":"גד מחנה","phone":"079-866-9677","openin":"א-ה: 11:00-01:30"}]
    ,'landwer':
    [{"city":"אשדוד","address":"דרך הרכבת 1","phone":"079-6378070","openin":"א-ה: 08:00-23:00"},{"city":"ירושלים","address":"דוד רמז 4","phone":"079-5877988","openin":"א-ה: 08:00-23:30"},{"city":"רעננה","address":"הסדנא 6","phone":"079-7689004","openin":"א-ה: 08:00-23:00"},{"city":"נתניה","address":"עובד בן עמי 10","phone":"079-9516170","openin":"א-ה: 08:00-23:30"}]
    ,'Japanika':
    [{"city":"אשדוד","address":"ז’בוטינסקי 43","phone":"079-6378070","openin":"א-ה: 11:00-16:00"},{"city":"ירושלים","address":"שדרות יצחק רבין 10","phone":"079-5877988","openin":"א-ה: 11:00-18:30"},{"city":"רעננה","address":"אחוזה 95","phone":"079-7689004","openin":"א-ה: 12:00-00:00"},{"city":"נתניה","address":"גיבורי ישראל 5 ","phone":"079-9516170","openin":"א-ה: 11:00-17:30"}]
})

ref = db.reference('/category')
ref.set(   {
        'BurgersBar':
        {
            'ירושלים':
                [{"icon":"http://10.0.2.2:5000/upload/icon/hamburger.jpng","name_soug_menu":"המבורגרים"},{"icon":"http://10.0.2.2:5000/upload/icon/bisim.jpng","name_soug_menu":"מדיום בורגר"},{"icon":"http://10.0.2.2:5000/upload/icon/vegan.jpng","name_soug_menu":"טבעוני"},{"icon":"http://10.0.2.2:5000/upload/icon/tortia.jpng","name_soug_menu":"טורטיות"},{"icon":"http://10.0.2.2:5000/upload/icon/sandwich.jpng","name_soug_menu":"סנדוויצים"},{"icon":"http://10.0.2.2:5000/upload/icon/baguet.jpng","name_soug_menu":"בגטים"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.jpng","name_soug_menu":"ארוחות ילדים"},{"name_soug_menu":"ביסים","icon":"http://10.0.2.2:5000/upload/icon/salad.jpng","name_soug_menu":"סלטים"}]
            ,'אשדוד':
                [{"icon":"http://10.0.2.2:5000/upload/icon/hamburger.jpng","name_soug_menu":"המבורגרים"},{"icon":"http://10.0.2.2:5000/upload/icon/bisim.jpng","name_soug_menu":"מדיום בורגר"},{"icon":"http://10.0.2.2:5000/upload/icon/vegan.jpng","name_soug_menu":"טבעוני"},{"icon":"http://10.0.2.2:5000/upload/icon/tortia.jpng","name_soug_menu":"טורטיות"},{"icon":"http://10.0.2.2:5000/upload/icon/sandwich.jpng","name_soug_menu":"סנדוויצים"},{"icon":"http://10.0.2.2:5000/upload/icon/baguet.jpng","name_soug_menu":"בגטים"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.jpng","name_soug_menu":"ארוחות ילדים"},{"name_soug_menu":"ביסים","icon":"http://10.0.2.2:5000/upload/icon/salad.jpng","name_soug_menu":"סלטים"}]
            ,'נתניה':
                [{"icon":"http://10.0.2.2:5000/upload/icon/hamburger.jpng","name_soug_menu":"המבורגרים"},{"icon":"http://10.0.2.2:5000/upload/icon/bisim.jpng","name_soug_menu":"מדיום בורגר"},{"icon":"http://10.0.2.2:5000/upload/icon/vegan.jpng","name_soug_menu":"טבעוני"},{"icon":"http://10.0.2.2:5000/upload/icon/tortia.jpng","name_soug_menu":"טורטיות"},{"icon":"http://10.0.2.2:5000/upload/icon/sandwich.jpng","name_soug_menu":"סנדוויצים"},{"icon":"http://10.0.2.2:5000/upload/icon/baguet.jpng","name_soug_menu":"בגטים"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.jpng","name_soug_menu":"ארוחות ילדים"},{"name_soug_menu":"ביסים","icon":"http://10.0.2.2:5000/upload/icon/salad.jpng","name_soug_menu":"סלטים"}]
            ,'רעננה':
                [{"icon":"http://10.0.2.2:5000/upload/icon/hamburger.jpng","name_soug_menu":"המבורגרים"},{"icon":"http://10.0.2.2:5000/upload/icon/bisim.jpng","name_soug_menu":"מדיום בורגר"},{"icon":"http://10.0.2.2:5000/upload/icon/vegan.jpng","name_soug_menu":"טבעוני"},{"icon":"http://10.0.2.2:5000/upload/icon/tortia.jpng","name_soug_menu":"טורטיות"},{"icon":"http://10.0.2.2:5000/upload/icon/sandwich.jpng","name_soug_menu":"סנדוויצים"},{"icon":"http://10.0.2.2:5000/upload/icon/baguet.jpng","name_soug_menu":"בגטים"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.jpng","name_soug_menu":"ארוחות ילדים"},{"name_soug_menu":"ביסים","icon":"http://10.0.2.2:5000/upload/icon/salad.jpng","name_soug_menu":"סלטים"}]
        
        }
        ,'landwer':
        {
            'ירושלים':
                [{"icon":"http://10.0.2.2:5000/upload1/salade/salade.png","name_soug_menu":"סלטים"},{"icon":"http://10.0.2.2:5000/upload/medium/maine.png","name_soug_menu":"עיקריות"},{"icon":"http://10.0.2.2:5000/upload/icon/pasta.png","name_soug_menu":"פסטה ופיצה"},{"icon":"http://10.0.2.2:5000/upload/icon/toast.png","name_soug_menu":"כריכים וטוסטים"},{"icon":"http://10.0.2.2:5000/upload/icon/breakfast.png","name_soug_menu":"ארוחות בוקר"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.png","name_soug_menu":"ארוחות ילדים"}]
            ,'אשדוד':
                [{"icon":"http://10.0.2.2:5000/upload/salade/salade.png","name_soug_menu":"סלטים"},{"icon":"http://10.0.2.2:5000/upload/medium/maine.png","name_soug_menu":"עיקריות"},{"icon":"http://10.0.2.2:5000/upload/icon/pasta.png","name_soug_menu":"פסטה ופיצה"},{"icon":"http://10.0.2.2:5000/upload/icon/toast.png","name_soug_menu":"כריכים וטוסטים"},{"icon":"http://10.0.2.2:5000/upload/icon/breakfast.png","name_soug_menu":"ארוחות בוקר"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.png","name_soug_menu":"ארוחות ילדים"}]
            ,'נתניה':
                [{"icon":"http://10.0.2.2:5000/upload/salade/salade.png","name_soug_menu":"סלטים"},{"icon":"http://10.0.2.2:5000/upload/medium/maine.png","name_soug_menu":"עיקריות"},{"icon":"http://10.0.2.2:5000/upload/icon/pasta.png","name_soug_menu":"פסטה ופיצה"},{"icon":"http://10.0.2.2:5000/upload/icon/toast.png","name_soug_menu":"כריכים וטוסטים"},{"icon":"http://10.0.2.2:5000/upload/icon/breakfast.png","name_soug_menu":"ארוחות בוקר"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.png","name_soug_menu":"ארוחות ילדים"}]
            ,'רעננה':
                [{"icon":"http://10.0.2.2:5000/upload/salade/salade.png","name_soug_menu":"סלטים"},{"icon":"http://10.0.2.2:5000/upload/medium/maine.png","name_soug_menu":"עיקריות"},{"icon":"http://10.0.2.2:5000/upload/icon/pasta.png","name_soug_menu":"פסטה ופיצה"},{"icon":"http://10.0.2.2:5000/upload/icon/toast.png","name_soug_menu":"כריכים וטוסטים"},{"icon":"http://10.0.2.2:5000/upload/icon/breakfast.png","name_soug_menu":"ארוחות בוקר"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.png","name_soug_menu":"ארוחות ילדים"}]
        
        }
        ,'Japanika':
        {
            'ירושלים':
                [{"icon":"http://10.0.2.2:5000/upload1/salade/salade.png","name_soug_menu":"אורז וגריל"},{"icon":"http://10.0.2.2:5000/upload/medium/maine.png","name_soug_menu":"מנות ווק"},{"icon":"http://10.0.2.2:5000/upload/icon/pasta.png","name_soug_menu":" ספיישל סושי"},{"icon":"http://10.0.2.2:5000/upload/icon/toast.png","name_soug_menu":"מרקים"},{"icon":"http://10.0.2.2:5000/upload/icon/breakfast.png","name_soug_menu":"ארוחות ילדים"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.png","name_soug_menu":"מנות פתיחה"}]
            ,'אשדוד':
                [{"icon":"http://10.0.2.2:5000/upload1/salade/salade.png","name_soug_menu":"אורז וגריל"},{"icon":"http://10.0.2.2:5000/upload/medium/maine.png","name_soug_menu":"מנות ווק"},{"icon":"http://10.0.2.2:5000/upload/icon/pasta.png","name_soug_menu":" ספיישל סושי"},{"icon":"http://10.0.2.2:5000/upload/icon/toast.png","name_soug_menu":"מרקים"},{"icon":"http://10.0.2.2:5000/upload/icon/breakfast.png","name_soug_menu":"ארוחות ילדים"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.png","name_soug_menu":"מנות פתיחה"}]
            ,'נתניה':
                [{"icon":"http://10.0.2.2:5000/upload1/salade/salade.png","name_soug_menu":"אורז וגריל"},{"icon":"http://10.0.2.2:5000/upload/medium/maine.png","name_soug_menu":"מנות ווק"},{"icon":"http://10.0.2.2:5000/upload/icon/pasta.png","name_soug_menu":" ספיישל סושי"},{"icon":"http://10.0.2.2:5000/upload/icon/toast.png","name_soug_menu":"מרקים"},{"icon":"http://10.0.2.2:5000/upload/icon/breakfast.png","name_soug_menu":"ארוחות ילדים"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.png","name_soug_menu":"מנות פתיחה"}]
            ,'רעננה':
                [{"icon":"http://10.0.2.2:5000/upload1/salade/salade.png","name_soug_menu":"אורז וגריל"},{"icon":"http://10.0.2.2:5000/upload/medium/maine.png","name_soug_menu":"מנות ווק"},{"icon":"http://10.0.2.2:5000/upload/icon/pasta.png","name_soug_menu":" ספיישל סושי"},{"icon":"http://10.0.2.2:5000/upload/icon/toast.png","name_soug_menu":"מרקים"},{"icon":"http://10.0.2.2:5000/upload/icon/breakfast.png","name_soug_menu":"ארוחות ילדים"},{"icon":"http://10.0.2.2:5000/upload/icon/kids.png","name_soug_menu":"מנות פתיחה"}]
        
        }
})

ref = db.reference('/taf')
ref.set({
    'BurgersBar':
        {
            'ירושלים':
                {
                 'המבורגרים':
                    [{"url":"http://10.0.2.2:5000/upload/המבורגרים/harif.png","name":"המבורגר חריף"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/classi.png","name":"המבורגר קלאסי"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/tale.png","name":"המבורגר טלה"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/talebait.png","name":"המבורגר טלה הבית"}]
                    ,'בגטים':
                    [{"url":"http://10.0.2.2:5000/upload/baguet/סטייק.png","name":"בגט סטייק"},{"url":"http://10.0.2.2:5000/upload/baguet/פורטובלו.png","name":"בגט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/baguet/קורנביף.png","name":"בגט קורנביף "},{"url":"http://10.0.2.2:5000/upload/baguet/שניצל-קריספי.png","name":"בגט שניצל קריספי"}]
                    ,'טורטיות':
                    [{"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה חזה עוף"},{"url":"http://10.0.2.2:5000/upload/tortia/סטייק.png","name":"טורטיה סטייק"},{"url":"http://10.0.2.2:5000/upload/tortia/פורטובלו.png","name":"טורטיה פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה המבורגר "},{"url":"http://10.0.2.2:5000/upload/tortia/שניצל-קריספי.png","name":"טורטיה שניצל קריספי"}]
                    ,'מדיום בורגר':
                    [{"url":"http://10.0.2.2:5000/upload/medium/M1.png","name":"המבורגר M1 "},{"url":"http://10.0.2.2:5000/upload/medium/M4.png","name":"המבורגר M2"}]
                    ,'סנדוויצים':
                    [{"url":"http://10.0.2.2:5000/upload/sandwich/חזה-עוף.png","name":"סנדוויץ חזה עוף"},{"url":"http://10.0.2.2:5000/upload/sandwich/סטייק.png","name":"סנדוויץ סטייק"},{"url":"http://10.0.2.2:5000/upload/sandwich/פורטבלו.png","name":"סנדוויץ פורטובלו"},{"url":"http://10.0.2.2:5000/upload/sandwich/קורנביף.png","name":"סנדוויץ קורנביף "},{"url":"http://10.0.2.2:5000/upload/sandwich/שניצל-קריספי.png","name":"סנדוויץ שניצל קריספי"}]
                    ,'ארוחות ילדים':
                    [{"url":"http://10.0.2.2:5000/upload/kids/ארוחת-המבורגר.png","name":"ארוחת-המבורגר"},{"url":"http://10.0.2.2:5000/upload/kids/ארוחת-שניצלונים.png","name":"ארוחת-שניצלונים"}]
                    ,'ביסים':
                    [{"url":"http://10.0.2.2:5000/upload/bisim/כנפיים.png","name":"כנפיים"},{"url":"http://10.0.2.2:5000/upload/bisim/שניצלונים.png","name":"שניצלונים"},{"url":"http://10.0.2.2:5000/upload/bisim/סיגר-הבית.png","name":"סיגר הבית"}]
                    ,'טבעוני':
                    [{"url":"http://10.0.2.2:5000/upload/tivoni/ביונד.png","name":"המבורגר ביונד"},{"url":"http://10.0.2.2:5000/upload/tivoni/פורטבלו.png","name":"המבורגר פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פור3.png","name":"בגט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פורטובלו.png","name":"טורטיה פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פור.png","name":"פורטובלו"}]
                    ,'סלטים':
                    [{"url":"http://10.0.2.2:5000/upload/salade/שוק.png","name":"סלט שוק"},{"url":"http://10.0.2.2:5000/upload/salade/אסייתי.png","name":"סלט אסייתי"},{"url":"http://10.0.2.2:5000/upload/salade/קיסרעלים.png","name":"סלט קיסר עלים"}]

                   
                }
                ,'רעננה':
                {
                        'המבורגרים':
                        [{"url":"http://10.0.2.2:5000/upload/המבורגרים/harif.png","name":"המבורגר חריף"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/classi.png","name":"המבורגר קלאסי"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/tale.png","name":"המבורגר טלה"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/talebait.png","name":"המבורגר טלה הבית"}]
                        ,'בגטים':
                        [{"url":"http://10.0.2.2:5000/upload/baguet/סטייק.png","name":"בגט סטייק"},{"url":"http://10.0.2.2:5000/upload/baguet/פורטובלו.png","name":"בגט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/baguet/קורנביף.png","name":"בגט קורנביף "},{"url":"http://10.0.2.2:5000/upload/baguet/שניצל-קריספי.png","name":"בגט שניצל קריספי"}]
                        ,'טורטיות':
                        [{"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה חזה עוף"},{"url":"http://10.0.2.2:5000/upload/tortia/סטייק.png","name":"טורטיה סטייק"},{"url":"http://10.0.2.2:5000/upload/tortia/פורטובלו.png","name":"טורטיה פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה המבורגר "},{"url":"http://10.0.2.2:5000/upload/tortia/שניצל-קריספי.png","name":"טורטיה שניצל קריספי"}]
                        ,'מדיום בורגר':
                        [{"url":"http://10.0.2.2:5000/upload/medium/M1.png","name":"המבורגר M1 "},{"url":"http://10.0.2.2:5000/upload/medium/M4.png","name":"המבורגר M2"}]
                        ,'סנדוויצים':
                        [{"url":"http://10.0.2.2:5000/upload/sandwich/חזה-עוף.png","name":"סנדוויץ חזה עוף"},{"url":"http://10.0.2.2:5000/upload/sandwich/סטייק.png","name":"סנדוויץ סטייק"},{"url":"http://10.0.2.2:5000/upload/sandwich/פורטבלו.png","name":"סנדוויץ פורטובלו"},{"url":"http://10.0.2.2:5000/upload/sandwich/קורנביף.png","name":"סנדוויץ קורנביף "},{"url":"http://10.0.2.2:5000/upload/sandwich/שניצל-קריספי.png","name":"סנדוויץ שניצל קריספי"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload/kids/ארוחת-המבורגר.png","name":"ארוחת-המבורגר"},{"url":"http://10.0.2.2:5000/upload/kids/ארוחת-שניצלונים.png","name":"ארוחת-שניצלונים"}]
                        ,'ביסים':
                        [{"url":"http://10.0.2.2:5000/upload/bisim/כנפיים.png","name":"כנפיים"},{"url":"http://10.0.2.2:5000/upload/bisim/שניצלונים.png","name":"שניצלונים"},{"url":"http://10.0.2.2:5000/upload/bisim/סיגר-הבית.png","name":"סיגר הבית"}]
                        ,'טבעוני':
                        [{"url":"http://10.0.2.2:5000/upload/tivoni/ביונד.png","name":"המבורגר ביונד"},{"url":"http://10.0.2.2:5000/upload/tivoni/פורטבלו.png","name":"המבורגר פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פור3.png","name":"בגט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פורטובלו.png","name":"טורטיה פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פור.png","name":"פורטובלו"}]
                        ,'סלטים':
                        [{"url":"http://10.0.2.2:5000/upload/salade/שוק.png","name":"סלט שוק"},{"url":"http://10.0.2.2:5000/upload/salade/אסייתי.png","name":"סלט אסייתי"},{"url":"http://10.0.2.2:5000/upload/salade/קיסרעלים.png","name":"סלט קיסר עלים"}]

                }
                ,'נתניה':
                {
                        'המבורגרים':
                        [{"url":"http://10.0.2.2:5000/upload/המבורגרים/harif.png","name":"המבורגר חריף"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/classi.png","name":"המבורגר קלאסי"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/tale.png","name":"המבורגר טלה"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/talebait.png","name":"המבורגר טלה הבית"}]
                        ,'בגטים':
                        [{"url":"http://10.0.2.2:5000/upload/baguet/סטייק.png","name":"בגט סטייק"},{"url":"http://10.0.2.2:5000/upload/baguet/פורטובלו.png","name":"בגט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/baguet/קורנביף.png","name":"בגט קורנביף "},{"url":"http://10.0.2.2:5000/upload/baguet/שניצל-קריספי.png","name":"בגט שניצל קריספי"}]
                        ,'טורטיות':
                        [{"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה חזה עוף"},{"url":"http://10.0.2.2:5000/upload/tortia/סטייק.png","name":"טורטיה סטייק"},{"url":"http://10.0.2.2:5000/upload/tortia/פורטובלו.png","name":"טורטיה פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה המבורגר "},{"url":"http://10.0.2.2:5000/upload/tortia/שניצל-קריספי.png","name":"טורטיה שניצל קריספי"}]
                        ,'מדיום בורגר':
                        [{"url":"http://10.0.2.2:5000/upload/medium/M1.png","name":"המבורגר M1 "},{"url":"http://10.0.2.2:5000/upload/medium/M4.png","name":"המבורגר M2"}]
                        ,'סנדוויצים':
                        [{"url":"http://10.0.2.2:5000/upload/sandwich/חזה-עוף.png","name":"סנדוויץ חזה עוף"},{"url":"http://10.0.2.2:5000/upload/sandwich/סטייק.png","name":"סנדוויץ סטייק"},{"url":"http://10.0.2.2:5000/upload/sandwich/פורטבלו.png","name":"סנדוויץ פורטובלו"},{"url":"http://10.0.2.2:5000/upload/sandwich/קורנביף.png","name":"סנדוויץ קורנביף "},{"url":"http://10.0.2.2:5000/upload/sandwich/שניצל-קריספי.png","name":"סנדוויץ שניצל קריספי"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload/kids/ארוחת-המבורגר.png","name":"ארוחת-המבורגר"},{"url":"http://10.0.2.2:5000/upload/kids/ארוחת-שניצלונים.png","name":"ארוחת-שניצלונים"}]
                        ,'ביסים':
                        [{"url":"http://10.0.2.2:5000/upload/bisim/כנפיים.png","name":"כנפיים"},{"url":"http://10.0.2.2:5000/upload/bisim/שניצלונים.png","name":"שניצלונים"},{"url":"http://10.0.2.2:5000/upload/bisim/סיגר-הבית.png","name":"סיגר הבית"}]
                        ,'טבעוני':
                        [{"url":"http://10.0.2.2:5000/upload/tivoni/ביונד.png","name":"המבורגר ביונד"},{"url":"http://10.0.2.2:5000/upload/tivoni/פורטבלו.png","name":"המבורגר פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פור3.png","name":"בגט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פורטובלו.png","name":"טורטיה פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פור.png","name":"פורטובלו"}]
                        ,'סלטים':
                        [{"url":"http://10.0.2.2:5000/upload/salade/שוק.png","name":"סלט שוק"},{"url":"http://10.0.2.2:5000/upload/salade/אסייתי.png","name":"סלט אסייתי"},{"url":"http://10.0.2.2:5000/upload/salade/קיסרעלים.png","name":"סלט קיסר עלים"}]

                }
                ,'אשדוד':
                {
                        'המבורגרים':
                        [{"url":"http://10.0.2.2:5000/upload/המבורגרים/harif.png","name":"המבורגר חריף"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/classi.png","name":"המבורגר קלאסי"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/tale.png","name":"המבורגר טלה"},{"url":"http://10.0.2.2:5000/upload/המבורגרים/talebait.png","name":"המבורגר טלה הבית"}]
                        ,'בגטים':
                        [{"url":"http://10.0.2.2:5000/upload/baguet/סטייק.png","name":"בגט סטייק"},{"url":"http://10.0.2.2:5000/upload/baguet/פורטובלו.png","name":"בגט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/baguet/קורנביף.png","name":"בגט קורנביף "},{"url":"http://10.0.2.2:5000/upload/baguet/שניצל-קריספי.png","name":"בגט שניצל קריספי"}]
                        ,'טורטיות':
                        [{"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה חזה עוף"},{"url":"http://10.0.2.2:5000/upload/tortia/סטייק.png","name":"טורטיה סטייק"},{"url":"http://10.0.2.2:5000/upload/tortia/פורטובלו.png","name":"טורטיה פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה המבורגר "},{"url":"http://10.0.2.2:5000/upload/tortia/שניצל-קריספי.png","name":"טורטיה שניצל קריספי"}]
                        ,'מדיום בורגר':
                        [{"url":"http://10.0.2.2:5000/upload/medium/M1.png","name":"המבורגר M1 "},{"url":"http://10.0.2.2:5000/upload/medium/M4.png","name":"המבורגר M2"}]
                        ,'סנדוויצים':
                        [{"url":"http://10.0.2.2:5000/upload/sandwich/חזה-עוף.png","name":"סנדוויץ חזה עוף"},{"url":"http://10.0.2.2:5000/upload/sandwich/סטייק.png","name":"סנדוויץ סטייק"},{"url":"http://10.0.2.2:5000/upload/sandwich/פורטבלו.png","name":"סנדוויץ פורטובלו"},{"url":"http://10.0.2.2:5000/upload/sandwich/קורנביף.png","name":"סנדוויץ קורנביף "},{"url":"http://10.0.2.2:5000/upload/sandwich/שניצל-קריספי.png","name":"סנדוויץ שניצל קריספי"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload/kids/ארוחת-המבורגר.png","name":"ארוחת-המבורגר"},{"url":"http://10.0.2.2:5000/upload/kids/ארוחת-שניצלונים.png","name":"ארוחת-שניצלונים"}]
                        ,'ביסים':
                        [{"url":"http://10.0.2.2:5000/upload/bisim/כנפיים.png","name":"כנפיים"},{"url":"http://10.0.2.2:5000/upload/bisim/שניצלונים.png","name":"שניצלונים"},{"url":"http://10.0.2.2:5000/upload/bisim/סיגר-הבית.png","name":"סיגר הבית"}]
                        ,'טבעוני':
                        [{"url":"http://10.0.2.2:5000/upload/tivoni/ביונד.png","name":"המבורגר ביונד"},{"url":"http://10.0.2.2:5000/upload/tivoni/פורטבלו.png","name":"המבורגר פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פור3.png","name":"בגט פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פורטובלו.png","name":"טורטיה פורטובלו"},{"url":"http://10.0.2.2:5000/upload/tivoni/פור.png","name":"פורטובלו"}]
                        ,'סלטים':
                        [{"url":"http://10.0.2.2:5000/upload/salade/שוק.png","name":"סלט שוק"},{"url":"http://10.0.2.2:5000/upload/salade/אסייתי.png","name":"סלט אסייתי"},{"url":"http://10.0.2.2:5000/upload/salade/קיסרעלים.png","name":"סלט קיסר עלים"}]

                }
        }

        ,'landwer':
        {
            'ירושלים':
            {
                        'סלטים':
                        [{"url":"http://10.0.2.2:5000/upload1/salade/סלטאיכריםאיטלקי.png","name":"סלט איכרים איטלקי"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטחלומי.png","name":"סלט חלומי"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטיםתיכוני.png","name":"סלט ים תיכוני"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטניסואזלימוני.png","name":"סלט ניסואז לימוני"}]
                        ,'עיקריות':
                        [{"url":"http://10.0.2.2:5000/upload1/maine/ביונדמיט.png","name":"ביונד מיט"},{"url":"http://10.0.2.2:5000/upload1/maine/סלמוןוסלטרענן.png","name":"סלמון וסלט רענן"},{"url":"http://10.0.2.2:5000/upload1/maine/סלמוןטריאקי.png","name":"סלמון טריאקי"},{"url":"http://10.0.2.2:5000/upload1/maine/פישאנדצ'יפס.png","name":"פיש & צ'יפס"},{"url":"http://10.0.2.2:5000/upload1/maine/תבשילכוסמת.png","name":"תבשיל כוסמת"}]
                        ,'פסטה ופיצה':
                        [{"url":"http://10.0.2.2:5000/upload1/pasta/פיצהעגבניותקלאסית.png","name":"פיצה עגבניות קלאסית"},{"url":"http://10.0.2.2:5000/upload1/pasta/פיצהפסטוגבינות.png","name":"פיצה פסטו גבינות"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהבטטהשמנתערמונים.png","name":"פסטה בטטה שמנת ערמונים"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותבזיליקום.png","name":"פסטה עגבניו תבזיליקום"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותורודות.png","name":"פסטה עגבניות ורודות"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהפטריותצלויות.png","name":"פסטה פטריות צלויות"},{"url":"http://10.0.2.2:5000/upload1/pasta/רביוליגבינות.png","name":"רביולי גבינות"}]
                        ,'כריכים וטסטים':
                        [{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטבולגרית.png","name":"בייגל טוסט בולגרית"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטירושלמי.png","name":"בייגל טוסט ירושלמי"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטצהובה.png","name":"בייגל טוסט צהובה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךחביתה.png","name":"כריך חביתה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךטונה.png","name":"כריך טונה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךסלמוןמעושן.png","name":"כריך סלמון מעושן"}]
                        ,'ארוחות בוקר':
                        [{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרגלילי.png","name":"בוקר גלילי"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרטבעוני.png","name":"בוקר טבעוני"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרכלהיום.png","name":"בוקר כל היום"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרלנדוור.png","name":"בוקר לנדוור"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בנדיקטסלמון.png","name":"בנדיקט סלמון"},{"url":"http://10.0.2.2:5000/upload1/breakfast/חציכריך+שתייה.png","name":"חצי כריך + שתייה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/מוזלי.png","name":"מוזלי"},{"url":"http://10.0.2.2:5000/upload1/breakfast/קפהומאפה.png","name":"קפה ומאפה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/רביוליבטטה.png","name":"רביולי בטטה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/שקשוקהקלאסית.png","name":"שקשוקה קלאסית"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload1/kids/בוקרקטנטנים.png","name":"בוקר קטנטנים"},{"url":"http://10.0.2.2:5000/upload1/kids/טוסטילדים.png","name":"טוסט ילדים"},{"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדיםללאגלוטן.png","name":"פיצה ילדים ללא גלוטן"},{"url":"http://10.0.2.2:5000/upload1/kids/פסטהילדים.png","name":"פסטה ילדים"},{"url":"http://10.0.2.2:5000/upload1/kids/שניצלונידגילדים.png","name":"שניצלוני דג ילדים"}]
                }
            ,'אשדוד':
            {
                         'סלטים':
                        [{"url":"http://10.0.2.2:5000/upload1/salade/סלטאיכריםאיטלקי.png","name":"סלט איכרים איטלקי"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטחלומי.png","name":"סלט חלומי"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטיםתיכוני.png","name":"סלט ים תיכוני"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטניסואזלימוני.png","name":"סלט ניסואז לימוני"}]
                        ,'עיקריות':
                        [{"url":"http://10.0.2.2:5000/upload1/maine/ביונדמיט.png","name":"ביונד מיט"},{"url":"http://10.0.2.2:5000/upload1/maine/סלמוןוסלטרענן.png","name":"סלמון וסלט רענן"},{"url":"http://10.0.2.2:5000/upload1/maine/סלמוןטריאקי.png","name":"סלמון טריאקי"},{"url":"http://10.0.2.2:5000/upload1/maine/פישאנדצ'יפס.png","name":"פיש & צ'יפס"},{"url":"http://10.0.2.2:5000/upload1/maine/תבשילכוסמת.png","name":"תבשיל כוסמת"}]
                        ,'פסטה ופיצה':
                        [{"url":"http://10.0.2.2:5000/upload1/pasta/פיצהעגבניותקלאסית.png","name":"פיצה עגבניות קלאסית"},{"url":"http://10.0.2.2:5000/upload1/pasta/פיצהפסטוגבינות.png","name":"פיצה פסטו גבינות"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהבטטהשמנתערמונים.png","name":"פסטה בטטה שמנת ערמונים"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותבזיליקום.png","name":"פסטה עגבניו תבזיליקום"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותורודות.png","name":"פסטה עגבניות ורודות"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהפטריותצלויות.png","name":"פסטה פטריות צלויות"},{"url":"http://10.0.2.2:5000/upload1/pasta/רביוליגבינות.png","name":"רביולי גבינות"}]
                        ,'כריכים וטסטים':
                        [{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטבולגרית.png","name":"בייגל טוסט בולגרית"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטירושלמי.png","name":"בייגל טוסט ירושלמי"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטצהובה.png","name":"בייגל טוסט צהובה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךחביתה.png","name":"כריך חביתה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךטונה.png","name":"כריך טונה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךסלמוןמעושן.png","name":"כריך סלמון מעושן"}]
                        ,'ארוחות בוקר':
                        [{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרגלילי.png","name":"בוקר גלילי"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרטבעוני.png","name":"בוקר טבעוני"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרכלהיום.png","name":"בוקר כל היום"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרלנדוור.png","name":"בוקר לנדוור"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בנדיקטסלמון.png","name":"בנדיקט סלמון"},{"url":"http://10.0.2.2:5000/upload1/breakfast/חציכריך+שתייה.png","name":"חצי כריך + שתייה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/מוזלי.png","name":"מוזלי"},{"url":"http://10.0.2.2:5000/upload1/breakfast/קפהומאפה.png","name":"קפה ומאפה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/רביוליבטטה.png","name":"רביולי בטטה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/שקשוקהקלאסית.png","name":"שקשוקה קלאסית"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload1/kids/בוקרקטנטנים.png","name":"בוקר קטנטנים"},{"url":"http://10.0.2.2:5000/upload1/kids/טוסטילדים.png","name":"טוסט ילדים"},{"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדיםללאגלוטן.png","name":"פיצה ילדים ללא גלוטן"},{"url":"http://10.0.2.2:5000/upload1/kids/פסטהילדים.png","name":"פסטה ילדים"},{"url":"http://10.0.2.2:5000/upload1/kids/שניצלונידגילדים.png","name":"שניצלוני דג ילדים"}]
                   }
            ,'נתניה':
            {
                       'סלטים':
                        [{"url":"http://10.0.2.2:5000/upload1/salade/סלטאיכריםאיטלקי.png","name":"סלט איכרים איטלקי"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטחלומי.png","name":"סלט חלומי"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטיםתיכוני.png","name":"סלט ים תיכוני"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטניסואזלימוני.png","name":"סלט ניסואז לימוני"}]
                        ,'עיקריות':
                        [{"url":"http://10.0.2.2:5000/upload1/maine/ביונדמיט.png","name":"ביונד מיט"},{"url":"http://10.0.2.2:5000/upload1/maine/סלמוןוסלטרענן.png","name":"סלמון וסלט רענן"},{"url":"http://10.0.2.2:5000/upload1/maine/סלמוןטריאקי.png","name":"סלמון טריאקי"},{"url":"http://10.0.2.2:5000/upload1/maine/פישאנדצ'יפס.png","name":"פיש & צ'יפס"},{"url":"http://10.0.2.2:5000/upload1/maine/תבשילכוסמת.png","name":"תבשיל כוסמת"}]
                        ,'פסטה ופיצה':
                        [{"url":"http://10.0.2.2:5000/upload1/pasta/פיצהעגבניותקלאסית.png","name":"פיצה עגבניות קלאסית"},{"url":"http://10.0.2.2:5000/upload1/pasta/פיצהפסטוגבינות.png","name":"פיצה פסטו גבינות"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהבטטהשמנתערמונים.png","name":"פסטה בטטה שמנת ערמונים"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותבזיליקום.png","name":"פסטה עגבניו תבזיליקום"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותורודות.png","name":"פסטה עגבניות ורודות"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהפטריותצלויות.png","name":"פסטה פטריות צלויות"},{"url":"http://10.0.2.2:5000/upload1/pasta/רביוליגבינות.png","name":"רביולי גבינות"}]
                        ,'כריכים וטסטים':
                        [{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטבולגרית.png","name":"בייגל טוסט בולגרית"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטירושלמי.png","name":"בייגל טוסט ירושלמי"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטצהובה.png","name":"בייגל טוסט צהובה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךחביתה.png","name":"כריך חביתה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךטונה.png","name":"כריך טונה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךסלמוןמעושן.png","name":"כריך סלמון מעושן"}]
                        ,'ארוחות בוקר':
                        [{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרגלילי.png","name":"בוקר גלילי"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרטבעוני.png","name":"בוקר טבעוני"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרכלהיום.png","name":"בוקר כל היום"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרלנדוור.png","name":"בוקר לנדוור"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בנדיקטסלמון.png","name":"בנדיקט סלמון"},{"url":"http://10.0.2.2:5000/upload1/breakfast/חציכריך+שתייה.png","name":"חצי כריך + שתייה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/מוזלי.png","name":"מוזלי"},{"url":"http://10.0.2.2:5000/upload1/breakfast/קפהומאפה.png","name":"קפה ומאפה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/רביוליבטטה.png","name":"רביולי בטטה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/שקשוקהקלאסית.png","name":"שקשוקה קלאסית"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload1/kids/בוקרקטנטנים.png","name":"בוקר קטנטנים"},{"url":"http://10.0.2.2:5000/upload1/kids/טוסטילדים.png","name":"טוסט ילדים"},{"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדיםללאגלוטן.png","name":"פיצה ילדים ללא גלוטן"},{"url":"http://10.0.2.2:5000/upload1/kids/פסטהילדים.png","name":"פסטה ילדים"},{"url":"http://10.0.2.2:5000/upload1/kids/שניצלונידגילדים.png","name":"שניצלוני דג ילדים"}]
                  }
            ,'רעננה':
            {
                         'סלטים':
                        [{"url":"http://10.0.2.2:5000/upload1/salade/סלטאיכריםאיטלקי.png","name":"סלט איכרים איטלקי"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטחלומי.png","name":"סלט חלומי"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטיםתיכוני.png","name":"סלט ים תיכוני"},{"url":"http://10.0.2.2:5000/upload1/salade/סלטניסואזלימוני.png","name":"סלט ניסואז לימוני"}]
                        ,'עיקריות':
                        [{"url":"http://10.0.2.2:5000/upload1/maine/ביונדמיט.png","name":"ביונד מיט"},{"url":"http://10.0.2.2:5000/upload1/maine/סלמוןוסלטרענן.png","name":"סלמון וסלט רענן"},{"url":"http://10.0.2.2:5000/upload1/maine/סלמוןטריאקי.png","name":"סלמון טריאקי"},{"url":"http://10.0.2.2:5000/upload1/maine/פישאנדצ'יפס.png","name":"פיש & צ'יפס"},{"url":"http://10.0.2.2:5000/upload1/maine/תבשילכוסמת.png","name":"תבשיל כוסמת"}]
                        ,'פסטה ופיצה':
                        [{"url":"http://10.0.2.2:5000/upload1/pasta/פיצהעגבניותקלאסית.png","name":"פיצה עגבניות קלאסית"},{"url":"http://10.0.2.2:5000/upload1/pasta/פיצהפסטוגבינות.png","name":"פיצה פסטו גבינות"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהבטטהשמנתערמונים.png","name":"פסטה בטטה שמנת ערמונים"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותבזיליקום.png","name":"פסטה עגבניו תבזיליקום"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותורודות.png","name":"פסטה עגבניות ורודות"},{"url":"http://10.0.2.2:5000/upload1/pasta/פסטהפטריותצלויות.png","name":"פסטה פטריות צלויות"},{"url":"http://10.0.2.2:5000/upload1/pasta/רביוליגבינות.png","name":"רביולי גבינות"}]
                        ,'כריכים וטסטים':
                        [{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטבולגרית.png","name":"בייגל טוסט בולגרית"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטירושלמי.png","name":"בייגל טוסט ירושלמי"},{"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטצהובה.png","name":"בייגל טוסט צהובה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךחביתה.png","name":"כריך חביתה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךטונה.png","name":"כריך טונה"},{"url":"http://10.0.2.2:5000/upload1/toast/כריךסלמוןמעושן.png","name":"כריך סלמון מעושן"}]
                        ,'ארוחות בוקר':
                        [{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרגלילי.png","name":"בוקר גלילי"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרטבעוני.png","name":"בוקר טבעוני"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרכלהיום.png","name":"בוקר כל היום"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרלנדוור.png","name":"בוקר לנדוור"},{"url":"http://10.0.2.2:5000/upload1/breakfast/בנדיקטסלמון.png","name":"בנדיקט סלמון"},{"url":"http://10.0.2.2:5000/upload1/breakfast/חציכריך+שתייה.png","name":"חצי כריך + שתייה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/מוזלי.png","name":"מוזלי"},{"url":"http://10.0.2.2:5000/upload1/breakfast/קפהומאפה.png","name":"קפה ומאפה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/רביוליבטטה.png","name":"רביולי בטטה"},{"url":"http://10.0.2.2:5000/upload1/breakfast/שקשוקהקלאסית.png","name":"שקשוקה קלאסית"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload1/kids/בוקרקטנטנים.png","name":"בוקר קטנטנים"},{"url":"http://10.0.2.2:5000/upload1/kids/טוסטילדים.png","name":"טוסט ילדים"},{"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדיםללאגלוטן.png","name":"פיצה ילדים ללא גלוטן"},{"url":"http://10.0.2.2:5000/upload1/kids/פסטהילדים.png","name":"פסטה ילדים"},{"url":"http://10.0.2.2:5000/upload1/kids/שניצלונידגילדים.png","name":"שניצלוני דג ילדים"}]
                }
        }
        
         ,'Japanika':
        {
            'ירושלים':
            {
                        'אורז וגריל':
                        [{"url":"http://10.0.2.2:5000/upload2/rice/3פאד-קפאו-בקר.jpg","name":"פאד קפאו בקר"},{"url":"http://10.0.2.2:5000/upload2/rice/דג-בקשיו.jpg","name":"דג בקשיו"},{"url":"http://10.0.2.2:5000/upload2/rice/חמוץ-מתוק.png","name":"חמוץ מתוק"}]
                        ,'מנות ווק':
                        [{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-בקר.png","name":"צאנג מאי בקר"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-טופו.png","name":"צאנג מאי טופו"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-ירקות.png","name":"צאנג מאי ירקות"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-עוף.png","name":"צאנג מאי עוף"}]
                        ,'ספיישל סושי':
                        [{"url":"http://10.0.2.2:5000/upload2/special/גפנקו.png","name":"גפנקו"},{"url":"http://10.0.2.2:5000/upload2/special/מנטה-רול.png","name":"מנטה רול"},{"url":"http://10.0.2.2:5000/upload2/special/סלמון-ליים-רול.png","name":"סלמון ליים רול"},{"url":"http://10.0.2.2:5000/upload2/special/סנסט.png","name":"סנסט"},{"url":"http://10.0.2.2:5000/upload2/special/קריספי-רול.png","name":"קריספי רול"}]
                        ,'מרקים':
                        [{"url":"http://10.0.2.2:5000/upload2/soup/אדום.png","name":"מרק מיסו"},{"url":"http://10.0.2.2:5000/upload2/soup/ירוק.png","name":"טום יאם ירקות"},{"url":"http://10.0.2.2:5000/upload2/soup/צהוב.png","name":"מרק תירס תאילנדי"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload2/kids/אצבעות-עוף.png","name":"אצבעות עוף"},{"url":"http://10.0.2.2:5000/upload2/kids/פרש-קידס-נודלס-עוף.png","name":"פרש נודלס"},{"url":"http://10.0.2.2:5000/upload2/kids/קריספי-ציקן-קידס.png","name":"קריספי ציקן"}]
                        ,'מנות פתיחה':
                        [{"url":"http://10.0.2.2:5000/upload2/appetizier/אדממה.png","name":"אדממה"},{"url":"http://10.0.2.2:5000/upload2/appetizier/חמוצים-יפניים.png","name":"חמוצים יפניים"},{"url":"http://10.0.2.2:5000/upload2/appetizier/קריספי-בטטה.png","name":"קריספי בטטה"}]
            }
            ,'אשדוד':
            {
                 'אורז וגריל':
                        [{"url":"http://10.0.2.2:5000/upload2/rice/3פאד-קפאו-בקר.jpg","name":"פאד קפאו בקר"},{"url":"http://10.0.2.2:5000/upload2/rice/דג-בקשיו.jpg","name":"דג בקשיו"},{"url":"http://10.0.2.2:5000/upload2/rice/חמוץ-מתוק.png","name":"חמוץ מתוק"}]
                        ,'מנות ווק':
                        [{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-בקר.png","name":"צאנג מאי בקר"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-טופו.png","name":"צאנג מאי טופו"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-ירקות.png","name":"צאנג מאי ירקות"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-עוף.png","name":"צאנג מאי עוף"}]
                        ,'ספיישל סושי':
                        [{"url":"http://10.0.2.2:5000/upload2/special/גפנקו.png","name":"גפנקו"},{"url":"http://10.0.2.2:5000/upload2/special/מנטה-רול.png","name":"מנטה רול"},{"url":"http://10.0.2.2:5000/upload2/special/סלמון-ליים-רול.png","name":"סלמון ליים רול"},{"url":"http://10.0.2.2:5000/upload2/special/סנסט.png","name":"סנסט"},{"url":"http://10.0.2.2:5000/upload2/special/קריספי-רול.png","name":"קריספי רול"}]
                        ,'מרקים':
                        [{"url":"http://10.0.2.2:5000/upload2/soup/אדום.png","name":"מרק מיסו"},{"url":"http://10.0.2.2:5000/upload2/soup/ירוק.png","name":"טום יאם ירקות"},{"url":"http://10.0.2.2:5000/upload2/soup/צהוב.png","name":"מרק תירס תאילנדי"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload2/kids/אצבעות-עוף.png","name":"אצבעות עוף"},{"url":"http://10.0.2.2:5000/upload2/kids/פרש-קידס-נודלס-עוף.png","name":"פרש נודלס"},{"url":"http://10.0.2.2:5000/upload2/kids/קריספי-ציקן-קידס.png","name":"קריספי ציקן"}]
                        ,'מנות פתיחה':
                        [{"url":"http://10.0.2.2:5000/upload2/appetizier/אדממה.png","name":"אדממה"},{"url":"http://10.0.2.2:5000/upload2/appetizier/חמוצים-יפניים.png","name":"חמוצים יפניים"},{"url":"http://10.0.2.2:5000/upload2/appetizier/קריספי-בטטה.png","name":"קריספי בטטה"}]
           
            }
            ,'רעננה':
            {
                 'אורז וגריל':
                        [{"url":"http://10.0.2.2:5000/upload2/rice/3פאד-קפאו-בקר.jpg","name":"פאד קפאו בקר"},{"url":"http://10.0.2.2:5000/upload2/rice/דג-בקשיו.jpg","name":"דג בקשיו"},{"url":"http://10.0.2.2:5000/upload2/rice/חמוץ-מתוק.png","name":"חמוץ מתוק"}]
                        ,'מנות ווק':
                        [{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-בקר.png","name":"צאנג מאי בקר"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-טופו.png","name":"צאנג מאי טופו"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-ירקות.png","name":"צאנג מאי ירקות"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-עוף.png","name":"צאנג מאי עוף"}]
                        ,'ספיישל סושי':
                        [{"url":"http://10.0.2.2:5000/upload2/special/גפנקו.png","name":"גפנקו"},{"url":"http://10.0.2.2:5000/upload2/special/מנטה-רול.png","name":"מנטה רול"},{"url":"http://10.0.2.2:5000/upload2/special/סלמון-ליים-רול.png","name":"סלמון ליים רול"},{"url":"http://10.0.2.2:5000/upload2/special/סנסט.png","name":"סנסט"},{"url":"http://10.0.2.2:5000/upload2/special/קריספי-רול.png","name":"קריספי רול"}]
                        ,'מרקים':
                        [{"url":"http://10.0.2.2:5000/upload2/soup/אדום.png","name":"מרק מיסו"},{"url":"http://10.0.2.2:5000/upload2/soup/ירוק.png","name":"טום יאם ירקות"},{"url":"http://10.0.2.2:5000/upload2/soup/צהוב.png","name":"מרק תירס תאילנדי"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload2/kids/אצבעות-עוף.png","name":"אצבעות עוף"},{"url":"http://10.0.2.2:5000/upload2/kids/פרש-קידס-נודלס-עוף.png","name":"פרש נודלס"},{"url":"http://10.0.2.2:5000/upload2/kids/קריספי-ציקן-קידס.png","name":"קריספי ציקן"}]
                        ,'מנות פתיחה':
                        [{"url":"http://10.0.2.2:5000/upload2/appetizier/אדממה.png","name":"אדממה"},{"url":"http://10.0.2.2:5000/upload2/appetizier/חמוצים-יפניים.png","name":"חמוצים יפניים"},{"url":"http://10.0.2.2:5000/upload2/appetizier/קריספי-בטטה.png","name":"קריספי בטטה"}]
           
            }
            ,'נתניה':
            {
                 'אורז וגריל':
                        [{"url":"http://10.0.2.2:5000/upload2/rice/3פאד-קפאו-בקר.jpg","name":"פאד קפאו בקר"},{"url":"http://10.0.2.2:5000/upload2/rice/דג-בקשיו.jpg","name":"דג בקשיו"},{"url":"http://10.0.2.2:5000/upload2/rice/חמוץ-מתוק.png","name":"חמוץ מתוק"}]
                        ,'מנות ווק':
                        [{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-בקר.png","name":"צאנג מאי בקר"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-טופו.png","name":"צאנג מאי טופו"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-ירקות.png","name":"צאנג מאי ירקות"},{"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-עוף.png","name":"צאנג מאי עוף"}]
                        ,'ספיישל סושי':
                        [{"url":"http://10.0.2.2:5000/upload2/special/גפנקו.png","name":"גפנקו"},{"url":"http://10.0.2.2:5000/upload2/special/מנטה-רול.png","name":"מנטה רול"},{"url":"http://10.0.2.2:5000/upload2/special/סלמון-ליים-רול.png","name":"סלמון ליים רול"},{"url":"http://10.0.2.2:5000/upload2/special/סנסט.png","name":"סנסט"},{"url":"http://10.0.2.2:5000/upload2/special/קריספי-רול.png","name":"קריספי רול"}]
                        ,'מרקים':
                        [{"url":"http://10.0.2.2:5000/upload2/soup/אדום.png","name":"מרק מיסו"},{"url":"http://10.0.2.2:5000/upload2/soup/ירוק.png","name":"טום יאם ירקות"},{"url":"http://10.0.2.2:5000/upload2/soup/צהוב.png","name":"מרק תירס תאילנדי"}]
                        ,'ארוחות ילדים':
                        [{"url":"http://10.0.2.2:5000/upload2/kids/אצבעות-עוף.png","name":"אצבעות עוף"},{"url":"http://10.0.2.2:5000/upload2/kids/פרש-קידס-נודלס-עוף.png","name":"פרש נודלס"},{"url":"http://10.0.2.2:5000/upload2/kids/קריספי-ציקן-קידס.png","name":"קריספי ציקן"}]
                        ,'מנות פתיחה':
                        [{"url":"http://10.0.2.2:5000/upload2/appetizier/אדממה.png","name":"אדממה"},{"url":"http://10.0.2.2:5000/upload2/appetizier/חמוצים-יפניים.png","name":"חמוצים יפניים"},{"url":"http://10.0.2.2:5000/upload2/appetizier/קריספי-בטטה.png","name":"קריספי בטטה"}]
           
            }
        }
})

ref = db.reference('/detail')
ref.set( {
        'BurgersBar':
            {
                'ירושלים':
                    {
                        'המבורגרים':
                        {
                            'המבורגר חריף':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/harif.png","name":"המבורגר חריף","description":"100% בקר בתיבול פיקנטי 150G","price":"מחיר 39₪","time":"10 דק'"}
                            ,'המבורגר קלאסי':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/classi.png","name":"המבורגר קלאסי","description":"100% בקר בתיבול מלח ופלפל 150 G","price":"מחיר 39₪","time":"15 דק'"}
                            ,'המבורגר טלה':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/tale.png","name":"המבורגר טלה","description":"100% בקר בתוספת שומן כבש בתיבול מלח ופלפל, 220 גרם","price":"מחיר 49₪","time":"15 דק'"}
                            ,'המבורגר טלה הבית':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/talebait.png","name":"המבורגר טלה הבית","description":" 100% בקר בתוספת שומן כבש, שום ובצל בתיבול הבית220 G","price":"מחיר 49₪","time":"15 דק'"}
                            }
                        ,'מדיום בורגר':
                        {
                            'המבורגר M1':
                            {"url":"http://10.0.2.2:5000/upload/medium/M1.png","name":"המבורגר M1","description":"מדיום בורגר קלאסי 100 גרם בליווי מגוון רטבים לבחירה","price":"מחיר 32₪","time":"15 דק'"}
                            ,'המבורגר M4':
                            {"url":"http://10.0.2.2:5000/upload/medium/M4.png","name":"המבורגר M4","description":"רביעיית מדיום בורגר קלאסי 100 גרם בליווי מגוון רטבים לבחירה","price":"מחיר 119₪","time":"15 דק'"}
                        }
                        ,'טורטיות':
                        {
                            'טורטיה חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה חזה עוף","description":"100% חזה עוף מובחר בטורטייה","price":"מחיר 42₪","time":"15 דק'"}
                            ,'טורטיה סטייק':
                            {"url":"http://10.0.2.2:5000/upload/tortia/סטייק.png","name":"טורטיה סטייק","description":"סטייק פרוס דק דק בטורטייה","price":"מחיר 47₪","time":"15 דק'"}
                            ,'טורטיה פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tortia/פורטובלו.png","name":"טורטיה פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בטורטייה","price":"מחיר 37₪","time":"15 דק'"}
                            ,'טורטיה המבורגר':
                            {"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה המבורגר","description":"ההמבורגר העסיסי שאתם אוהבים בטורטייה.150G","price":"מחיר 39₪","time":"15 דק'"}
                            ,'טורטיה שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/tortia/שניצל-קריספי.png","name":"טורטיה שניצל קריספי","description":"100% חזה עוף מובחר בציפוי פריך בטורטייה","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'סנדוויצים':
                        {
                            'סנדוויץ חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/חזה-עוף.png","name":"סנדוויץ חזה עוף","description":"100% חזה עוף מוגש בלחמנית בורגר","price":"מחיר42₪","time":"15 דק'"}
                            ,'סנדוויץ סטייק':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/סטייק.png","name":"סנדוויץ סטייק","description":"סטייק פרוס דק דק מוגש בלחמנית בורגר","price":"מחיר 47₪","time":"15 דק'"}
                            ,'סנדוויץ פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/פורטובלו.png","name":"סנדוויץ פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית, מלח ופלפל מוגש בלחמנית בורגר","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סנדוויץ קורנביף':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/קורנביף.png","name":"סנדוויץ קורנביף ","description":"נתחי חזה בקר מעושן מוגש בלחמנית בורגר","price":"מחיר 47₪","time":"15 דק'"}
                            ,'סנדוויץ שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/שניצל-קריספי.png","name":"סנדוויץ שניצל קריספי","description":"100% חזה עוף מובחר בציפוי פריך מוגש בלחמנית בורגר","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'ביסים':
                        {
                            'כנפיים':
                            {"url":"http://10.0.2.2:5000/upload/bisim/כנפיים.png","name":"כנפיים","description":"חצאי כנפיים מוקפצות ברוטב לבחירה10 חצאים","price":"מחיר 35₪","time":"15 דק'"}
                            ,'שניצלונים':
                            {"url":"http://10.0.2.2:5000/upload/bisim/שניצלונים.png","name":"שניצלונים","description":"רצועות של  100% חזה עוף מובחר בציפוי פריך","price":"מחיר 32₪","time":"15 דק'"}
                            ,'סיגר הבית':
                            {"url":"http://10.0.2.2:5000/upload/bisim/סיגר-הבית.png","name":"סיגר הבית","description":"סיגר מגולגל בעבודת יד, במילוי אסאדו מפורק","price":"מחיר 10₪","time":"15 דק'"}
                        }
                        ,'ארוחות ילדים':
                        {
                            'ארוחת-המבורגר':
                            {"url":"http://10.0.2.2:5000/upload/kids/ארוחת-המבורגר.png","name":"ארוחת-המבורגר","description":"המבורגר קלאסי + צ'יפס/ כדורי פירה / טבעות בצל","price":"מחיר 42₪","time":"15 דק'"}
                            ,'ארוחת-שניצלונים':
                            {"url":"http://10.0.2.2:5000/upload/kids/ארוחת-שניצלונים.png","name":"ארוחת-שניצלונים","description":"שניצלונים + צ'יפס / כדורי פירה / טבעות בצל","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'טבעוני':
                        {
                            'המבורגר ביונד':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/ביונד.png","name":"המבורגר ביונד","description":"ההמבורגר הטבעוני המושלם.100% בשר מהצומח בחווית טעם של הדבר האמיתי","price":"מחיר 49₪","time":"15 דק'"}
                            ,'המבורגר פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פורטבלו.png","name":"המבורגר פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית, מלח ופלפל מוגש בלחמנית בורגר","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פור3.png","name":"בגט פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בבאגט","price":"מחיר 37₪","time":"15 דק'"}
                            ,'טורטיה פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פורטובלו.png","name":"טורטיה פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בטורטייה","price":"מחיר 37₪","time":"15 דק'"}
                        }
                        ,'סלטים':
                        {
                            'סלט שוק':
                            {"url":"http://10.0.2.2:5000/upload/salade/שוק.png","name":"סלט שוק","description":"לבבות חסה, עגבניות שרי תמר, מלפפון, כרוב לבן וגזר בתיבול שמן זית ולימון","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סלט אסייתי':
                            {"url":"http://10.0.2.2:5000/upload/salade/אסייתי.png","name":"סלט אסייתי","description":"כרוב לבן וגזר בתיבול שמן זית ולימון","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סלט קיסר עלים':
                            {"url":"http://10.0.2.2:5000/upload/salade/קיסרעלים.png","name":"סלט קיסר עלים","description":"לבבות חסה, בצל סגול, לבבות דקל, זיתי קלמטה, ביצה קשה מגורדת ושקדים קלויים בתיבול רוטב קיסר.","price":"מחיר 40₪","time":"15 דק'"}
                        }
                        ,'בגטים':
                        {
                            'בגט סטייק':
                            {"url":"http://10.0.2.2:5000/upload/baguet/סטייק.png","name":"בגט סטייק","description":"","price":"מחיר 47₪","time":"15 דק'"}
                             ,'בגט חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/baguet/haze.png","name":"בגט חזה עוף","description":"100% חזה עוף מובחר ","price":"מחיר 42₪","time":"15 דק'"}
                            ,'בגט פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/baguet/פורטובלו.png","name":"בגט פורטובלו","description":"","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט קורנביף':
                            {"url":"http://10.0.2.2:5000/upload/baguet/קורנביף.png","name":"בגט קורנביף","description":"נתחי חזה בקר מעושן","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/baguet/שניצל-קריספי.png","name":"בגט שניצל קריספי","description":"","price":"מחיר 37₪","time":"15 דק'"}
                        }
                    }
                ,'רעננה':
                    {
                        'המבורגרים':
                        {
                            'המבורגר חריף':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/harif.png","name":"המבורגר חריף","description":"100% בקר בתיבול פיקנטי 150G","price":"מחיר 39₪","time":"10 דק'"}
                            ,'המבורגר קלאסי':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/classi.png","name":"המבורגר קלאסי","description":"100% בקר בתיבול מלח ופלפל 150 G","price":"מחיר 39₪","time":"15 דק'"}
                            ,'המבורגר טלה':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/tale.png","name":"המבורגר טלה","description":"100% בקר בתוספת שומן כבש בתיבול מלח ופלפל, 220 גרם","price":"מחיר 49₪","time":"15 דק'"}
                            ,'המבורגר טלה הבית':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/talebait.png","name":"המבורגר טלה הבית","description":" 100% בקר בתוספת שומן כבש, שום ובצל בתיבול הבית220 G","price":"מחיר 49₪","time":"15 דק'"}
                            }
                        ,'מדיום בורגר':
                        {
                            'המבורגר M1':
                            {"url":"http://10.0.2.2:5000/upload/medium/M1.png","name":"המבורגר M1","description":"מדיום בורגר קלאסי 100 גרם בליווי מגוון רטבים לבחירה","price":"מחיר 32₪","time":"15 דק'"}
                            ,'המבורגר M4':
                            {"url":"http://10.0.2.2:5000/upload/medium/M4.png","name":"המבורגר M4","description":"רביעיית מדיום בורגר קלאסי 100 גרם בליווי מגוון רטבים לבחירה","price":"מחיר 119₪","time":"15 דק'"}
                        }
                        ,'טורטיות':
                        {
                            'טורטיה חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה חזה עוף","description":"100% חזה עוף מובחר בטורטייה","price":"מחיר 42₪","time":"15 דק'"}
                            ,'טורטיה סטייק':
                            {"url":"http://10.0.2.2:5000/upload/tortia/סטייק.png","name":"טורטיה סטייק","description":"סטייק פרוס דק דק בטורטייה","price":"מחיר 47₪","time":"15 דק'"}
                            ,'טורטיה פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tortia/פורטובלו.png","name":"טורטיה פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בטורטייה","price":"מחיר 37₪","time":"15 דק'"}
                            ,'טורטיה המבורגר':
                            {"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה המבורגר","description":"ההמבורגר העסיסי שאתם אוהבים בטורטייה.150G","price":"מחיר 39₪","time":"15 דק'"}
                            ,'טורטיה שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/tortia/שניצל-קריספי.png","name":"טורטיה שניצל קריספי","description":"100% חזה עוף מובחר בציפוי פריך בטורטייה","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'סנדוויצים':
                        {
                            'סנדוויץ חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/חזה-עוף.png","name":"סנדוויץ חזה עוף","description":"100% חזה עוף מוגש בלחמנית בורגר","price":"מחיר42₪","time":"15 דק'"}
                            ,'סנדוויץ סטייק':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/סטייק.png","name":"סנדוויץ סטייק","description":"סטייק פרוס דק דק מוגש בלחמנית בורגר","price":"מחיר 47₪","time":"15 דק'"}
                            ,'סנדוויץ פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/פורטובלו.png","name":"סנדוויץ פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית, מלח ופלפל מוגש בלחמנית בורגר","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סנדוויץ קורנביף':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/קורנביף.png","name":"סנדוויץ קורנביף ","description":"נתחי חזה בקר מעושן מוגש בלחמנית בורגר","price":"מחיר 47₪","time":"15 דק'"}
                            ,'סנדוויץ שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/שניצל-קריספי.png","name":"סנדוויץ שניצל קריספי","description":"100% חזה עוף מובחר בציפוי פריך מוגש בלחמנית בורגר","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'ביסים':
                        {
                            'כנפיים':
                            {"url":"http://10.0.2.2:5000/upload/bisim/כנפיים.png","name":"כנפיים","description":"חצאי כנפיים מוקפצות ברוטב לבחירה10 חצאים","price":"מחיר 35₪","time":"15 דק'"}
                            ,'שניצלונים':
                            {"url":"http://10.0.2.2:5000/upload/bisim/שניצלונים.png","name":"שניצלונים","description":"רצועות של  100% חזה עוף מובחר בציפוי פריך","price":"מחיר 32₪","time":"15 דק'"}
                            ,'סיגר הבית':
                            {"url":"http://10.0.2.2:5000/upload/bisim/סיגר-הבית.png","name":"סיגר הבית","description":"סיגר מגולגל בעבודת יד, במילוי אסאדו מפורק","price":"מחיר 10₪","time":"15 דק'"}
                        }
                        ,'ארוחות ילדים':
                        {
                            'ארוחת-המבורגר':
                            {"url":"http://10.0.2.2:5000/upload/kids/ארוחת-המבורגר.png","name":"ארוחת-המבורגר","description":"המבורגר קלאסי + צ'יפס/ כדורי פירה / טבעות בצל","price":"מחיר 42₪","time":"15 דק'"}
                            ,'ארוחת-שניצלונים':
                            {"url":"http://10.0.2.2:5000/upload/kids/ארוחת-שניצלונים.png","name":"ארוחת-שניצלונים","description":"שניצלונים + צ'יפס / כדורי פירה / טבעות בצל","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'טבעוני':
                        {
                            'המבורגר ביונד':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/ביונד.png","name":"המבורגר ביונד","description":"ההמבורגר הטבעוני המושלם.100% בשר מהצומח בחווית טעם של הדבר האמיתי","price":"מחיר 49₪","time":"15 דק'"}
                            ,'המבורגר פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פורטבלו.png","name":"המבורגר פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית, מלח ופלפל מוגש בלחמנית בורגר","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פור3.png","name":"בגט פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בבאגט","price":"מחיר 37₪","time":"15 דק'"}
                            ,'טורטיה פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פורטובלו.png","name":"טורטיה פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בטורטייה","price":"מחיר 37₪","time":"15 דק'"}
                        }
                        ,'סלטים':
                        {
                            'סלט שוק':
                            {"url":"http://10.0.2.2:5000/upload/salade/שוק.png","name":"סלט שוק","description":"לבבות חסה, עגבניות שרי תמר, מלפפון, כרוב לבן וגזר בתיבול שמן זית ולימון","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סלט אסייתי':
                            {"url":"http://10.0.2.2:5000/upload/salade/אסייתי.png","name":"סלט אסייתי","description":"כרוב לבן וגזר בתיבול שמן זית ולימו","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סלט קיסר עלים':
                            {"url":"http://10.0.2.2:5000/upload/salade/קיסרעלים.png","name":"סלט קיסר עלים","description":"לבבות חסה, בצל סגול, לבבות דקל, זיתי קלמטה, ביצה קשה מגורדת ושקדים קלויים בתיבול רוטב קיסר.","price":"מחיר 40₪","time":"15 דק'"}
                        }
                        ,'בגטים':
                        {
                            'בגט סטייק':
                            {"url":"http://10.0.2.2:5000/upload/baguet/סטייק.png","name":"בגט סטייק","description":"","price":"מחיר 47₪","time":"15 דק'"}
                             ,'בגט חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/baguet/haze.png","name":"בגט חזה עוף","description":"100% חזה עוף מובחר ","price":"מחיר 42₪","time":"15 דק'"}
                            ,'בגט פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/baguet/פורטובלו.png","name":"בגט פורטובלו","description":"","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט קורנביף':
                            {"url":"http://10.0.2.2:5000/upload/baguet/קורנביף.png","name":"בגט קורנביף","description":"נתחי חזה בקר מעושן","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/baguet/שניצל-קריספי.png","name":"בגט שניצל קריספי","description":"","price":"מחיר 37₪","time":"15 דק'"}
                        }
                    }
                ,'אשדוד':
                     {
                        'המבורגרים':
                        {
                            'המבורגר חריף':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/harif.png","name":"המבורגר חריף","description":"100% בקר בתיבול פיקנטי 150G","price":"מחיר 39₪","time":"10 דק'"}
                            ,'המבורגר קלאסי':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/classi.png","name":"המבורגר קלאסי","description":"100% בקר בתיבול מלח ופלפל 150 G","price":"מחיר 39₪","time":"15 דק'"}
                            ,'המבורגר טלה':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/tale.png","name":"המבורגר טלה","description":"100% בקר בתוספת שומן כבש בתיבול מלח ופלפל, 220 גרם","price":"מחיר 49₪","time":"15 דק'"}
                            ,'המבורגר טלה הבית':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/talebait.png","name":"המבורגר טלה הבית","description":" 100% בקר בתוספת שומן כבש, שום ובצל בתיבול הבית220 G","price":"מחיר 49₪","time":"15 דק'"}
                            }
                        ,'מדיום בורגר':
                        {
                            'המבורגר M1':
                            {"url":"http://10.0.2.2:5000/upload/medium/M1.png","name":"המבורגר M1","description":"מדיום בורגר קלאסי 100 גרם בליווי מגוון רטבים לבחירה","price":"מחיר 32₪","time":"15 דק'"}
                            ,'המבורגר M4':
                            {"url":"http://10.0.2.2:5000/upload/medium/M4.png","name":"המבורגר M4","description":"רביעיית מדיום בורגר קלאסי 100 גרם בליווי מגוון רטבים לבחירה","price":"מחיר 119₪","time":"15 דק'"}
                        }
                        ,'טורטיות':
                        {
                            'טורטיה חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה חזה עוף","description":"100% חזה עוף מובחר בטורטייה","price":"מחיר 42₪","time":"15 דק'"}
                            ,'טורטיה סטייק':
                            {"url":"http://10.0.2.2:5000/upload/tortia/סטייק.png","name":"טורטיה סטייק","description":"סטייק פרוס דק דק בטורטייה","price":"מחיר 47₪","time":"15 דק'"}
                            ,'טורטיה פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tortia/פורטובלו.png","name":"טורטיה פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בטורטייה","price":"מחיר 37₪","time":"15 דק'"}
                            ,'טורטיה המבורגר':
                            {"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה המבורגר","description":"ההמבורגר העסיסי שאתם אוהבים בטורטייה.150G","price":"מחיר 39₪","time":"15 דק'"}
                            ,'טורטיה שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/tortia/שניצל-קריספי.png","name":"טורטיה שניצל קריספי","description":"100% חזה עוף מובחר בציפוי פריך בטורטייה","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'סנדוויצים':
                        {
                            'סנדוויץ חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/חזה-עוף.png","name":"סנדוויץ חזה עוף","description":"100% חזה עוף מוגש בלחמנית בורגר","price":"מחיר42₪","time":"15 דק'"}
                            ,'סנדוויץ סטייק':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/סטייק.png","name":"סנדוויץ סטייק","description":"סטייק פרוס דק דק מוגש בלחמנית בורגר","price":"מחיר 47₪","time":"15 דק'"}
                            ,'סנדוויץ פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/פורטובלו.png","name":"סנדוויץ פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית, מלח ופלפל מוגש בלחמנית בורגר","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סנדוויץ קורנביף':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/קורנביף.png","name":"סנדוויץ קורנביף ","description":"נתחי חזה בקר מעושן מוגש בלחמנית בורגר","price":"מחיר 47₪","time":"15 דק'"}
                            ,'סנדוויץ שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/שניצל-קריספי.png","name":"סנדוויץ שניצל קריספי","description":"100% חזה עוף מובחר בציפוי פריך מוגש בלחמנית בורגר","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'ביסים':
                        {
                            'כנפיים':
                            {"url":"http://10.0.2.2:5000/upload/bisim/כנפיים.png","name":"כנפיים","description":"חצאי כנפיים מוקפצות ברוטב לבחירה10 חצאים","price":"מחיר 35₪","time":"15 דק'"}
                            ,'שניצלונים':
                            {"url":"http://10.0.2.2:5000/upload/bisim/שניצלונים.png","name":"שניצלונים","description":"רצועות של  100% חזה עוף מובחר בציפוי פריך","price":"מחיר 32₪","time":"15 דק'"}
                            ,'סיגר הבית':
                            {"url":"http://10.0.2.2:5000/upload/bisim/סיגר-הבית.png","name":"סיגר הבית","description":"סיגר מגולגל בעבודת יד, במילוי אסאדו מפורק","price":"מחיר 10₪","time":"15 דק'"}
                        }
                        ,'ארוחות ילדים':
                        {
                            'ארוחת-המבורגר':
                            {"url":"http://10.0.2.2:5000/upload/kids/ארוחת-המבורגר.png","name":"ארוחת-המבורגר","description":"המבורגר קלאסי + צ'יפס/ כדורי פירה / טבעות בצל","price":"מחיר 42₪","time":"15 דק'"}
                            ,'ארוחת-שניצלונים':
                            {"url":"http://10.0.2.2:5000/upload/kids/ארוחת-שניצלונים.png","name":"ארוחת-שניצלונים","description":"שניצלונים + צ'יפס / כדורי פירה / טבעות בצל","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'טבעוני':
                        {
                            'המבורגר ביונד':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/ביונד.png","name":"המבורגר ביונד","description":"ההמבורגר הטבעוני המושלם.100% בשר מהצומח בחווית טעם של הדבר האמיתי","price":"מחיר 49₪","time":"15 דק'"}
                            ,'המבורגר פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פורטבלו.png","name":"המבורגר פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית, מלח ופלפל מוגש בלחמנית בורגר","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פור3.png","name":"בגט פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בבאגט","price":"מחיר 37₪","time":"15 דק'"}
                            ,'טורטיה פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פורטובלו.png","name":"טורטיה פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בטורטייה","price":"מחיר 37₪","time":"15 דק'"}
                        }
                        ,'סלטים':
                        {
                            'סלט שוק':
                            {"url":"http://10.0.2.2:5000/upload/salade/שוק.png","name":"סלט שוק","description":"לבבות חסה, עגבניות שרי תמר, מלפפון, כרוב לבן וגזר בתיבול שמן זית ולימון","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סלט אסייתי':
                            {"url":"http://10.0.2.2:5000/upload/salade/אסייתי.png","name":"סלט אסייתי","description":"כרוב לבן וגזר בתיבול שמן זית ולימו","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סלט קיסר עלים':
                            {"url":"http://10.0.2.2:5000/upload/salade/קיסרעלים.png","name":"סלט קיסר עלים","description":"לבבות חסה, בצל סגול, לבבות דקל, זיתי קלמטה, ביצה קשה מגורדת ושקדים קלויים בתיבול רוטב קיסר.","price":"מחיר 40₪","time":"15 דק'"}
                        }
                        ,'בגטים':
                        {
                            'בגט סטייק':
                            {"url":"http://10.0.2.2:5000/upload/baguet/סטייק.png","name":"בגט סטייק","description":"","price":"מחיר 47₪","time":"15 דק'"}
                             ,'בגט חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/baguet/haze.png","name":"בגט חזה עוף","description":"100% חזה עוף מובחר ","price":"מחיר 42₪","time":"15 דק'"}
                            ,'בגט פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/baguet/פורטובלו.png","name":"בגט פורטובלו","description":"","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט קורנביף':
                            {"url":"http://10.0.2.2:5000/upload/baguet/קורנביף.png","name":"בגט קורנביף","description":"נתחי חזה בקר מעושן","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/baguet/שניצל-קריספי.png","name":"בגט שניצל קריספי","description":"","price":"מחיר 37₪","time":"15 דק'"}
                        }
                    }
                ,'נתניה':
                    {
                        'המבורגרים':
                        {
                            'המבורגר חריף':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/harif.png","name":"המבורגר חריף","description":"100% בקר בתיבול פיקנטי 150G","price":"מחיר 39₪","time":"10 דק'"}
                            ,'המבורגר קלאסי':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/classi.png","name":"המבורגר קלאסי","description":"100% בקר בתיבול מלח ופלפל 150 G","price":"מחיר 39₪","time":"15 דק'"}
                            ,'המבורגר טלה':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/tale.png","name":"המבורגר טלה","description":"100% בקר בתוספת שומן כבש בתיבול מלח ופלפל, 220 גרם","price":"מחיר 49₪","time":"15 דק'"}
                            ,'המבורגר טלה הבית':
                            {"url":"http://10.0.2.2:5000/upload/המבורגרים/talebait.png","name":"המבורגר טלה הבית","description":" 100% בקר בתוספת שומן כבש, שום ובצל בתיבול הבית220 G","price":"מחיר 49₪","time":"15 דק'"}
                            }
                        ,'מדיום בורגר':
                        {
                            'המבורגר M1':
                            {"url":"http://10.0.2.2:5000/upload/medium/M1.png","name":"המבורגר M1","description":"מדיום בורגר קלאסי 100 גרם בליווי מגוון רטבים לבחירה","price":"מחיר 32₪","time":"15 דק'"}
                            ,'המבורגר M4':
                            {"url":"http://10.0.2.2:5000/upload/medium/M4.png","name":"המבורגר M4","description":"רביעיית מדיום בורגר קלאסי 100 גרם בליווי מגוון רטבים לבחירה","price":"מחיר 119₪","time":"15 דק'"}
                        }
                        ,'טורטיות':
                        {
                            'טורטיה חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה חזה עוף","description":"100% חזה עוף מובחר בטורטייה","price":"מחיר 42₪","time":"15 דק'"}
                            ,'טורטיה סטייק':
                            {"url":"http://10.0.2.2:5000/upload/tortia/סטייק.png","name":"טורטיה סטייק","description":"סטייק פרוס דק דק בטורטייה","price":"מחיר 47₪","time":"15 דק'"}
                            ,'טורטיה פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tortia/פורטובלו.png","name":"טורטיה פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בטורטייה","price":"מחיר 37₪","time":"15 דק'"}
                            ,'טורטיה המבורגר':
                            {"url":"http://10.0.2.2:5000/upload/tortia/המבורגר.png","name":"טורטיה המבורגר","description":"ההמבורגר העסיסי שאתם אוהבים בטורטייה.150G","price":"מחיר 39₪","time":"15 דק'"}
                            ,'טורטיה שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/tortia/שניצל-קריספי.png","name":"טורטיה שניצל קריספי","description":"100% חזה עוף מובחר בציפוי פריך בטורטייה","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'סנדוויצים':
                        {
                            'סנדוויץ חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/חזה-עוף.png","name":"סנדוויץ חזה עוף","description":"100% חזה עוף מוגש בלחמנית בורגר","price":"מחיר42₪","time":"15 דק'"}
                            ,'סנדוויץ סטייק':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/סטייק.png","name":"סנדוויץ סטייק","description":"סטייק פרוס דק דק מוגש בלחמנית בורגר","price":"מחיר 47₪","time":"15 דק'"}
                            ,'סנדוויץ פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/פורטובלו.png","name":"סנדוויץ פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית, מלח ופלפל מוגש בלחמנית בורגר","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סנדוויץ קורנביף':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/קורנביף.png","name":"סנדוויץ קורנביף ","description":"נתחי חזה בקר מעושן מוגש בלחמנית בורגר","price":"מחיר 47₪","time":"15 דק'"}
                            ,'סנדוויץ שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/sandwich/שניצל-קריספי.png","name":"סנדוויץ שניצל קריספי","description":"100% חזה עוף מובחר בציפוי פריך מוגש בלחמנית בורגר","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'ביסים':
                        {
                            'כנפיים':
                            {"url":"http://10.0.2.2:5000/upload/bisim/כנפיים.png","name":"כנפיים","description":"חצאי כנפיים מוקפצות ברוטב לבחירה10 חצאים","price":"מחיר 35₪","time":"15 דק'"}
                            ,'שניצלונים':
                            {"url":"http://10.0.2.2:5000/upload/bisim/שניצלונים.png","name":"שניצלונים","description":"רצועות של  100% חזה עוף מובחר בציפוי פריך","price":"מחיר 32₪","time":"15 דק'"}
                            ,'סיגר הבית':
                            {"url":"http://10.0.2.2:5000/upload/bisim/סיגר-הבית.png","name":"סיגר הבית","description":"סיגר מגולגל בעבודת יד, במילוי אסאדו מפורק","price":"מחיר 10₪","time":"15 דק'"}
                        }
                        ,'ארוחות ילדים':
                        {
                            'ארוחת-המבורגר':
                            {"url":"http://10.0.2.2:5000/upload/kids/ארוחת-המבורגר.png","name":"ארוחת-המבורגר","description":"המבורגר קלאסי + צ'יפס/ כדורי פירה / טבעות בצל","price":"מחיר 42₪","time":"15 דק'"}
                            ,'ארוחת-שניצלונים':
                            {"url":"http://10.0.2.2:5000/upload/kids/ארוחת-שניצלונים.png","name":"ארוחת-שניצלונים","description":"שניצלונים + צ'יפס / כדורי פירה / טבעות בצל","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'טבעוני':
                        {
                            'המבורגר ביונד':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/ביונד.png","name":"המבורגר ביונד","description":"ההמבורגר הטבעוני המושלם.100% בשר מהצומח בחווית טעם של הדבר האמיתי","price":"מחיר 49₪","time":"15 דק'"}
                            ,'המבורגר פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פורטבלו.png","name":"המבורגר פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית, מלח ופלפל מוגש בלחמנית בורגר","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פור3.png","name":"בגט פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בבאגט","price":"מחיר 37₪","time":"15 דק'"}
                            ,'טורטיה פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/tivoni/פורטובלו.png","name":"טורטיה פורטובלו","description":"פטריית פורטובלו צלויה על הגריל בתיבול שמן זית,מלח ופלפל בטורטייה","price":"מחיר 37₪","time":"15 דק'"}
                        }
                        ,'סלטים':
                        {
                            'סלט שוק':
                            {"url":"http://10.0.2.2:5000/upload/salade/שוק.png","name":"סלט שוק","description":"לבבות חסה, עגבניות שרי תמר, מלפפון, כרוב לבן וגזר בתיבול שמן זית ולימון","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סלט אסייתי':
                            {"url":"http://10.0.2.2:5000/upload/salade/אסייתי.png","name":"סלט אסייתי","description":"כרוב לבן וגזר בתיבול שמן זית ולימון","price":"מחיר 37₪","time":"15 דק'"}
                            ,'סלט קיסר עלים':
                            {"url":"http://10.0.2.2:5000/upload/salade/קיסרעלים.png","name":"סלט קיסר עלים","description":"לבבות חסה, בצל סגול, לבבות דקל, זיתי קלמטה, ביצה קשה מגורדת ושקדים קלויים בתיבול רוטב קיסר.","price":"מחיר 40₪","time":"15 דק'"}
                        }
                        ,'בגטים':
                        {
                            'בגט סטייק':
                            {"url":"http://10.0.2.2:5000/upload/baguet/סטייק.png","name":"בגט סטייק","description":"","price":"מחיר 47₪","time":"15 דק'"}
                             ,'בגט חזה עוף':
                            {"url":"http://10.0.2.2:5000/upload/baguet/haze.png","name":"בגט חזה עוף","description":"100% חזה עוף מובחר ","price":"מחיר 42₪","time":"15 דק'"}
                            ,'בגט פורטובלו':
                            {"url":"http://10.0.2.2:5000/upload/baguet/פורטובלו.png","name":"בגט פורטובלו","description":"","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט קורנביף':
                            {"url":"http://10.0.2.2:5000/upload/baguet/קורנביף.png","name":"בגט קורנביף","description":"נתחי חזה בקר מעושן","price":"מחיר 37₪","time":"15 דק'"}
                            ,'בגט שניצל קריספי':
                            {"url":"http://10.0.2.2:5000/upload/baguet/שניצל-קריספי.png","name":"בגט שניצל קריספי","description":"","price":"מחיר 37₪","time":"15 דק'"}
                        }
                    }
                }
        ,'landwer':
            {
                'ירושלים':
                     {
                        'סלטים':
                        {
                            'סלט איכרים איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטאיכריםאיטלקי.png","name":"סלט איכרים איטלקי","description":"כדורי מוצרלה, עגבניות, פלפל קלוי, עגבניות שרי, בצל סגול, חסה, רוקט, צנונית מוגש על פוקאצ'ה. ברוטב שמן זית וחומץ בלסמי.","price":"מחיר 39₪","time":"10 דק'"}
                        ,'סלט חלומי':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטחלומי.png","name":"סלט חלומי","description":"חלומי, עגבנייה, עגבניות שרי, מלפפון, פלפלים, צנונית, רוקט, זיתי קלמטה, בצל סגול, תערובת צמחי תבלין, ברוטב לימון ונענע.","price":"מחיר 39₪","time":"10 דק'"}
                            ,'סלט ים תיכוני':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטיםתיכוני.png","name":"סלט ים תיכוני","description":"פטה בתיבול זעתר וסומק, עגבניות שרי, עגבניות, מלפפונים, פלפלים צבעוניים, חסה, תערובת צמחי תבלין, זיתי קלמטה, צנוניות, ברוטב לימון נענע.","price":"מחיר 49₪","time":"10 דק'"}
                            ,'סלט ניסואז לימוני':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטניסואזלימוני.png","name":"סלט ניסואז לימוני","description":"טונה לימונית, אבוקדו (בעונה, או ברוקולי), ביצה קשה, קרעי תפוא, שעועית ירוקה, זיתי קלמטה, חסה, עגבנייה, רוקט, תערובת צמחי תבלין, צנונית ברוטב לימון ונענע","price":"מחיר 49₪","time":"10 דק'"}
                        }
                        ,'עיקריות':
                        {
                            'ביונד מיט':
                            {"url":"http://10.0.2.2:5000/upload1/maine/ביונדמיט.png","name":"ביונד מיט","description":"בורגול, ירקות שורש, טופו, בטטה, תרד, ברוקולי, ערמונים, טחינה, סילאן, עשבי תיבול (פטרוזיליה, בצל ירוק, בזיליקום), אגוזי מלך.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'למון וסלט רענן':
                            {"url":"http://10.0.2.2:5000/upload1/maine/סלמוןוסלטרענן.png","name":"סלמון וסלט רענן","description":"עגבניות שרי, זיתי קלמטה, גרגרי חומוס, בצל סגול, צנונית, פלפל קלוי, צמחי תבלין.","price":"מחיר 119₪","time":"10 דק'"}
                            ,'סלמון טריאקי':
                            {"url":"http://10.0.2.2:5000/upload1/maine/סלמוןטריאקי.png","name":"סלמון טריאקי","description":"פטריות, שום קונפי, גזר, צנון, שומשום ולימון.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיש & ציפס':
                            {"url":"http://10.0.2.2:5000/upload1/maine/פישאנדצ'יפס.png","name":"פיש & צ'יפס","description":"דג ים בציפוי פריך עם עשבי תיבול. איולי צ'יפוטלה (פיקנטי), איולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'תבשיל כוסמת':
                            {"url":"http://10.0.2.2:5000/upload1/maine/תבשילכוסמת.png","name":"תבשיל כוסמת","description":"בורגול, ירקות שורש, טופו, בטטה, תרד, ברוקולי, ערמונים, טחינה, סילאן, עשבי תיבול (פטרוזיליה, בצל ירוק, בזיליקום), אגוזי מלך.","price":"מחיר 32₪","time":"10 דק'"}
                        }
                        ,'פסטה ופיצה':
                        {
                            'פיצה עגבניות קלאסית':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פיצהעגבניותקלאסית.png","name":"פיצה עגבניות קלאסית","description":"מוצרלה, מיקרו בזיליקום.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה פסטו גבינות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פיצהפסטוגבינות.png","name":"פיצה פסטו גבינות","description":"גבינת עיזים, פטה, מוצרלה, פרמז'ן, מיקרו בזיליקום.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה בטטה שמנת ערמונים':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהבטטהשמנתערמונים.png","name":"פסטה בטטה שמנת ערמונים","description":"שמנת, שמן כמהין, בטטה, ערמונים ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה עגבניו תבזיליקום':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותבזיליקום.png","name":"פסטה עגבניו תבזיליקום","description":"שמן זית, שום, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן בבחירת טורצ'יו וללא פרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה עגבניות ורודות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותורודות.png","name":"פסטה עגבניות ורודות","description":"נגיעת שמנת, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה פטריות צלויות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהפטריותצלויות.png","name":"פסטה פטריות צלויות","description":"שמנת, שמן כמהין, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'רביולי גבינות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/רביוליגבינות.png","name":"רביולי גבינות","description":"רוטב לבחירה","price":"מחיר 32₪","time":"10 דק'"}    
                        }          
                        ,'כריכים וטסטים':                   
                        {

                            'בייגל טוסט איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי","description":"ממרח עגבניות מיובשות,פסטו, גבינה צהובה, חמאה ובזיליקום.  מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי","description":"","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט בולגרית':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטבולגרית.png","name":"בייגל טוסט בולגרית","description":"גבינה בולגרית, גבינה צהובה, עגבנייה, בצל בזעתר וזיתי קלמטה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט ירושלמי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטירושלמי.png","name":"בייגל טוסט ירושלמי","description":"ממרח עגבניות מיובשות, גבינה צהובה, ביצה קשה וזעתר.  מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט צהובה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטצהובה.png","name":"בייגל טוסט צהובה","description":"גבינה צהובה, עגבנייה, חמאה ובזיליקום מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך חביתה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךחביתה.png","name":"כריך חביתה","description":"מלפפון, עגבנייה, חסה וגבינת שמנת/טחינה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך טונה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךטונה.png","name":"כריך טונה","description":"סלט טונה, איולי, ביצה קשה, מלפפון חמוץ, רוקט ועגבנייה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך סלמון מעושן':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךסלמוןמעושן.png","name":"כריך סלמון מעושן","description":"סלמון מעושן, גבינת שמנת, צ'ילי,בצל ירוק ועגבניות שרי.","price":"מחיר 32₪","time":"10 דק'"}

                            }
                        ,'ארוחות בוקר':
                        {              
                            'בוקר גלילי':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרגלילי.png","name":"בוקר גלילי","description":"ביצת עין וסלט ירקות קצוץ מוגשים על פוקאצ'ה עם טחינה וזיתים בצד. ","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר טבעוני':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרטבעוני.png","name":"בוקר טבעוני","description":"חביתת עדשים אדומות ועשבי תיבול, סלט, פטה, טאבולה קינואה, זיתים, סלט אבוקדו, גבינת שמנת  ומוזלי.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר כל היום':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרכלהיום.png","name":"בוקר כל היום","description":"2 ביצים לבחירה, סלט ירקות טרי, לחם וגבינת שמנת / טחינה.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר לנדוור':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרלנדוור.png","name":"בוקר לנדוור","description":"ביצים לבחירה, סלט ירקות טרי, גבינת שמנת, פטה ולאבנה. קרם חצילים וממרח אבוקדו,  יוגורט וגרנולה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בנדיקט סלמון':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בנדיקטסלמון.png","name":"בנדיקט סלמון","description":"בריוש, ביצים עלומות, גבינת שמנת, סלמון מעושן, הולנדייז, עירית וסלט ירקות גינה.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'חצי כריך + שתייה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/חציכריך+שתייה.png","name":"חצי כריך + שתייה","description":"חצי כריך חביתה/חביתת עדשים אדומות + קפה/תה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'מוזלי':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/מוזלי.png","name":"מוזלי","description":"יוגורט, גרנולה, פירות, דבש","price":"מחיר 32₪","time":"10 דק'"}
                            ,'קפה ומאפה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/קפהומאפה.png","name":"קפה ומאפה","description":"מגוון מאפים מהבייקרי החדש של לנדוור","price":"מחיר 32₪","time":"10 דק'"}
                            ,'רביולי בטטה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/רביוליבטטה.png","name":"רביולי בטטה","description":"רטבים לבחירה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'שקשוקה קלאסית':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/שקשוקהקלאסית.png","name":"שקשוקה קלאסית","description":"מוגשת עם סלט, טחינה ולחמניית חלה","price":"מחיר 32₪","time":"10 דק'"}
                            }
                        ,'ארוחות ילדים':
                        {
                            'בוקר קטנטנים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/בוקרקטנטנים.png","name":"בוקר קטנטנים","description":"ביצה לבחירה, ירקות טריים, גבינה, טחינה, ריבה, פירות העונה וטוסטונים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'טוסט ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/טוסטילדים.png","name":"טוסט ילדים","description":"פסטה ברוטב עגבניות או שמנת לבחירה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדים.png","name":"פיצה ילדים","description":"ברוטב עגבניות ומוצרלה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה ילדים ללא גלוטן':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדיםללאגלוטן.png","name":"פיצה ילדים ללא גלוטן","description":"ברוטב עגבניות ומוצרלה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פסטהילדים.png","name":"פסטה ילדים","description":"פסטה ברוטב עגבניות או שמנת לבחירה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'שניצלוני דג ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/שניצלונידגילדים.png","name":"שניצלוני דג ילדים","description":"מוגשים עם צ'יפס, קטשופ, טחינה וירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                        }
                    }
                ,'רעננה':
                    {
                        'סלטים':
                        {
                            'סלט איכרים איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטאיכריםאיטלקי.png","name":"סלט איכרים איטלקי","description":"כדורי מוצרלה, עגבניות, פלפל קלוי, עגבניות שרי, בצל סגול, חסה, רוקט, צנונית מוגש על פוקאצ'ה. ברוטב שמן זית וחומץ בלסמי.","price":"מחיר 39₪","time":"10 דק'"}
                            ,'סלט חלומי':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטחלומי.png","name":"סלט חלומי","description":"חלומי, עגבנייה, עגבניות שרי, מלפפון, פלפלים, צנונית, רוקט, זיתי קלמטה, בצל סגול, תערובת צמחי תבלין, ברוטב לימון ונענע.","price":"מחיר 39₪","time":"10 דק'"}
                            ,'סלט ים תיכוני':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטיםתיכוני.png","name":"סלט ים תיכוני","description":"פטה בתיבול זעתר וסומק, עגבניות שרי, עגבניות, מלפפונים, פלפלים צבעוניים, חסה, תערובת צמחי תבלין, זיתי קלמטה, צנוניות, ברוטב לימון נענע.","price":"מחיר 49₪","time":"10 דק'"}
                            ,'סלט ניסואז לימוני':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטניסואזלימוני.png","name":"סלט ניסואז לימוני","description":"טונה לימונית, אבוקדו (בעונה, או ברוקולי), ביצה קשה, קרעי תפוא, שעועית ירוקה, זיתי קלמטה, חסה, עגבנייה, רוקט, תערובת צמחי תבלין, צנונית ברוטב לימון ונענע","price":"מחיר 49₪","time":"10 דק'"}
                        }
                        ,'עיקריות':
                        {
                            'ביונד מיט':
                            {"url":"http://10.0.2.2:5000/upload1/maine/ביונדמיט.png","name":"ביונד מיט","description":"בורגול, ירקות שורש, טופו, בטטה, תרד, ברוקולי, ערמונים, טחינה, סילאן, עשבי תיבול (פטרוזיליה, בצל ירוק, בזיליקום), אגוזי מלך.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'למון וסלט רענן':
                            {"url":"http://10.0.2.2:5000/upload1/maine/סלמוןוסלטרענן.png","name":"סלמון וסלט רענן","description":"עגבניות שרי, זיתי קלמטה, גרגרי חומוס, בצל סגול, צנונית, פלפל קלוי, צמחי תבלין.","price":"מחיר 119₪","time":"10 דק'"}
                            ,'סלמון טריאקי':
                            {"url":"http://10.0.2.2:5000/upload1/maine/סלמוןטריאקי.png","name":"סלמון טריאקי","description":"פטריות, שום קונפי, גזר, צנון, שומשום ולימון.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיש & ציפס':
                            {"url":"http://10.0.2.2:5000/upload1/maine/פישאנדצ'יפס.png","name":"פיש & צ'יפס","description":"דג ים בציפוי פריך עם עשבי תיבול. איולי צ'יפוטלה (פיקנטי), איולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'תבשיל כוסמת':
                            {"url":"http://10.0.2.2:5000/upload1/maine/תבשילכוסמת.png","name":"תבשיל כוסמת","description":"בורגול, ירקות שורש, טופו, בטטה, תרד, ברוקולי, ערמונים, טחינה, סילאן, עשבי תיבול (פטרוזיליה, בצל ירוק, בזיליקום), אגוזי מלך.","price":"מחיר 32₪","time":"10 דק'"}
                        }
                        ,'פסטה ופיצה':
                        {
                            'פיצה עגבניות קלאסית':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פיצהעגבניותקלאסית.png","name":"פיצה עגבניות קלאסית","description":"מוצרלה, מיקרו בזיליקום.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה פסטו גבינות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פיצהפסטוגבינות.png","name":"פיצה פסטו גבינות","description":"גבינת עיזים, פטה, מוצרלה, פרמז'ן, מיקרו בזיליקום.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה בטטה שמנת ערמונים':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהבטטהשמנתערמונים.png","name":"פסטה בטטה שמנת ערמונים","description":"שמנת, שמן כמהין, בטטה, ערמונים ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה עגבניו תבזיליקום':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותבזיליקום.png","name":"פסטה עגבניו תבזיליקום","description":"שמן זית, שום, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן בבחירת טורצ'יו וללא פרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה עגבניות ורודות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותורודות.png","name":"פסטה עגבניות ורודות","description":"נגיעת שמנת, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה פטריות צלויות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהפטריותצלויות.png","name":"פסטה פטריות צלויות","description":"שמנת, שמן כמהין, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'רביולי גבינות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/רביוליגבינות.png","name":"רביולי גבינות","description":"רוטב לבחירה","price":"מחיר 32₪","time":"10 דק'"}    
                        }          
                        ,'כריכים וטסטים':                   
                        {

                            'בייגל טוסט איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי","description":"ממרח עגבניות מיובשות,פסטו, גבינה צהובה, חמאה ובזיליקום.  מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי","description":"","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט בולגרית':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטבולגרית.png","name":"בייגל טוסט בולגרית","description":"גבינה בולגרית, גבינה צהובה, עגבנייה, בצל בזעתר וזיתי קלמטה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט ירושלמי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטירושלמי.png","name":"בייגל טוסט ירושלמי","description":"ממרח עגבניות מיובשות, גבינה צהובה, ביצה קשה וזעתר.  מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט צהובה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטצהובה.png","name":"בייגל טוסט צהובה","description":"גבינה צהובה, עגבנייה, חמאה ובזיליקום מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך חביתה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךחביתה.png","name":"כריך חביתה","description":"מלפפון, עגבנייה, חסה וגבינת שמנת/טחינה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך טונה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךטונה.png","name":"כריך טונה","description":"סלט טונה, איולי, ביצה קשה, מלפפון חמוץ, רוקט ועגבנייה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך סלמון מעושן':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךסלמוןמעושן.png","name":"כריך סלמון מעושן","description":"סלמון מעושן, גבינת שמנת, צ'ילי,בצל ירוק ועגבניות שרי.","price":"מחיר 32₪","time":"10 דק'"}

                            }
                        ,'ארוחות בוקר':
                        {              
                            'בוקר גלילי':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרגלילי.png","name":"בוקר גלילי","description":"ביצת עין וסלט ירקות קצוץ מוגשים על פוקאצ'ה עם טחינה וזיתים בצד. ","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר טבעוני':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרטבעוני.png","name":"בוקר טבעוני","description":"חביתת עדשים אדומות ועשבי תיבול, סלט, פטה, טאבולה קינואה, זיתים, סלט אבוקדו, גבינת שמנת  ומוזלי.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר כל היום':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרכלהיום.png","name":"בוקר כל היום","description":"2 ביצים לבחירה, סלט ירקות טרי, לחם וגבינת שמנת / טחינה.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר לנדוור':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרלנדוור.png","name":"בוקר לנדוור","description":"ביצים לבחירה, סלט ירקות טרי, גבינת שמנת, פטה ולאבנה. קרם חצילים וממרח אבוקדו,  יוגורט וגרנולה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בנדיקט סלמון':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בנדיקטסלמון.png","name":"בנדיקט סלמון","description":"בריוש, ביצים עלומות, גבינת שמנת, סלמון מעושן, הולנדייז, עירית וסלט ירקות גינה.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'חצי כריך + שתייה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/חציכריך+שתייה.png","name":"חצי כריך + שתייה","description":"חצי כריך חביתה/חביתת עדשים אדומות + קפה/תה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'מוזלי':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/מוזלי.png","name":"מוזלי","description":"יוגורט, גרנולה, פירות, דבש","price":"מחיר 32₪","time":"10 דק'"}
                            ,'קפה ומאפה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/קפהומאפה.png","name":"קפה ומאפה","description":"מגוון מאפים מהבייקרי החדש של לנדוור","price":"מחיר 32₪","time":"10 דק'"}
                            ,'רביולי בטטה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/רביוליבטטה.png","name":"רביולי בטטה","description":"רטבים לבחירה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'שקשוקה קלאסית':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/שקשוקהקלאסית.png","name":"שקשוקה קלאסית","description":"מוגשת עם סלט, טחינה ולחמניית חלה","price":"מחיר 32₪","time":"10 דק'"}
                            }
                        ,'ארוחות ילדים':
                        {
                            'בוקר קטנטנים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/בוקרקטנטנים.png","name":"בוקר קטנטנים","description":"ביצה לבחירה, ירקות טריים, גבינה, טחינה, ריבה, פירות העונה וטוסטונים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'טוסט ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/טוסטילדים.png","name":"טוסט ילדים","description":"פסטה ברוטב עגבניות או שמנת לבחירה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדים.png","name":"פיצה ילדים","description":"ברוטב עגבניות ומוצרלה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה ילדים ללא גלוטן':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדיםללאגלוטן.png","name":"פיצה ילדים ללא גלוטן","description":"ברוטב עגבניות ומוצרלה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פסטהילדים.png","name":"פסטה ילדים","description":"פסטה ברוטב עגבניות או שמנת לבחירה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'שניצלוני דג ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/שניצלונידגילדים.png","name":"שניצלוני דג ילדים","description":"מוגשים עם צ'יפס, קטשופ, טחינה וירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                        }
                    }
                ,'אשדוד':
                   {
                        'סלטים':
                        {
                            'סלט איכרים איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטאיכריםאיטלקי.png","name":"סלט איכרים איטלקי","description":"כדורי מוצרלה, עגבניות, פלפל קלוי, עגבניות שרי, בצל סגול, חסה, רוקט, צנונית מוגש על פוקאצ'ה. ברוטב שמן זית וחומץ בלסמי.","price":"מחיר 39₪","time":"10 דק'"}
                            ,'סלט חלומי':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטחלומי.png","name":"סלט חלומי","description":"חלומי, עגבנייה, עגבניות שרי, מלפפון, פלפלים, צנונית, רוקט, זיתי קלמטה, בצל סגול, תערובת צמחי תבלין, ברוטב לימון ונענע.","price":"מחיר 39₪","time":"10 דק'"}
                            ,'סלט ים תיכוני':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטיםתיכוני.png","name":"סלט ים תיכוני","description":"פטה בתיבול זעתר וסומק, עגבניות שרי, עגבניות, מלפפונים, פלפלים צבעוניים, חסה, תערובת צמחי תבלין, זיתי קלמטה, צנוניות, ברוטב לימון נענע.","price":"מחיר 49₪","time":"10 דק'"}
                            ,'סלט ניסואז לימוני':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטניסואזלימוני.png","name":"סלט ניסואז לימוני","description":"טונה לימונית, אבוקדו (בעונה, או ברוקולי), ביצה קשה, קרעי תפוא, שעועית ירוקה, זיתי קלמטה, חסה, עגבנייה, רוקט, תערובת צמחי תבלין, צנונית ברוטב לימון ונענע","price":"מחיר 49₪","time":"10 דק'"}
                        }
                        ,'עיקריות':
                        {
                            'ביונד מיט':
                            {"url":"http://10.0.2.2:5000/upload1/maine/ביונדמיט.png","name":"ביונד מיט","description":"בורגול, ירקות שורש, טופו, בטטה, תרד, ברוקולי, ערמונים, טחינה, סילאן, עשבי תיבול (פטרוזיליה, בצל ירוק, בזיליקום), אגוזי מלך.","price":"מחיר 32₪"},"time":"10 דק'"
                            ,'למון וסלט רענן':
                            {"url":"http://10.0.2.2:5000/upload1/maine/סלמוןוסלטרענן.png","name":"סלמון וסלט רענן","description":"עגבניות שרי, זיתי קלמטה, גרגרי חומוס, בצל סגול, צנונית, פלפל קלוי, צמחי תבלין.","price":"מחיר 119₪","time":"10 דק'"}
                            ,'סלמון טריאקי':
                            {"url":"http://10.0.2.2:5000/upload1/maine/סלמוןטריאקי.png","name":"סלמון טריאקי","description":"פטריות, שום קונפי, גזר, צנון, שומשום ולימון.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיש & ציפס':
                            {"url":"http://10.0.2.2:5000/upload1/maine/פישאנדצ'יפס.png","name":"פיש & צ'יפס","description":"דג ים בציפוי פריך עם עשבי תיבול. איולי צ'יפוטלה (פיקנטי), איולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'תבשיל כוסמת':
                            {"url":"http://10.0.2.2:5000/upload1/maine/תבשילכוסמת.png","name":"תבשיל כוסמת","description":"בורגול, ירקות שורש, טופו, בטטה, תרד, ברוקולי, ערמונים, טחינה, סילאן, עשבי תיבול (פטרוזיליה, בצל ירוק, בזיליקום), אגוזי מלך.","price":"מחיר 32₪","time":"10 דק'"}
                        }
                        ,'פסטה ופיצה':
                        {
                            'פיצה עגבניות קלאסית':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פיצהעגבניותקלאסית.png","name":"פיצה עגבניות קלאסית","description":"מוצרלה, מיקרו בזיליקום.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה פסטו גבינות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פיצהפסטוגבינות.png","name":"פיצה פסטו גבינות","description":"גבינת עיזים, פטה, מוצרלה, פרמז'ן, מיקרו בזיליקום.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה בטטה שמנת ערמונים':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהבטטהשמנתערמונים.png","name":"פסטה בטטה שמנת ערמונים","description":"שמנת, שמן כמהין, בטטה, ערמונים ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה עגבניו תבזיליקום':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותבזיליקום.png","name":"פסטה עגבניו תבזיליקום","description":"שמן זית, שום, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן בבחירת טורצ'יו וללא פרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה עגבניות ורודות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותורודות.png","name":"פסטה עגבניות ורודות","description":"נגיעת שמנת, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה פטריות צלויות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהפטריותצלויות.png","name":"פסטה פטריות צלויות","description":"שמנת, שמן כמהין, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'רביולי גבינות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/רביוליגבינות.png","name":"רביולי גבינות","description":"רוטב לבחירה","price":"מחיר 32₪","time":"10 דק'"}    
                        }          
                        ,'כריכים וטסטים':                   
                        {

                            'בייגל טוסט איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי","description":"ממרח עגבניות מיובשות,פסטו, גבינה צהובה, חמאה ובזיליקום.  מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי","description":"","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט בולגרית':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטבולגרית.png","name":"בייגל טוסט בולגרית","description":"גבינה בולגרית, גבינה צהובה, עגבנייה, בצל בזעתר וזיתי קלמטה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט ירושלמי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטירושלמי.png","name":"בייגל טוסט ירושלמי","description":"ממרח עגבניות מיובשות, גבינה צהובה, ביצה קשה וזעתר.  מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט צהובה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטצהובה.png","name":"בייגל טוסט צהובה","description":"גבינה צהובה, עגבנייה, חמאה ובזיליקום מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך חביתה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךחביתה.png","name":"כריך חביתה","description":"מלפפון, עגבנייה, חסה וגבינת שמנת/טחינה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך טונה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךטונה.png","name":"כריך טונה","description":"סלט טונה, איולי, ביצה קשה, מלפפון חמוץ, רוקט ועגבנייה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך סלמון מעושן':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךסלמוןמעושן.png","name":"כריך סלמון מעושן","description":"סלמון מעושן, גבינת שמנת, צ'ילי,בצל ירוק ועגבניות שרי.","price":"מחיר 32₪","time":"10 דק'"}

                            }
                        ,'ארוחות בוקר':
                        {              
                            'בוקר גלילי':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרגלילי.png","name":"בוקר גלילי","description":"ביצת עין וסלט ירקות קצוץ מוגשים על פוקאצ'ה עם טחינה וזיתים בצד. ","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר טבעוני':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרטבעוני.png","name":"בוקר טבעוני","description":"חביתת עדשים אדומות ועשבי תיבול, סלט, פטה, טאבולה קינואה, זיתים, סלט אבוקדו, גבינת שמנת  ומוזלי.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר כל היום':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרכלהיום.png","name":"בוקר כל היום","description":"2 ביצים לבחירה, סלט ירקות טרי, לחם וגבינת שמנת / טחינה.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר לנדוור':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרלנדוור.png","name":"בוקר לנדוור","description":"ביצים לבחירה, סלט ירקות טרי, גבינת שמנת, פטה ולאבנה. קרם חצילים וממרח אבוקדו,  יוגורט וגרנולה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בנדיקט סלמון':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בנדיקטסלמון.png","name":"בנדיקט סלמון","description":"בריוש, ביצים עלומות, גבינת שמנת, סלמון מעושן, הולנדייז, עירית וסלט ירקות גינה.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'חצי כריך + שתייה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/חציכריך+שתייה.png","name":"חצי כריך + שתייה","description":"חצי כריך חביתה/חביתת עדשים אדומות + קפה/תה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'מוזלי':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/מוזלי.png","name":"מוזלי","description":"יוגורט, גרנולה, פירות, דבש","price":"מחיר 32₪","time":"10 דק'"}
                            ,'קפה ומאפה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/קפהומאפה.png","name":"קפה ומאפה","description":"מגוון מאפים מהבייקרי החדש של לנדוור","price":"מחיר 32₪","time":"10 דק'"}
                            ,'רביולי בטטה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/רביוליבטטה.png","name":"רביולי בטטה","description":"רטבים לבחירה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'שקשוקה קלאסית':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/שקשוקהקלאסית.png","name":"שקשוקה קלאסית","description":"מוגשת עם סלט, טחינה ולחמניית חלה","price":"מחיר 32₪","time":"10 דק'"}
                            }
                        ,'ארוחות ילדים':
                        {
                            'בוקר קטנטנים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/בוקרקטנטנים.png","name":"בוקר קטנטנים","description":"ביצה לבחירה, ירקות טריים, גבינה, טחינה, ריבה, פירות העונה וטוסטונים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'טוסט ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/טוסטילדים.png","name":"טוסט ילדים","description":"פסטה ברוטב עגבניות או שמנת לבחירה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדים.png","name":"פיצה ילדים","description":"ברוטב עגבניות ומוצרלה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה ילדים ללא גלוטן':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדיםללאגלוטן.png","name":"פיצה ילדים ללא גלוטן","description":"ברוטב עגבניות ומוצרלה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פסטהילדים.png","name":"פסטה ילדים","description":"פסטה ברוטב עגבניות או שמנת לבחירה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'שניצלוני דג ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/שניצלונידגילדים.png","name":"שניצלוני דג ילדים","description":"מוגשים עם צ'יפס, קטשופ, טחינה וירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                        }
                    }
                ,'נתניה':
                    {
                        'סלטים':
                        {
                            'סלט איכרים איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטאיכריםאיטלקי.png","name":"סלט איכרים איטלקי","description":"כדורי מוצרלה, עגבניות, פלפל קלוי, עגבניות שרי, בצל סגול, חסה, רוקט, צנונית מוגש על פוקאצ'ה. ברוטב שמן זית וחומץ בלסמי.","price":"מחיר 39₪","time":"10 דק'"}
                             ,'סלט חלומי':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטחלומי.png","name":"סלט חלומי","description":"חלומי, עגבנייה, עגבניות שרי, מלפפון, פלפלים, צנונית, רוקט, זיתי קלמטה, בצל סגול, תערובת צמחי תבלין, ברוטב לימון ונענע.","price":"מחיר 39₪","time":"10 דק'"}
                            ,'סלט ים תיכוני':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטיםתיכוני.png","name":"סלט ים תיכוני","description":"פטה בתיבול זעתר וסומק, עגבניות שרי, עגבניות, מלפפונים, פלפלים צבעוניים, חסה, תערובת צמחי תבלין, זיתי קלמטה, צנוניות, ברוטב לימון נענע.","price":"מחיר 49₪","time":"10 דק'"}
                            ,'סלט ניסואז לימוני':
                            {"url":"http://10.0.2.2:5000/upload1/salade/סלטניסואזלימוני.png","name":"סלט ניסואז לימוני","description":"טונה לימונית, אבוקדו (בעונה, או ברוקולי), ביצה קשה, קרעי תפוא, שעועית ירוקה, זיתי קלמטה, חסה, עגבנייה, רוקט, תערובת צמחי תבלין, צנונית ברוטב לימון ונענע","price":"מחיר 49₪","time":"10 דק'"}
                        }
                        ,'עיקריות':
                        {
                            'ביונד מיט':
                            {"url":"http://10.0.2.2:5000/upload1/maine/ביונדמיט.png","name":"ביונד מיט","description":"בורגול, ירקות שורש, טופו, בטטה, תרד, ברוקולי, ערמונים, טחינה, סילאן, עשבי תיבול (פטרוזיליה, בצל ירוק, בזיליקום), אגוזי מלך.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'למון וסלט רענן':
                            {"url":"http://10.0.2.2:5000/upload1/maine/סלמוןוסלטרענן.png","name":"סלמון וסלט רענן","description":"עגבניות שרי, זיתי קלמטה, גרגרי חומוס, בצל סגול, צנונית, פלפל קלוי, צמחי תבלין.","price":"מחיר 119₪","time":"10 דק'"}
                            ,'סלמון טריאקי':
                            {"url":"http://10.0.2.2:5000/upload1/maine/סלמוןטריאקי.png","name":"סלמון טריאקי","description":"פטריות, שום קונפי, גזר, צנון, שומשום ולימון.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיש & ציפס':
                            {"url":"http://10.0.2.2:5000/upload1/maine/פישאנדצ'יפס.png","name":"פיש & צ'יפס","description":"דג ים בציפוי פריך עם עשבי תיבול. איולי צ'יפוטלה (פיקנטי), איולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'תבשיל כוסמת':
                            {"url":"http://10.0.2.2:5000/upload1/maine/תבשילכוסמת.png","name":"תבשיל כוסמת","description":"בורגול, ירקות שורש, טופו, בטטה, תרד, ברוקולי, ערמונים, טחינה, סילאן, עשבי תיבול (פטרוזיליה, בצל ירוק, בזיליקום), אגוזי מלך.","price":"מחיר 32₪","time":"10 דק'"}
                        }
                        ,'פסטה ופיצה':
                        {
                            'פיצה עגבניות קלאסית':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פיצהעגבניותקלאסית.png","name":"פיצה עגבניות קלאסית","description":"מוצרלה, מיקרו בזיליקום.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה פסטו גבינות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פיצהפסטוגבינות.png","name":"פיצה פסטו גבינות","description":"גבינת עיזים, פטה, מוצרלה, פרמז'ן, מיקרו בזיליקום.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה בטטה שמנת ערמונים':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהבטטהשמנתערמונים.png","name":"פסטה בטטה שמנת ערמונים","description":"שמנת, שמן כמהין, בטטה, ערמונים ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה עגבניו תבזיליקום':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותבזיליקום.png","name":"פסטה עגבניו תבזיליקום","description":"שמן זית, שום, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן בבחירת טורצ'יו וללא פרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה עגבניות ורודות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהעגבניותורודות.png","name":"פסטה עגבניות ורודות","description":"נגיעת שמנת, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה פטריות צלויות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/פסטהפטריותצלויות.png","name":"פסטה פטריות צלויות","description":"שמנת, שמן כמהין, צמחי תבלין, מיקרו בזיליקום ופרמז׳ן.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'רביולי גבינות':
                            {"url":"http://10.0.2.2:5000/upload1/pasta/רביוליגבינות.png","name":"רביולי גבינות","description":"רוטב לבחירה","price":"מחיר 32₪","time":"10 דק'"}    
                        }          
                        ,'כריכים וטסטים':                   
                        {

                            'בייגל טוסט איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי","description":"ממרח עגבניות מיובשות,פסטו, גבינה צהובה, חמאה ובזיליקום.  מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט איטלקי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטאיטלקי.png","name":"בייגל טוסט איטלקי","description":"","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט בולגרית':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטבולגרית.png","name":"בייגל טוסט בולגרית","description":"גבינה בולגרית, גבינה צהובה, עגבנייה, בצל בזעתר וזיתי קלמטה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט ירושלמי':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטירושלמי.png","name":"בייגל טוסט ירושלמי","description":"ממרח עגבניות מיובשות, גבינה צהובה, ביצה קשה וזעתר.  מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בייגל טוסט צהובה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/בייגלטוסטצהובה.png","name":"בייגל טוסט צהובה","description":"גבינה צהובה, עגבנייה, חמאה ובזיליקום מוגש עם סלט ירוק ואיולי פסטו.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך חביתה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךחביתה.png","name":"כריך חביתה","description":"מלפפון, עגבנייה, חסה וגבינת שמנת/טחינה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך טונה':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךטונה.png","name":"כריך טונה","description":"סלט טונה, איולי, ביצה קשה, מלפפון חמוץ, רוקט ועגבנייה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'כריך סלמון מעושן':
                            {"url":"http://10.0.2.2:5000/upload1/toast/כריךסלמוןמעושן.png","name":"כריך סלמון מעושן","description":"סלמון מעושן, גבינת שמנת, צ'ילי,בצל ירוק ועגבניות שרי.","price":"מחיר 32₪","time":"10 דק'"}

                            }
                        ,'ארוחות בוקר':
                        {              
                            'בוקר גלילי':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרגלילי.png","name":"בוקר גלילי","description":"ביצת עין וסלט ירקות קצוץ מוגשים על פוקאצ'ה עם טחינה וזיתים בצד. ","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר טבעוני':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרטבעוני.png","name":"בוקר טבעוני","description":"חביתת עדשים אדומות ועשבי תיבול, סלט, פטה, טאבולה קינואה, זיתים, סלט אבוקדו, גבינת שמנת  ומוזלי.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר כל היום':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרכלהיום.png","name":"בוקר כל היום","description":"2 ביצים לבחירה, סלט ירקות טרי, לחם וגבינת שמנת / טחינה.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בוקר לנדוור':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בוקרלנדוור.png","name":"בוקר לנדוור","description":"ביצים לבחירה, סלט ירקות טרי, גבינת שמנת, פטה ולאבנה. קרם חצילים וממרח אבוקדו,  יוגורט וגרנולה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'בנדיקט סלמון':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/בנדיקטסלמון.png","name":"בנדיקט סלמון","description":"בריוש, ביצים עלומות, גבינת שמנת, סלמון מעושן, הולנדייז, עירית וסלט ירקות גינה.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'חצי כריך + שתייה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/חציכריך+שתייה.png","name":"חצי כריך + שתייה","description":"חצי כריך חביתה/חביתת עדשים אדומות + קפה/תה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'מוזלי':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/מוזלי.png","name":"מוזלי","description":"יוגורט, גרנולה, פירות, דבש","price":"מחיר 32₪","time":"10 דק'"}
                            ,'קפה ומאפה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/קפהומאפה.png","name":"קפה ומאפה","description":"מגוון מאפים מהבייקרי החדש של לנדוור","price":"מחיר 32₪","time":"10 דק'"}
                            ,'רביולי בטטה':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/רביוליבטטה.png","name":"רביולי בטטה","description":"רטבים לבחירה","price":"מחיר 32₪","time":"10 דק'"}
                            ,'שקשוקה קלאסית':
                            {"url":"http://10.0.2.2:5000/upload1/breakfast/שקשוקהקלאסית.png","name":"שקשוקה קלאסית","description":"מוגשת עם סלט, טחינה ולחמניית חלה","price":"מחיר 32₪","time":"10 דק'"}
                            }
                        ,'ארוחות ילדים':
                        {
                            'בוקר קטנטנים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/בוקרקטנטנים.png","name":"בוקר קטנטנים","description":"ביצה לבחירה, ירקות טריים, גבינה, טחינה, ריבה, פירות העונה וטוסטונים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'טוסט ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/טוסטילדים.png","name":"טוסט ילדים","description":"פסטה ברוטב עגבניות או שמנת לבחירה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדים.png","name":"פיצה ילדים","description":"ברוטב עגבניות ומוצרלה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פיצה ילדים ללא גלוטן':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פיצהילדיםללאגלוטן.png","name":"פיצה ילדים ללא גלוטן","description":"ברוטב עגבניות ומוצרלה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'פסטה ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/פסטהילדים.png","name":"פסטה ילדים","description":"פסטה ברוטב עגבניות או שמנת לבחירה, מוגשת עם ירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'שניצלוני דג ילדים':
                            {"url":"http://10.0.2.2:5000/upload1/kids/שניצלונידגילדים.png","name":"שניצלוני דג ילדים","description":"מוגשים עם צ'יפס, קטשופ, טחינה וירקות טריים חתוכים.","price":"מחיר 32₪","time":"10 דק'"}
                        }
                    }
            }   
        ,'Japanika':
            {
                'ירושלים':
                    {
                        'אורז וגריל':
                        {
                            'פאד קפאו בקר':
                            {"url":"http://10.0.2.2:5000/upload2/rice/3פאד-קפאו-בקר.jpg","name":"פאד קפאו בקר","description":"בשר עגל קצוץ בתיבול תאילנדי, פלפלים, בצל, עלי נענע, למון גראס וקפיר ליים.","price":"מחיר 57₪","time":"15 דק'"}
                            ,'דג בקשיו':
                            {"url":"http://10.0.2.2:5000/upload2/rice/דג-בקשיו.jpg","name":"דג בקשיו","description":"רצועות דג בטמפורה מוקפצות ברוטב צ'ילי תמרינדי עם פלפל מתוק מעושן","price":"מחיר 59₪","time":"15 דק'"}
                            ,'חמוץ מתוק':
                            {"url":"http://10.0.2.2:5000/upload2/rice/חמוץ-מתוק.png","name":"חמוץ מתוק","description":"כדורי עוף בטמפורה מוקפצים ברוטב חמוץ מתוק עם פטריות שמפניון, פלפלים.","price":"מחיר 56₪","time":"15 דק'"}
                           }
                        ,'מנות ווק':
                        {                    
                            'צאנג מאי בקר':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-בקר.png","name":"צאנג מאי בקר","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 57₪","time":"15 דק'"}
                            ,'צאנג מאי טופו':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-טופו.png","name":"צאנג מאי טופו","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 52₪","time":"15 דק'"}
                            ,'צאנג מאי ירקות':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-ירקות.png","name":"צאנג מאי ירקות","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 49₪","time":"15 דק'"}
                            ,'צאנג מאי עוף':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-עוף.png","name":"צאנג מאי עוף","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 54₪","time":"15 דק'"}
                        }
                         ,'ספיישל סושי':
                        {
                            'גפנקו':
                            {"url":"http://10.0.2.2:5000/upload2/special/גפנקו.png","name":"גפנקו","description":"I/O בציפוי פנקו, מוגש חם עם רוטב טריאקי","price":"מחיר 39₪","time":"15 דק'"}
                            ,'מנטה רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/מנטה-רול.png","name":"מנטה רול","description":"סלמון נא, אבוקדו, כוסברה, נענע וחסה אייסברג בציפוי סלמון נא ושבבי בטטה.","price":"מחיר 48₪","time":"15 דק'"}
                            ,'סלמון ליים רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/סלמון-ליים-רול.png","name":"סלמון ליים רול","description":"סלמון נא, אבוקדו, שיטאקי ופלחי לימון בציפוי סלמון מעושן, אבוקדו ופלחי לימון.","price":"מחיר 44₪","time":"15 דק'"}
                            ,'סנסט':
                            {"url":"http://10.0.2.2:5000/upload2/special/סנסט.png","name":"סנסט","description":"סלמון בטמפורה, אבוקדו, מלפפון ועירית בציפוי בטטה.","price":"מחיר 44₪","time":"15 דק'"}
                            ,'קריספי רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/קריספי-רול.png","name":"קריספי רול","description":"ספייסי סלמון/סלמון טמפורה, אבוקדו ובטטה בציפוי סלמון גריל","price":"מחיר 49₪","time":"15 דק'"}
                        }
                        ,'מרקים':
                        {
                            'מרק מיסו':
                            {"url":"http://10.0.2.2:5000/upload2/soup/אדום.png","name":"מרק מיסו","description":"מרק יפני מסורתי עם ציר דאשי, קוביות טופו, אצות וואקמה ובצל ירוק.","price":"מחיר 19₪","time":"15 דק'"}
                            ,'טום יאם ירקות':
                            {"url":"http://10.0.2.2:5000/upload2/soup/ירוק.png","name":"טום יאם ירקות","description":"עם ציר עוף, חלב קוקוס, אטריות שעועית, ירקות וקישוט כוסברה.","price":"מחיר 32₪","time":"15 דק'"}
                            ,'מרק תירס תאילנדי':
                            {"url":"http://10.0.2.2:5000/upload2/soup/צהוב.png","name":"מרק תירס תאילנדי","description":"עם קארי אדום, חלב קוקוס, אטריות אודון ועוף.","price":"מחיר 32₪","time":"15 דק'"}     
                        }            
                        ,'ארוחות ילדים':
                        {
                            'אצבעות עוף':
                            {"url":"http://10.0.2.2:5000/upload2/kids/אצבעות-עוף.png","name":"אצבעות עוף","description":"אצבעות עוף בציפוי פנקו בתוספת אורז מאודה וקטשופ.","price":"מחיר 42₪","time":"15 דק'"}
                            ,'פרש נודלס':
                            {"url":"http://10.0.2.2:5000/upload2/kids/פרש-קידס-נודלס-עוף.png","name":"פרש נודלס","description":"אטריות טריות מוקפצות בטריאקי עם טופו / רצועות עוף","price":"מחיר 42₪","time":"15 דק'"}
                            ,'קריספי ציקן':
                            {"url":"http://10.0.2.2:5000/upload2/kids/קריספי-ציקן-קידס.png","name":"קריספי ציקן","description":"כדורי עוף פריכים בתוספת אורז מאודה וקטשופ.","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'מנות פתיחה':
                        {
                            'אדממה':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/אדממה.png","name":"אדממה","description":"פולי סויה ירוקה עם מלח ים ופלח לימון.","price":"מחיר 19₪","time":"15 דק'"}
                            ,'חמוצים יפניים':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/חמוצים-יפניים.png","name":"חמוצים יפניים","description":"כרוב, גזר, מלפפון, פלפלים וצנון, בקישוט שומשום קלוי.","price":"מחיר 19₪","time":"15 דק'"}
                            ,'קריספי בטטה':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/קריספי-בטטה.png","name":"קריספי בטטה","description":"רצועות בטטה בטמפורה מוגשות עם רוטב טריאקי.","price":"מחיר 26₪","time":"15 דק'"}
                        }
                    }
                    
                ,'אשדוד':
                    {
                        'אורז וגריל':
                        {
                            'פאד קפאו בקר':
                            {"url":"http://10.0.2.2:5000/upload2/rice/3פאד-קפאו-בקר.jpg","name":"פאד קפאו בקר","description":"בשר עגל קצוץ בתיבול תאילנדי, פלפלים, בצל, עלי נענע, למון גראס וקפיר ליים.","price":"מחיר 57₪","time":"15 דק'"}
                            ,'דג בקשיו':
                            {"url":"http://10.0.2.2:5000/upload2/rice/דג-בקשיו.jpg","name":"דג בקשיו","description":"רצועות דג בטמפורה מוקפצות ברוטב צ'ילי תמרינדי עם פלפל מתוק מעושן","price":"מחיר 59₪","time":"15 דק'"}
                            ,'חמוץ מתוק':
                            {"url":"http://10.0.2.2:5000/upload2/rice/חמוץ-מתוק.png","name":"חמוץ מתוק","description":"כדורי עוף בטמפורה מוקפצים ברוטב חמוץ מתוק עם פטריות שמפניון, פלפלים.","price":"מחיר 56₪","time":"15 דק'"}
                        }
                        ,'מנות ווק':
                        {                    
                            'צאנג מאי בקר':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-בקר.png","name":"צאנג מאי בקר","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 57₪","time":"15 דק'"}
                            ,'צאנג מאי טופו':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-טופו.png","name":"צאנג מאי טופו","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 52₪","time":"15 דק'"}
                            ,'צאנג מאי ירקות':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-ירקות.png","name":"צאנג מאי ירקות","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 49₪","time":"15 דק'"}
                            ,'צאנג מאי עוף':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-עוף.png","name":"צאנג מאי עוף","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 54₪","time":"15 דק'"}
                        }
                         ,'ספיישל סושי':
                        {
                            'גפנקו':
                            {"url":"http://10.0.2.2:5000/upload2/special/גפנקו.png","name":"גפנקו","description":"I/O בציפוי פנקו, מוגש חם עם רוטב טריאקי","price":"מחיר 39₪","time":"10 דק'"}
                            ,'מנטה רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/מנטה-רול.png","name":"מנטה רול","description":"סלמון נא, אבוקדו, כוסברה, נענע וחסה אייסברג בציפוי סלמון נא ושבבי בטטה.","price":"מחיר 48₪","time":"10 דק'"}
                            ,'סלמון ליים רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/סלמון-ליים-רול.png","name":"סלמון ליים רול","description":"סלמון נא, אבוקדו, שיטאקי ופלחי לימון בציפוי סלמון מעושן, אבוקדו ופלחי לימון.","price":"מחיר 44₪","time":"10 דק'"}
                            ,'סנסט':
                            {"url":"http://10.0.2.2:5000/upload2/special/סנסט.png","name":"סנסט","description":"סלמון בטמפורה, אבוקדו, מלפפון ועירית בציפוי בטטה.","price":"מחיר 44₪","time":"10 דק'"}
                            ,'קריספי רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/קריספי-רול.png","name":"קריספי רול","description":"ספייסי סלמון/סלמון טמפורה, אבוקדו ובטטה בציפוי סלמון גריל","price":"מחיר 49₪","time":"10 דק'"}
                        }
                        ,'מרקים':
                        {
                            'מרק מיסו':
                            {"url":"http://10.0.2.2:5000/upload2/soup/אדום.png","name":"מרק מיסו","description":"מרק יפני מסורתי עם ציר דאשי, קוביות טופו, אצות וואקמה ובצל ירוק.","price":"מחיר 19₪","time":"10 דק'"}
                            ,'טום יאם ירקות':
                            {"url":"http://10.0.2.2:5000/upload2/soup/ירוק.png","name":"טום יאם ירקות","description":"עם ציר עוף, חלב קוקוס, אטריות שעועית, ירקות וקישוט כוסברה.","price":"מחיר 32₪","time":"10 דק'"}
                            ,'מרק תירס תאילנדי':
                            {"url":"http://10.0.2.2:5000/upload2/soup/צהוב.png","name":"מרק תירס תאילנדי","description":"עם קארי אדום, חלב קוקוס, אטריות אודון ועוף.","price":"מחיר 32₪","time":"10 דק'"}     
                        }            
                        ,'ארוחות ילדים':
                        {
                            'אצבעות עוף':
                            {"url":"http://10.0.2.2:5000/upload2/kids/אצבעות-עוף.png","name":"אצבעות עוף","description":"אצבעות עוף בציפוי פנקו בתוספת אורז מאודה וקטשופ.","price":"מחיר 42₪","time":"10 דק'"}
                            ,'פרש נודלס':
                            {"url":"http://10.0.2.2:5000/upload2/kids/פרש-קידס-נודלס-עוף.png","name":"פרש נודלס","description":"אטריות טריות מוקפצות בטריאקי עם טופו / רצועות עוף","price":"מחיר 42₪","time":"10 דק'"}
                            ,'קריספי ציקן':
                            {"url":"http://10.0.2.2:5000/upload2/kids/קריספי-ציקן-קידס.png","name":"קריספי ציקן","description":"כדורי עוף פריכים בתוספת אורז מאודה וקטשופ.","price":"מחיר 42₪","time":"10 דק'"}
                        }
                        ,'מנות פתיחה':
                        {
                            'אדממה':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/אדממה.png","name":"אדממה","description":"פולי סויה ירוקה עם מלח ים ופלח לימון.","price":"מחיר 19₪","time":"10 דק'"}
                            ,'חמוצים יפניים':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/חמוצים-יפניים.png","name":"חמוצים יפניים","description":"כרוב, גזר, מלפפון, פלפלים וצנון, בקישוט שומשום קלוי.","price":"מחיר 19₪","time":"10 דק'"}
                            ,'קריספי בטטה':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/קריספי-בטטה.png","name":"קריספי בטטה","description":"רצועות בטטה בטמפורה מוגשות עם רוטב טריאקי.","price":"מחיר 26₪","time":"10 דק'"}
                        }
                    }
                    
                ,'רעננה':
                    {
                        'אורז וגריל':
                        {
                            'פאד קפאו בקר':
                            {"url":"http://10.0.2.2:5000/upload2/rice/3פאד-קפאו-בקר.jpg","name":"פאד קפאו בקר","description":"בשר עגל קצוץ בתיבול תאילנדי, פלפלים, בצל, עלי נענע, למון גראס וקפיר ליים.","price":"מחיר 57₪","time":"15 דק'"}
                            ,'דג בקשיו':
                            {"url":"http://10.0.2.2:5000/upload2/rice/דג-בקשיו.jpg","name":"דג בקשיו","description":"רצועות דג בטמפורה מוקפצות ברוטב צ'ילי תמרינדי עם פלפל מתוק מעושן","price":"מחיר 59₪","time":"15 דק'"}
                            ,'חמוץ מתוק':
                            {"url":"http://10.0.2.2:5000/upload2/rice/חמוץ-מתוק.png","name":"חמוץ מתוק","description":"כדורי עוף בטמפורה מוקפצים ברוטב חמוץ מתוק עם פטריות שמפניון, פלפלים.","price":"מחיר 56₪","time":"15 דק'"}
                           }
                        ,'מנות ווק':
                        {                    
                            'צאנג מאי בקר':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-בקר.png","name":"צאנג מאי בקר","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 57₪","time":"15 דק'"}
                            ,'צאנג מאי טופו':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-טופו.png","name":"צאנג מאי טופו","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 52₪","time":"15 דק'"}
                            ,'צאנג מאי ירקות':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-ירקות.png","name":"צאנג מאי ירקות","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 49₪","time":"15 דק'"}
                            ,'צאנג מאי עוף':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-עוף.png","name":"צאנג מאי עוף","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 54₪","time":"15 דק'"}
                        }
                         ,'ספיישל סושי':
                        {
                            'גפנקו':
                            {"url":"http://10.0.2.2:5000/upload2/special/גפנקו.png","name":"גפנקו","description":"I/O בציפוי פנקו, מוגש חם עם רוטב טריאקי","price":"מחיר 39₪","time":"15 דק'"}
                            ,'מנטה רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/מנטה-רול.png","name":"מנטה רול","description":"סלמון נא, אבוקדו, כוסברה, נענע וחסה אייסברג בציפוי סלמון נא ושבבי בטטה.","price":"מחיר 48₪","time":"15 דק'"}
                            ,'סלמון ליים רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/סלמון-ליים-רול.png","name":"סלמון ליים רול","description":"סלמון נא, אבוקדו, שיטאקי ופלחי לימון בציפוי סלמון מעושן, אבוקדו ופלחי לימון.","price":"מחיר 44₪","time":"15 דק'"}
                            ,'סנסט':
                            {"url":"http://10.0.2.2:5000/upload2/special/סנסט.png","name":"סנסט","description":"סלמון בטמפורה, אבוקדו, מלפפון ועירית בציפוי בטטה.","price":"מחיר 44₪","time":"15 דק'"}
                            ,'קריספי רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/קריספי-רול.png","name":"קריספי רול","description":"ספייסי סלמון/סלמון טמפורה, אבוקדו ובטטה בציפוי סלמון גריל","price":"מחיר 49₪","time":"15 דק'"}
                        }
                        ,'מרקים':
                        {
                            'מרק מיסו':
                            {"url":"http://10.0.2.2:5000/upload2/soup/אדום.png","name":"מרק מיסו","description":"מרק יפני מסורתי עם ציר דאשי, קוביות טופו, אצות וואקמה ובצל ירוק.","price":"מחיר 19₪","time":"15 דק'"}
                            ,'טום יאם ירקות':
                            {"url":"http://10.0.2.2:5000/upload2/soup/ירוק.png","name":"טום יאם ירקות","description":"עם ציר עוף, חלב קוקוס, אטריות שעועית, ירקות וקישוט כוסברה.","price":"מחיר 32₪","time":"15 דק'"}
                            ,'מרק תירס תאילנדי':
                            {"url":"http://10.0.2.2:5000/upload2/soup/צהוב.png","name":"מרק תירס תאילנדי","description":"עם קארי אדום, חלב קוקוס, אטריות אודון ועוף.","price":"מחיר 32₪","time":"15 דק'"}     
                        }            
                        ,'ארוחות ילדים':
                        {
                            'אצבעות עוף':
                            {"url":"http://10.0.2.2:5000/upload2/kids/אצבעות-עוף.png","name":"אצבעות עוף","description":"אצבעות עוף בציפוי פנקו בתוספת אורז מאודה וקטשופ.","price":"מחיר 42₪","time":"15 דק'"}
                            ,'פרש נודלס':
                            {"url":"http://10.0.2.2:5000/upload2/kids/פרש-קידס-נודלס-עוף.png","name":"פרש נודלס","description":"אטריות טריות מוקפצות בטריאקי עם טופו / רצועות עוף","price":"מחיר 42₪","time":"15 דק'"}
                            ,'קריספי ציקן':
                            {"url":"http://10.0.2.2:5000/upload2/kids/קריספי-ציקן-קידס.png","name":"קריספי ציקן","description":"כדורי עוף פריכים בתוספת אורז מאודה וקטשופ.","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'מנות פתיחה':
                        {
                            'אדממה':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/אדממה.png","name":"אדממה","description":"פולי סויה ירוקה עם מלח ים ופלח לימון.","price":"מחיר 19₪","time":"15 דק'"}
                            ,'חמוצים יפניים':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/חמוצים-יפניים.png","name":"חמוצים יפניים","description":"כרוב, גזר, מלפפון, פלפלים וצנון, בקישוט שומשום קלוי.","price":"מחיר 19₪","time":"15 דק'"}
                            ,'קריספי בטטה':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/קריספי-בטטה.png","name":"קריספי בטטה","description":"רצועות בטטה בטמפורה מוגשות עם רוטב טריאקי.","price":"מחיר 26₪","time":"15 דק'"}
                        }
                    }
                    
                ,'נתניה':
                    {
                        'אורז וגריל':
                        {
                            'פאד קפאו בקר':
                            {"url":"http://10.0.2.2:5000/upload2/rice/3פאד-קפאו-בקר.jpg","name":"פאד קפאו בקר","description":"בשר עגל קצוץ בתיבול תאילנדי, פלפלים, בצל, עלי נענע, למון גראס וקפיר ליים.","price":"מחיר 57₪","time":"15 דק'"}
                            ,'דג בקשיו':
                            {"url":"http://10.0.2.2:5000/upload2/rice/דג-בקשיו.jpg","name":"דג בקשיו","description":"רצועות דג בטמפורה מוקפצות ברוטב צ'ילי תמרינדי עם פלפל מתוק מעושן","price":"מחיר 59₪","time":"15 דק'"}
                            ,'חמוץ מתוק':
                            {"url":"http://10.0.2.2:5000/upload2/rice/חמוץ-מתוק.png","name":"חמוץ מתוק","description":"כדורי עוף בטמפורה מוקפצים ברוטב חמוץ מתוק עם פטריות שמפניון, פלפלים.","price":"מחיר 56₪","time":"15 דק'"}
                           }
                        ,'מנות ווק':
                        {                    
                            'צאנג מאי בקר':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-בקר.png","name":"צאנג מאי בקר","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 57₪","time":"15 דק'"}
                            ,'צאנג מאי טופו':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-טופו.png","name":"צאנג מאי טופו","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 52₪","time":"15 דק'"}
                            ,'צאנג מאי ירקות':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-ירקות.png","name":"צאנג מאי ירקות","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 49₪","time":"15 דק'"}
                            ,'צאנג מאי עוף':
                            {"url":"http://10.0.2.2:5000/upload2/wok/צאנג-מאי-עוף.png","name":"צאנג מאי עוף","description":"אטריות אודון מוקפצות בקארי אדום וחלב קוקוס עם פטריות שמפניון","price":"מחיר 54₪","time":"15 דק'"}
                        }
                         ,'ספיישל סושי':
                        {
                            'גפנקו':
                            {"url":"http://10.0.2.2:5000/upload2/special/גפנקו.png","name":"גפנקו","description":"I/O בציפוי פנקו, מוגש חם עם רוטב טריאקי","price":"מחיר 39₪","time":"15 דק'"}
                            ,'מנטה רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/מנטה-רול.png","name":"מנטה רול","description":"סלמון נא, אבוקדו, כוסברה, נענע וחסה אייסברג בציפוי סלמון נא ושבבי בטטה.","price":"מחיר 48₪","time":"15 דק'"}
                            ,'סלמון ליים רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/סלמון-ליים-רול.png","name":"סלמון ליים רול","description":"סלמון נא, אבוקדו, שיטאקי ופלחי לימון בציפוי סלמון מעושן, אבוקדו ופלחי לימון.","price":"מחיר 44₪","time":"15 דק'"}
                            ,'סנסט':
                            {"url":"http://10.0.2.2:5000/upload2/special/סנסט.png","name":"סנסט","description":"סלמון בטמפורה, אבוקדו, מלפפון ועירית בציפוי בטטה.","price":"מחיר 44₪","time":"15 דק'"}
                            ,'קריספי רול':
                            {"url":"http://10.0.2.2:5000/upload2/special/קריספי-רול.png","name":"קריספי רול","description":"ספייסי סלמון/סלמון טמפורה, אבוקדו ובטטה בציפוי סלמון גריל","price":"מחיר 49₪","time":"15 דק'"}
                        }
                        ,'מרקים':
                        {
                            'מרק מיסו':
                            {"url":"http://10.0.2.2:5000/upload2/soup/אדום.png","name":"מרק מיסו","description":"מרק יפני מסורתי עם ציר דאשי, קוביות טופו, אצות וואקמה ובצל ירוק.","price":"מחיר 19₪","time":"15 דק'"}
                            ,'טום יאם ירקות':
                            {"url":"http://10.0.2.2:5000/upload2/soup/ירוק.png","name":"טום יאם ירקות","description":"עם ציר עוף, חלב קוקוס, אטריות שעועית, ירקות וקישוט כוסברה.","price":"מחיר 32₪","time":"15 דק'"}
                            ,'מרק תירס תאילנדי':
                            {"url":"http://10.0.2.2:5000/upload2/soup/צהוב.png","name":"מרק תירס תאילנדי","description":"עם קארי אדום, חלב קוקוס, אטריות אודון ועוף.","price":"מחיר 32₪","time":"15 דק'"}     
                        }            
                        ,'ארוחות ילדים':
                        {
                            'אצבעות עוף':
                            {"url":"http://10.0.2.2:5000/upload2/kids/אצבעות-עוף.png","name":"אצבעות עוף","description":"אצבעות עוף בציפוי פנקו בתוספת אורז מאודה וקטשופ.","price":"מחיר 42₪","time":"15 דק'"}
                            ,'פרש נודלס':
                            {"url":"http://10.0.2.2:5000/upload2/kids/פרש-קידס-נודלס-עוף.png","name":"פרש נודלס","description":"אטריות טריות מוקפצות בטריאקי עם טופו / רצועות עוף","price":"מחיר 42₪","time":"15 דק'"}
                            ,'קריספי ציקן':
                            {"url":"http://10.0.2.2:5000/upload2/kids/קריספי-ציקן-קידס.png","name":"קריספי ציקן","description":"כדורי עוף פריכים בתוספת אורז מאודה וקטשופ.","price":"מחיר 42₪","time":"15 דק'"}
                        }
                        ,'מנות פתיחה':
                        {
                            'אדממה':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/אדממה.png","name":"אדממה","description":"פולי סויה ירוקה עם מלח ים ופלח לימון.","price":"מחיר 19₪","time":"15 דק'"}
                            ,'חמוצים יפניים':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/חמוצים-יפניים.png","name":"חמוצים יפניים","description":"כרוב, גזר, מלפפון, פלפלים וצנון, בקישוט שומשום קלוי.","price":"מחיר 19₪","time":"15 דק'"}
                            ,'קריספי בטטה':
                            {"url":"http://10.0.2.2:5000/upload2/appetizier/קריספי-בטטה.png","name":"קריספי בטטה","description":"רצועות בטטה בטמפורה מוגשות עם רוטב טריאקי.","price":"מחיר 26₪","time":"15 דק'"}
                        }
                    }
            }
    })