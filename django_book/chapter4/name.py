# third party imports
from django.template import Context, Template
from django.utils.safestring import SafeString
import os


def greet(name: str) -> SafeString:
    t = Template("My name is {{ name }}")
    c = Context(dict(name=name))
    return t.render(c)


def person_info(person: dict) -> SafeString:
    # access dict keys with ".", e.g. person.age
    # we can invoke methods of an object that take no arguments with "." and omitting the parenthesis, e.g. name.upper
    name = person.get("name")
    t = Template('{{ name.upper }} is {{ person.age }} years old.')  #
    c = Context({"name": name, 'person': person})
    return t.render(c)


def pick_second_item(a_list: list) -> SafeString:
    t = Template("{{ list.1 }}")  # a list item can be picked with "." by passing one index
    c = Context({"list": a_list})
    return t.render(c)


# must be executed with "python manage.py shell" because the settings need to be loaded
if __name__ == "__main__":
    print(greet("Jose"))
    print(person_info(dict(name="Joe", age=42)))
    print(pick_second_item(["zero", "one", "two"]))
