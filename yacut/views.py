from urllib.parse import urljoin

from flask import flash, redirect, render_template, url_for

from . import app
from .constants import MAIN_PAGE_TEMPLATE
from .error_handlers import MakingUrlException
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        try:
            url = URLMap.add_urlmap(form.original_link.data, short, False)
            base_url = url_for('index_view', _external=True)
            new_url = urljoin(base_url, url.short)
            return render_template(MAIN_PAGE_TEMPLATE, form=form,
                                   new_url=new_url)
        except MakingUrlException as error:
            flash(error)
            return render_template(MAIN_PAGE_TEMPLATE, form=form)
    return render_template(MAIN_PAGE_TEMPLATE, form=form)


@app.route('/<string:short_id>')
def opinion_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url.original)
