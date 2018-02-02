#coding:utf-8
import web
from urllib import parse
from urllib import request

urls=('/','index','/movie/(\d+)','movie','/cast/(.*)','cast')
db=web.database(dbn='sqlite',db='MovieSite.db')

render=web.template.render('templates/')

class index:

    def GET(self):
        movies=db.select('movie')
        count = db.query('select count(1) as count from movie')[0]['count']
        return render.index(movies,count,None)

    def POST(self):
        data=web.input()
        condition=r'title like "%'+data.title+r'%"'
        movies=db.select('movie',where=condition)
        count=db.query('select count(1) as count from movie where '+condition)[0]['count']
        return render.index(movies,count,data.title)
class movie:
    def GET(self,movie_id):
        movie_id=int(movie_id)
        movie=db.select('movie',where='id=$movie_id',vars=locals())[0]
        return  render.movie(movie,parse)

class cast:
    def GET(self,cast_name):
        cast_name=parse.unquote(str(cast_name).replace("@","%"))
        condition=r'casts like "%'+cast_name+'%"'
        movies=db.select('movie',where=condition)
        count = db.query('select count(1) as count from movie where ' + condition)[0]['count']
        return render.index(movies,count,cast_name)

if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()