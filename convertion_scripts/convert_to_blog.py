import os
import re
import subprocess
from sys import argv as args

from bs4 import BeautifulSoup


def get_as_html(fname):
    curr_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
    elyxer_path = os.path.join(curr_dir, 'elyxer.py')
    html_str = subprocess.check_output(['python', elyxer_path, '--nofooter', '--mathjax', 'remote', '--html', fname])
    return BeautifulSoup(html_str, 'html.parser')


USAGE = 'python covert_to_blog.py <path to lyx file>'
HEADER_TEMPLATE = '''---
layout: post
author: {author}
title:  {title}
date:   {date}
comments: true
---

'''


def gen_ourput_fname(meta_data):
    title = meta_data['title'].replace(' ', '-')
    return '%s-%s.markdown' % (meta_data['date'], title)


def save(content, fname):
    with open(fname, 'w') as f:
        f.write(content)
    print 'saved successfully to %s' % os.path.abspath(fname)


def _get_text_from_tag(html_tree, *args):
    return html_tree.find_all(*args)[0].extract().text.strip()


def get_content_and_metadata(html_tree, fname):
    title = _get_text_from_tag(html_tree, 'h1', 'title')
    author = _get_text_from_tag(html_tree, 'h2', 'author')
    date = re.match(r'\d{4}-\d{2}-\d{2}', os.path.basename(fname)).group()

    content_div = html_tree.find_all(id='globalWrapper')[0]
    content_html = ''.join([str(s) for s in content_div.contents])
    return content_html, {
        'author': author,
        'title': title,
        'date': date
    }


def run():
    if 'python' in args[0]:
        args.pop(0)
    if len(args) != 2:
        print USAGE
        return

    input_fname = args[1]
    html_tree = get_as_html(input_fname)
    content_str, meta_data = get_content_and_metadata(html_tree, input_fname)

    header_str = HEADER_TEMPLATE.format(**meta_data)
    output_fname = gen_ourput_fname(meta_data)
    save(header_str + content_str, output_fname)


if __name__ == '__main__':
    run()
