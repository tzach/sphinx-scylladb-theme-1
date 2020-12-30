# -*- coding: utf-8 -*-
import os
import sys
from datetime import date
from sphinx.util import logging
import recommonmark
from recommonmark.transform import AutoStructify
from sphinx_scylladb_theme.extensions.utils import multiversion_regex_builder

logger = logging.getLogger(__name__)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
    'sphinx_scylladb_theme',
    'sphinx_multiversion',
    'recommonmark'
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
autosectionlabel_prefix_document = True

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Scylla Documentation Theme and Extensions'
copyright = str(date.today().year) + ', ScyllaDB. All rights reserved.'
author = u'Scylla Project Contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.3'
# The full version, including alpha/beta/rc tags.
release = u'1.3.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'lib', 'lib64','**/_common/*', 'README.md', '.git', '.github', '_utils', '_templates', 'rst_include']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Setup Sphinx
def setup(sphinx):
    sphinx.add_config_value('recommonmark_config', {
        'enable_eval_rst': True,
        'enable_auto_toc_tree': False,
    }, True)
    sphinx.add_transform(AutoStructify)

# Adds version variables for monitoring and manager versions when used in inline text
rst_prolog = """
.. |mon_version| replace:: 3.1
.. |man_version| replace:: 2.0
.. |mon_root| replace::  :doc:`Scylla Monitoring Stack </operating-scylla/monitoring/index>`
""" 

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_scylladb_theme'
html_theme_path = ["../.."]
html_style = ''

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'header_links': [
    ('Scylla Cloud', 'https://docs.scylladb.com/scylla-cloud/'),
    ('Scylla University', 'https://university.scylladb.com/'),
    ('ScyllaDB Home', 'https://www.scylladb.com/')],
    'github_issues_repository': 'scylladb/sphinx-scylladb-theme',
}

extlinks = {
    'manager': ('/operating-scylla/manager/%s/',''),
    'manager_lst': ('/operating-scylla/manager/2.0/%s/',''),
    'monitor': ('/operating-scylla/monitoring/%s/',''),
    'monitor_lst': ('/operating-scylla/monitoring/3.1/%s/','')
}

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = '%d %B %Y'

# Custom sidebar templates, maps document names to template names.
#
html_sidebars = {'**': ['side-nav.html']}

# Output file base name for HTML help builder.
htmlhelp_basename = 'ScyllaDocumentationdoc'

# URL which points to the root of the HTML documentation. 
html_baseurl = 'https://sphinx-theme.scylladb.com'

# Dictionary of values to pass into the template engine’s context for all pages
html_context = {'html_baseurl': html_baseurl}

# -- Options for not found extension -------------------------------------------

# Template used to render the 404.html generated by this extension.
notfound_template =  '404.html'

# Prefix added to all the URLs generated in the 404 page.
notfound_urls_prefix = ''

# -- Options for redirect extension ---------------------------------------

# Read a YAML dictionary of redirections and generate an HTML file for each
redirects_file = "_utils/redirections.yaml"

# -- Options for multiversion extension ----------------------------------

# Whitelist pattern for tags (set to None to ignore all tags)
TAGS = ['stable', '0.1.8']
smv_tag_whitelist = multiversion_regex_builder(TAGS)
# Whitelist pattern for branches (set to None to ignore all branches)
BRANCHES = ['master']
smv_branch_whitelist = multiversion_regex_builder(BRANCHES)
# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r"^origin$"
# Pattern for released versions
smv_released_pattern = r'^tags/.*$'
# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# -- Options for LaTeX page output ---------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ScyllaDocumentation.tex', u'Scylla Documentation Documentation',
     u'Scylla Project Contributors', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'scylladocumentation', u'Scylla Documentation Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ScyllaDocumentation', u'Scylla Documentation Documentation',
     author, 'ScyllaDocumentation', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
