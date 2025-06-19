# -*- coding: utf-8 -*-
project = 'SPC 系统文档'
author = '你的名字'
version = '1.0'
release = '1.0'

# 显式设置文档源目录为 docs/
source_dir = 'docs'  
# 主文档是 docs/index.rst（只需写文件名，Sphinx 从 source_dir 查找）
master_doc = 'index'  

source_suffix = '.rst'
extensions = [
    'sphinx_rtd_theme',  # 确保已安装
]
html_theme = 'sphinx_rtd_theme'
language = 'zh_CN'
