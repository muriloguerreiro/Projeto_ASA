from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app, db, lm
from app.models.tables import User, Perfil
from app.models.forms import LoginForm, AlunoForm, PerfilForm


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Olá " + user.name + ", login realizado com sucesso!")
            if (user.password == 'coordenacao2019'):
                return redirect(url_for("coordenacao"))
            else:
                return redirect(url_for("aluno"))
        else:
            flash("Algum campo é inválido!")
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Você foi desconectado!")
    return redirect(url_for("index"))


@app.route("/coordenacao")
def coordenacao():
    return render_template('coordenacao.html')

@app.route("/aluno")
def aluno():
    return render_template('aluno.html')

@app.route("/coordenacao/listagem", methods=['GET', 'POST'])
def listagem():
    data = {}
    data['users'] = User.query.all()
    return render_template('listagem.html', data=data)


@app.route("/create/<info>")
@app.route("/create", defaults={"info": None})
def create(info):
    i = User("coordenador10", "coordenacao2019", "Coordenador10", "coordenacao10@gmail.com")
    db.session.add(i)
    db.session.commit()
    return "OK"


@app.route("/read/<info>")
@app.route("/read", defaults={"info": None})
def read(info):
    r = Perfil.query.filter_by(id=15).first()
    print(r.curso)
    return "OK"


@app.route("/update/<info>")
@app.route("/update", defaults={"info": None})
def update(info):
    r = User.query.filter_by(username="teste46").first()
    r.name = "testedeucerto"
    db.session.add(r)
    db.session.commit()
    return "OK"


@app.route("/delete/<info>")
@app.route("/delete", defaults={"info": None})
def delete(info):
    r = User.query.filter_by(username="teste46").first()
    r.name = "testedeucerto"
    db.session.delete(r)
    db.session.commit()
    return "OK"


@app.route("/coordenacao/cadaluno/", methods=['GET', 'POST'])
def cadaluno():
    form = AlunoForm()
    i = User(form.username.data, form.password.data, form.name.data, form.email.data)
    if form.validate_on_submit():
        db.session.add(i)
        db.session.commit()
        flash('Usuário Cadastrado')
    return render_template('cadaluno.html', form=form)


@app.route("/coordenacao/cadperfil/", methods=['GET', 'POST'])
def cadperfil():
    form = PerfilForm()
    i = Perfil(form.user_id.data, form.curso.data, form.periodo.data, form.disc_1.data, form.nota_d1.data, form.disc_2.data, form.nota_d2.data,
                                                    form.disc_3.data, form.nota_d3.data, form.disc_4.data, form.nota_d4.data)
    if form.validate_on_submit():
        db.session.add(i)
        db.session.commit()
        flash('Perfil Cadastrado')
    return render_template('cadperfil.html', form=form)
