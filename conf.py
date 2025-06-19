# -*- coding: utf-8 -*-
project = 'SPC 系统文档'
author = '你的名字'
version = '1.0'
release = '1.0'

# 文档源目录（Sphinx 会从 docs/ 读取 RST 文件）
source_dir = 'docs'  
source_suffix = '.rst'

# 主文档是 docs/index.rst（只需指定文件名，Sphinx 从 source_dir 查找）
master_doc = 'index'  

extensions = [
    'sphinx_rtd_theme',  # 确保已安装
]

html_theme = 'sphinx_rtd_theme'
language = 'zh_CN'
