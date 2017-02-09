import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
          "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
          "url":"http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
            "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks",
            "url":"http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
            "url":"http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title": "Bottle",
            "url":"http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
            "url":"http://flask.pocoo.org"}
    ]

    categories = {
        "Python": {"Pages": python_pages},
        "Django": {"Pages": django_pages},
        "Other": {"Pages": other_pages}
    }

    for category, category_data in categories.items():
        cat = add_category(category)
            for page in category_data["Pages"]:
                add_page(cat,page["title"], page["url"])

    for cat in Category.objects.all():
        for page in Page.objects.filter(category=cat):
            print("- {0} - {1}".format(str(cat), str(page)))

def add_page(category, title, url, views=0):
    page = Page.objects.get_or_create(category=category, title=title)[0]
    page.url=url
    page.views=views
    page.save()
    return page

def add_cat(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.save()
    return category

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()