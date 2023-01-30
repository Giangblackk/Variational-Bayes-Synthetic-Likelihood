"""Sphinx configuration."""
project = "Variational Bayes Synthetic Likelihood"
author = "Giang Ngo"
copyright = "2023, Giang Ngo"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
