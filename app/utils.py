import markdown
import re


def get_item(ancestor, selector, attribute=None, return_list=False):
    try:
        if return_list:
            return [item.get_text().strip() for item in ancestor.select(selector)]
        if attribute:
            return ancestor.select_one(selector)[attribute]
        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError, TypeError):
        return None

def mdtohtml():
    with open('README.md','r') as file:
        content = file.read()
    template = markdown.markdown(content, extensions=['tables'])
    return re.sub('<table>','<table class="table table-bordered">', template)
##szukałem ale nie wiem jak na stronie pokazać polskie znaki