# -*- coding: utf-8 -*-
import os
import sys

# 添加项目根目录到系统路径
sys.path.insert(0, os.path.abspath('.'))

project = 'SPC 系统文档'
author = '您的名字'
copyright = f'2023, {author}'
version = '1.0'
release = '1.0'

# 核心设置
master_doc = 'index'
source_suffix = '.rst'

# 扩展模块
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
]

# 主题设置
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
}

# 语言设置
language = 'zh_CN'

# 路径设置
templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# 解决中文路径问题
def setup(app):
    app.add_config_value('recommonmark_config', {
        'enable_auto_toc_tree': True,
        'auto_toc_tree_section': '目录',
    }, True)
