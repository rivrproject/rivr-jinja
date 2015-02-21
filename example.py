from jinja2 import Environment, DictLoader

import rivr
from rivr_jinja import *


class View(JinjaView):
    template_name = 'index.html'

    def get_context_data(self):
        return {
            'name': 'World'
        }


if __name__ == '__main__':
    loader = DictLoader({'index.html': 'Hello {{ name }}'})
    environment = Environment(loader=loader)

    rivr.serve(JinjaMiddleware.wrap(View.as_view(), environment))

