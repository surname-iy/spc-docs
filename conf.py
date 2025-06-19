# conf.py
project = 'SPC 系统文档'
author = '你的名字'
version = '1.0'
release = '1.0'

source_suffix = '.rst'
master_doc = 'docs/index'  # 主文档路径

extensions = [
    'sphinx_rtd_theme',  # 仅保留必要扩展
]

html_theme = 'sphinx_rtd_theme'  # 使用 RTD 主题
language = 'zh_CN'
