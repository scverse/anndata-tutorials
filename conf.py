from datetime import datetime
project = 'anndata'
author = 'andata developers'
copyright = f'{datetime.now():%Y}, {author}'

version = ''
release = version

extensions = [
    'nbsphinx',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

html_theme = 'scanpydoc'
html_theme_options = dict(navigation_depth=4)
html_context = dict(
    display_github=True,      # Integrate GitHub
    github_user='theislab',   # Username
    github_repo='anndata-tutorials',     # Repo name
    github_version='master',  # Version
    conf_py_path='/',    # Path in the checkout to the docs root
)
html_show_sphinx = False


# -- Strip output ----------------------------------------------

# import nbclean, glob
# for filename in glob.glob('**/*.ipynb', recursive=True):
#     ntbk = nbclean.NotebookCleaner(filename)
#     ntbk.clear('stderr')
#     ntbk.save(filename)
