# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'SPC 系统文档'
author = '你的名字'  # 替换成实际作者名
version = '1.0'
release = '1.0'

# -- General configuration ---------------------------------------------------
# 文档源文件的后缀
source_suffix = '.rst'
# 主文档文件，这里要写相对于源目录的路径，因为下面设置了源目录是 docs
master_doc = 'index'  
# 设置文档的源目录为 docs 文件夹，Sphinx 会从这个目录读取文档源文件
source_dir = 'docs'  
# 额外的扩展，可以根据需要添加，比如 'sphinx_rtd_theme' 等
extensions = []  

# 要排除的文件或目录，构建时不会处理这些内容
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# 使用的 HTML 主题，这里用 sphinx_rtd_theme（需在 requirements.txt 中配置依赖）
html_theme = 'sphinx_rtd_theme'  
# HTML 静态文件目录，若有自定义静态资源可放这里，注意目录要实际存在
html_static_path = ['_static']  

# -- 中文支持相关配置 -------------------------------------------------
# 文档使用的语言
language = 'zh_CN'  
# 源文件编码，确保中文等字符能正确处理
source_encoding = 'utf-8-sig'  
