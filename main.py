from appconfig import app
from apps.authentication import views as authviews
from apps.crud import views as crudviews
from apps import routes
from environ import SECRET_KEY

app.secret_key = SECRET_KEY



app.register_blueprint(authviews.authprint)
app.register_blueprint(crudviews.crudprints)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=3000, debug=True)
