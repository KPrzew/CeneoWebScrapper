import markdown

def tohtml():
    with open('README.md','r') as file:
        content = file.read()

    template = markdown.markdown(content, extensions=['tables'])
    return template
##szukałem ale nie wiem jak na stronie pokazać polskie znaki