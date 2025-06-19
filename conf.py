# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------
project = 'SPC 系统文档'
author = 'xielong'
version = '1.0'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_rtd_theme',  # 启用 Read the Docs 主题
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # 使用 Read the Docs 主题
html_static_path = ['_static']

# -- 中文支持 -------------------------------------------------
language = 'zh_CN'
source_encoding = 'utf-8-sig'  # 确保中文编码正确

# -- 文档结构配置 -------------------------------------------------
source_suffix = '.rst'
master_doc = 'index'  # 主文档是 docs/index.rst
