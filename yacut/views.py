from urllib.parse import urljoin

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if URLMap.query.filter_by(short=short).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)
        if not short:
            short = get_unique_short_id()
        url = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url)
        db.session.commit()
        base_url = url_for('index_view', _external=True)
        new_url = urljoin(base_url, url.short)
        return render_template('index.html', form=form, new_url=new_url)
    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def opinion_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url:
        return redirect(url.original)
    abort(404)
