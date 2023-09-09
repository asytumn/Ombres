# -*- coding: utf-8 -*-
#
# The Linux Kernel documentation build configuration file, created by
# sphinx-quickstart on Fri Feb 12 13:51:46 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import sphinx

from subprocess import check_output

# Get Sphinx version
major, minor, patch = sphinx.version_info[:3]


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('sphinx'))
from load_config import loadConfig

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['kerneldoc', 'rstFlatTable', 'kernel_include',
              'kfigure', 'sphinx.ext.ifconfig', 'automarkup',
              'maintainers_include', 'sphinx.ext.autosectionlabel',
              'kernel_abi']

#
# cdomain is badly broken in Sphinx 3+.  Leaving it out generates *most*
# of the docs correctly, but not all.  Scream bloody murder but allow
# the process to proceed; hopefully somebody will fix this properly soon.
#
if major >= 3:
    sys.stderr.write('''WARNING: The kernel documentation build process
        support for Sphinx v3.0 and above is brand new. Be prepared for
        possible issues in the generated output.
        ''')
    if (major > 3) or (minor > 0 or patch >= 2):
        # Sphinx c function parser is more pedantic with regards to type
        # checking. Due to that, having macros at c:function cause problems.
        # Those needed to be scaped by using c_id_attributes[] array
        c_id_attributes = [
            # GCC Compiler types not parsed by Sphinx:
            "__restrict__",

            # include/linux/compiler_types.h:
            "__iomem",
            "__kernel",
            "noinstr",
            "notrace",
            "__percpu",
            "__rcu",
            "__user",

            # include/linux/compiler_attributes.h:
            "__alias",
            "__aligned",
            "__aligned_largest",
            "__always_inline",
            "__assume_aligned",
            "__cold",
            "__attribute_const__",
            "__copy",
            "__pure",
            "__designated_init",
            "__visible",
            "__printf",
            "__scanf",
            "__gnu_inline",
            "__malloc",
            "__mode",
            "__no_caller_saved_registers",
            "__noclone",
            "__nonstring",
            "__noreturn",
            "__packed",
            "__pure",
            "__section",
            "__always_unused",
            "__maybe_unused",
            "__used",
            "__weak",
            "noinline",

            # include/linux/memblock.h:
            "__init_memblock",
            "__meminit",

            # include/linux/init.h:
            "__init",
            "__ref",

            # include/linux/linkage.h:
            "asmlinkage",
        ]

else:
    extensions.append('cdomain')

# Ensure that autosectionlabel will produce unique names
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# The name of the math extension changed on Sphinx 1.4
if (major == 1 and minor > 3) or (major > 1):
    extensions.append("sphinx.ext.imgmath")
else:
    extensions.append("sphinx.ext.pngmath")

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'The Linux Kernel'
copyright = 'The kernel development community'
author = 'The kernel development community'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# In a normal build, version and release are are set to KERNELVERSION and
# KERNELRELEASE, respectively, from the Makefile via Sphinx command line
# arguments.
#
# The following code tries to extract the information by reading the Makefile,
# when Sphinx is run directly (e.g. by Read the Docs).
try:
    makefile_version = None
    makefile_patchlevel = None
    for line in open('../Makefile'):
        key, val = [x.strip() for x in line.split('=', 2)]
        if key == 'VERSION':
            makefile_version = val
        elif key == 'PATCHLEVEL':
            makefile_patchlevel = val
        if makefile_version and makefile_patchlevel:
            break
except:
    pass
finally:
    if makefile_version and makefile_patchlevel:
        version = release = makefile_version + '.' + makefile_patchlevel
    else:
        version = release = "unknown version"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['output']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

primary_domain = 'c'
highlight_language = 'none'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# The Read the Docs theme is available from
# - https://github.com/snide/sphinx_rtd_theme
# - https://pypi.python.org/pypi/sphinx_rtd_theme
# - python-sphinx-rtd-theme package (on Debian)
try:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
except ImportError:
    sys.stderr.write('Warning: The Sphinx \'sphinx_rtd_theme\' HTML theme was not found. Make sure you have the theme installed to produce pretty HTML output. Falling back to the default theme.\n')

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['sphinx-static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',
    ],
}

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'TheLinuxKerneldoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '11pt',

# Latex figure (float) alignment
#'figure_align': 'htbp',

# Don't mangle with UTF-8 chars
'inputenc': '',
'utf8extra': '',

# Additional stuff for the LaTeX preamble.
    'preamble': '''
	% Use some font with UTF-8 support with XeLaTeX
        \\usepackage{fontspec}
        \\setsansfont{DejaVu Sans}
        \\setromanfont{DejaVu Serif}
        \\setmonofont{DejaVu Sans Mono}
     '''
}

# At least one book (translations) may have Asian characters
# with are only displayed if xeCJK is used

cjk_cmd = check_output(['fc-list', '--format="%{family[0]}\n"']).decode('utf-8', 'ignore')
if cjk_cmd.find("Noto Sans CJK SC") >= 0:
    print ("enabling CJK for LaTeX builder")
    latex_elements['preamble']  += '''
	% This is needed for translations
        \\usepackage{xeCJK}
        \\setCJKmainfont{Noto Sans CJK SC}
     '''

