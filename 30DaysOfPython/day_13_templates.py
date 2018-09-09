import os


def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.join(os.getcwd(), path):
        raise Exception("This is not a valid path")
    return file_path


def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()


def render_content(template_string, context):
    return template_string.format(**context)


file_ = "/Users/jsalinas/Documents/Developer/learning_python/30DaysOfPython/templates/email_message.txt"
file_html = "/Users/jsalinas/Documents/Developer/learning_python/30DaysOfPython/templates/email_message.html"
template = get_template(file_)
template_html = get_template(file_html)
context = {
    "name": "Justin",
    "date": None,
    "total": None
}

print(render_content(template, context))
print(render_content(template_html, context))
