from flask import redirect, render_template

from . import app
from .constants import MAIN_PAGE_TEMPLATE
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        return URLMap.add_urlmap(form.original_link.data, short, False, form)
    return render_template(MAIN_PAGE_TEMPLATE, form=form)


@app.route('/<string:short_id>')
def opinion_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url.original)
