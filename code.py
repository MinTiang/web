#coding:utf-8
import web


urls=('/','index','/movie/(\d+)','movie')
db=web.database(dbn='sqlite',db='MovieSite.db')
# movies=[{'title':'Forrest Gump','year':1994},{'title':'Titanic','year':1997}]

render=web.template.render('templates/')

class index:

    def GET(self):
        movies=db.select('movie')
        return render.index(movies)
class movie:
    def GET(self,movie_id):
        movie_id=int(movie_id)
        movie=db.select('movie',where='id=$movie_id',vars=locals())[0]
        return  render.movie(movie)
if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()