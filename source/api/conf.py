import sys, os

extensions = ['sphinx.ext.intersphinx']

intersphinx_mapping = {'blender_manual': ('https://docs.blender.org/manual/en/dev/', None)}

project = 'Blender'
copyright = u'Blender Foundation'
version = '2.79.1 e432371ed2 - API'
release = '2.79.1 e432371ed2 - API'
exclude_patterns = [
    'include__bmesh.rst',
]

html_theme = 'classic'
html_copy_source = False
html_show_sphinx = False
html_split_index = True
html_extra_path = ['__/static/favicon.ico', '__/static/blender_logo.svg']
html_favicon = '__/static/favicon.ico'
html_logo = '__/static/blender_logo.svg'

latex_elements = {
  'papersize': 'a4paper',
}

latex_documents = [ ('contents', 'contents.tex', 'Blender Index', 'Blender Foundation', 'manual'), ]

from sphinx.domains.python import PythonDomain

class PatchedPythonDomain(PythonDomain):
    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        if 'refspecific' in node:
            del node['refspecific']
        return super(PatchedPythonDomain, self).resolve_xref(
            env, fromdocname, builder, typ, target, node, contnode)

def setup(sphinx):
    sphinx.override_domain(PatchedPythonDomain)
