# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import os
import sphinx
import datetime

project = 'Design of Embedded Systems with RaspberryPI'
copyright = 'Universidad Politécnica de Madrid'
author = 'Mariano Ruiz'
release = '1.0'
version = '1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_simplepdf','sphinx_rtd_theme','myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    'docs_scope': 'external',
    'cover_logo_title': '',
    'cover_meta_data': 'Design of Embedded Systems with RaspberryPI.',
    'cover_footer': f'Build: {datetime.datetime.now().strftime("%d.%m.%Y")}<br>'
                    f'Author: Mariano Ruiz',
}
simplepdf_vars = {
#    'primary': '#a023fa',
#    'secondary': '#379683',
#    'cover': '#ffffff',
#    'white': '#ffffff',
#    'links': 'FA2323',
#    'cover-bg': 'url(cover-bg.jpg) no-repeat center',
#    'cover-overlay': 'rgba(250, 35, 35, 0.5)',
    'top-left-content': 'counter(page)',
    'bottom-center-content': 'string(heading)',
}

numfig = True
simplepdf_file_name = "EmbeddedLinuxRPI.pdf"

numfig_format = {
    'code-block': 'Listing %s',
    'figure': 'Fig. %s',
    'section': 'Section',
    'table': 'Table %s',
}