# Fix reference escape troubles with Sphinx 1.4.x
if major == 1 and minor > 3:
    latex_elements['preamble']  += '\\renewcommand*{\\DUrole}[2]{ #2 }\n'

if major == 1 and minor <= 4:
    latex_elements['preamble']  += '\\usepackage[margin=0.5in, top=1in, bottom=1in]{geometry}'
elif major == 1 and (minor > 5 or (minor == 5 and patch >= 3)):
    latex_elements['sphinxsetup'] = 'hmargin=0.5in, vmargin=1in'
    latex_elements['preamble']  += '\\fvset{fontsize=auto}\n'

# Customize notice background colors on Sphinx < 1.6:
if major == 1 and minor < 6:
   latex_elements['preamble']  += '''
        \\usepackage{ifthen}

        % Put notes in color and let them be inside a table
	\\definecolor{NoteColor}{RGB}{204,255,255}
	\\definecolor{WarningColor}{RGB}{255,204,204}
	\\definecolor{AttentionColor}{RGB}{255,255,204}
	\\definecolor{ImportantColor}{RGB}{192,255,204}
	\\definecolor{OtherColor}{RGB}{204,204,204}
        \\newlength{\\mynoticelength}
        \\makeatletter\\newenvironment{coloredbox}[1]{%
	   \\setlength{\\fboxrule}{1pt}
	   \\setlength{\\fboxsep}{7pt}
	   \\setlength{\\mynoticelength}{\\linewidth}
	   \\addtolength{\\mynoticelength}{-2\\fboxsep}
	   \\addtolength{\\mynoticelength}{-2\\fboxrule}
           \\begin{lrbox}{\\@tempboxa}\\begin{minipage}{\\mynoticelength}}{\\end{minipage}\\end{lrbox}%
	   \\ifthenelse%
	      {\\equal{\\py@noticetype}{note}}%
	      {\\colorbox{NoteColor}{\\usebox{\\@tempboxa}}}%
	      {%
	         \\ifthenelse%
	         {\\equal{\\py@noticetype}{warning}}%
	         {\\colorbox{WarningColor}{\\usebox{\\@tempboxa}}}%
		 {%
	            \\ifthenelse%
	            {\\equal{\\py@noticetype}{attention}}%
	            {\\colorbox{AttentionColor}{\\usebox{\\@tempboxa}}}%
		    {%
	               \\ifthenelse%
	               {\\equal{\\py@noticetype}{important}}%
	               {\\colorbox{ImportantColor}{\\usebox{\\@tempboxa}}}%
	               {\\colorbox{OtherColor}{\\usebox{\\@tempboxa}}}%
		    }%
		 }%
	      }%
        }\\makeatother

        \\makeatletter
        \\renewenvironment{notice}[2]{%
          \\def\\py@noticetype{#1}
          \\begin{coloredbox}{#1}
          \\bf\\it
          \\par\\strong{#2}
          \\csname py@noticestart@#1\\endcsname
        }
	{
          \\csname py@noticeend@\\py@noticetype\\endcsname
          \\end{coloredbox}
        }
	\\makeatother

     '''

# With Sphinx 1.6, it is possible to change the Bg color directly
# by using:
#	\definecolor{sphinxnoteBgColor}{RGB}{204,255,255}
#	\definecolor{sphinxwarningBgColor}{RGB}{255,204,204}
#	\definecolor{sphinxattentionBgColor}{RGB}{255,255,204}
#	\definecolor{sphinximportantBgColor}{RGB}{192,255,204}
#
# However, it require to use sphinx heavy box with:
#
#	\renewenvironment{sphinxlightbox} {%
#		\\begin{sphinxheavybox}
#	}
#		\\end{sphinxheavybox}
#	}
#
# Unfortunately, the implementation is buggy: if a note is inside a
# table, it isn't displayed well. So, for now, let's use boring
# black and white notes.

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# Sorted in alphabetical order
latex_documents = [
]

# Add all other index files from Documentation/ subdirectories
for fn in os.listdir('.'):
    doc = os.path.join(fn, "index")
    if os.path.exists(doc + ".rst"):
        has = False
        for l in latex_documents:
            if l[0] == doc:
                has = True
                break
        if not has:
            latex_documents.append((doc, fn + '.tex',
                                    'Linux %s Documentation' % fn.capitalize(),
                                    'The kernel development community',
                                    'manual'))

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'thelinuxkernel', 'The Linux Kernel Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'TheLinuxKernel', 'The Linux Kernel Documentation',
     author, 'TheLinuxKernel', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True

#=======
# rst2pdf
#
# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# See the Sphinx chapter of https://ralsina.me/static/manual.pdf
#
# FIXME: Do not add the index file here; the result will be too big. Adding
# multiple PDF files here actually tries to get the cross-referencing right
# *between* PDF files.
pdf_documents = [
    ('kernel-documentation', u'Kernel', u'Kernel', u'J. Random Bozo'),
]

# kernel-doc extension configuration for running Sphinx directly (e.g. by Read
# the Docs). In a normal build, these are supplied from the Makefile via command
# line arguments.
kerneldoc_bin = '../scripts/kernel-doc'
kerneldoc_srctree = '..'

# ------------------------------------------------------------------------------
# Since loadConfig overwrites settings from the global namespace, it has to be
# the last statement in the conf.py file
# ------------------------------------------------------------------------------
loadConfig(globals())
