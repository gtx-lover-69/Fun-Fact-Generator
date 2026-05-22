import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    clear()

    put_html(
        '<p align="center">'
        '<h2><img src="https://i.redd.it/funniest-cat-pictures-you-have-v0-cvk0vuc0hj5a1.jpg?width=3000&format=pjpg&auto=webp&s=73c395c63462f04c52e1550559dfb9809dd2a599" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.get(url)
    data = json.loads(response.text)

    useless_facts = data['text']
    style(put_text(useless_facts), 'color:blue; font-size:30px')

    put_buttons(
        [dict(label='Click me!', value='outline-success',
        color='outline-success')],
        onclick=get_fun_fact
    )

if __name__ == '__main__':
    put_html(
        '<p align="center">'
        '<h2><img src="https://i.redd.it/funniest-cat-pictures-you-have-v0-cvk0vuc0hj5a1.jpg?width=3000&format=pjpg&auto=webp&s=73c395c63462f04c52e1550559dfb9809dd2a599" width="7%"> Fun Fact Generator</h2>'
        '</p>'
        )

    put_buttons(
        [dict(label='Click me!', value='outline-success',color='outline-success')],
        onclick=get_fun_fact
    )
    hold()