from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
#from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import default_url_fetcher, HTML, CSS
import logging
from base64 import b64encode
# import cairosvg
from xml import etree  # refer to xml.etree.ElementTree documentions

logger = logging.getLogger('weasyprint')

def my_fetcher(url): # external urls
    if url.startswith('assets://'):
        pass
        #url = url[len('assets://'):]
        #url = "file://" + safe_join(settings.ASSETS_ROOT, url) # example : file:///C:/Users/a/Projects/my-projects/cv_builder/static/img/eisa-91.jpg
    return default_url_fetcher(url)


#def svg_embed(html):
#    """For the child of nvd3 nodes (svg) munge them into b64encoded data
#    as a workaround for https://github.com/Kozea/WeasyPrint/issues/75"""
#    root = html.root_element
#    svgs = root.findall('.//nvd3')
#    for svg in svgs:
#        child = svg.getchildren()[0]
#        encoded = b64encode(etree.tostring(child)).decode()
#        encoded_data = "data:image/svg+xml;charset=utf-8;base64," + encoded
#        encoded_child = etree.fromstring('<img src="%s"/>' % encoded_data)
#        svg.replace(child, encoded_child)
#    return html
# and after use as svg_embed(HTML(string=html, base_url=base_url)).write_pdf..


def home_page_view(request):
    # cairosvg.svg2png(url="/code/static/assets/mail.svg", write_to="/code/static/img/output.png")   # convert svg to png
    return render(request, './builder/home.html')


def download(request):
    print('downloading..')
    logger.addHandler(logging.FileHandler('/code/logs/weasyprint.log'))
    html = render_to_string('builder/cv.html')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=Eisa-Nahardani.pdf'
    HTML(string=html, base_url=request.build_absolute_uri(), url_fetcher=my_fetcher ).write_pdf(response)
    return response
