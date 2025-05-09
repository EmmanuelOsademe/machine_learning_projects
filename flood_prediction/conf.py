# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Project Deluge- Predicting Flood Risk'
copyright = '2024, Miles Weberman, Julia Metz, David Mamane, Precious Okon, Yixuan Yan, Haoran Sun, Pengjie Wang, Yiyu Yang'
author = 'Miles Weberman, Julia Metz, David Mamane, Precious Okon, Yixuan Yan, Haoran Sun, Pengjie Wang, Yiyu Yang'
release = 'November 2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
