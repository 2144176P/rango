import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
          "url":"http://docs.python.org/2/tutorial/",
         "views":85856},
        {"title":"How to Think like a Computer Scientist",
          "url":"http://www.greenteapress.com/thinkpython/",
         "views":11101},
        {"title":"Learn Python in 10 Minutes",
          "url":"http://www.korokithakis.net/tutorials/python/",
         "views":1010}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
            "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views":65555},
        {"title": "Django Rocks",
            "url":"http://www.djangorocks.com/",
         "views":8168},
        {"title": "How to Tango with Django",
            "url":"http://www.tangowithdjango.com/",
         "views":1}
    ]

    other_pages = [
        {"title": "Bottle",
            "url":"http://bottlepy.org/docs/dev/",
         "views":807713},
        {"title": "Flask",
            "url":"http://flask.pocoo.org",
         "views":127001}
    ]

    categories = {
        "Python": {"Pages": python_pages, "Views":128},
        "Django": {"Pages": django_pages, "Views":64},
        "Other Frameworks": {"Pages": other_pages, "Views":32}
    }

    for category, category_data in categories.items():
        cat = add_category(category, category_data["Views"])
        for page in category_data["Pages"]:
            add_page(cat,page["title"], page["url"], page["views"])

    for cat in Category.objects.all():
        for page in Page.objects.filter(category=cat):
            print("- {0} - {1}".format(str(cat), str(page)))


def add_page(category, title, url, views):
    page = Page.objects.get_or_create(category=category, title=title)[0]
    page.url=url
    page.views=views
    page.save()
    return page

def add_category(name, views):
    category = Category.objects.get_or_create(name=name)[0]
    category.views= views
    category.likes=views/2
    category.save()
    return category

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()