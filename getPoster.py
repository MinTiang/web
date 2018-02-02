import web
from urllib import request

def get_poster(id,url):
    pic=request.urlopen(url).read()

    file_name='static/poster/%d.jpg'%id
    f=open(file=file_name,mode='wb')
    f.write(pic)
db=web.database(dbn='sqlite',db='MovieSite.db')

movies=db.select('movie')
count=0
for movie in movies:
    print(movie.image)
    get_poster(movie.id,movie.image)
    count+=1
