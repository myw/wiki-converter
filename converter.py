"""
    Wiki Converter
    ~~~~~~

    Simple wrapper of pandoc for conversion from MediaWiki to Markdown.

    :copyright: (c) 2015 by Mikhail Wolfson
    :license: ISC, see LICENSE for more details.
"""

from flask import Flask, render_template, request
import pypandoc


app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
  input_markup = request.form['input_markup']
  output_markup = pypandoc.convert(input_markup, format='mediawiki', to='markdown_github')
  return render_template('index.html',
                         input_markup=input_markup,
                         output_markup=output_markup)


if __name__ == '__main__':
    app.run(debug=True)
