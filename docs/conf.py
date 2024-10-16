# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Example'
copyright = 'workshop participant'
author = 'Mariano Ruz'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_pdf_generate']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Sphinx-PDF-Generate global options
pdfgen_site_url = "https://example.com"
pdfgen_author = "Sphinx-PDF Generate"
pdfgen_copyright = "2023, Sphinx-PDF Generate"
pdfgen_disclaimer = "Disclaimer: Content can change at anytime and best to refer to website for latest information."
pdfgen_cover = True
pdfgen_cover_title = "Sphinx-PDF Generate"
pdfgen_toc = True
pdfgen_toc_numbering = True
pdfgen_toc_title = "Table of Contents"
pdfgen_toc_level = 4
