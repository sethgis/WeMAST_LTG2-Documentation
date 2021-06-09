# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sys, os

sys.path.insert(0, os.path.abspath('extensions'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.ifconfig',
              'epub2', 'mobi', 'autoimage', 'code_example', 'sphinx_rtd_theme']

todo_include_todos = True
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []
add_function_parentheses = True
project = 'WETLAND MONITORING AND ASSESSMENT SERVICE (WeMAST)'
copyright = '2021, LocateIT Limited'
author = 'LocateIT Limited'
logo = 'D:\newfile\source\_static\logo.PNG'
# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx_rtd_theme',
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_themes']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []





# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

import sphinx_rtd_theme

extensions = [
    'sphinx_rtd_theme',
]

html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]
html_theme = 'basic'
html_theme_options = html_theme_options = {
    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_button_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'light blue',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}





# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = logo

html_context = {
"display_github": True, # Add 'Edit on Github' link instead of 'View page source'
"last_updated": True,
"commit": False,
}



latex_elements = {
# The paper size ( 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '11pt',

# Additional stuff for the LaTeX preamble.
#'preamble':'',

#Figure placement within LaTeX paper NOT WORKING
'figure_align': 'H',

}


latex_documents = [
  
]

latex_elements = {
     'papersize': '',
     'fontpkg': '',
     'fncychap': '',
     'maketitle': '\\cover',
     'pointsize': '',
     'preamble': '',
     'releasename': "",
     'babel': '',
     'printindex': '',
     'fontenc': '',
     'inputenc': '',
     'classoptions': '',
     'utf8extra': '',
     
}

latex_additional_files = ["mfgan-bw.sty", "mfgan.sty", "_static/cover.png"]

latex_show_pagerefs = True
latex_domain_indices = True
latex_use_modindex = True


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css',
                  'https://example.com/css/custom.css',
                  ('print.css', {'media': 'print'})]




autosummary_generate = True
