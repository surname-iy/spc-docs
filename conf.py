# conf.py
project = 'SPC 系统文档'    # 文档项目名称
author = '你的名字'         # 作者
version = '1.0'             # 文档版本
release = '1.0'             # 发布版本

# 文档源目录（Sphinx 会从 docs/ 读取 RST 文件）
source_suffix = '.rst'      # RST 文件后缀
master_doc = 'index'        # 主页文档（对应 docs/index.rst）

# 扩展与主题（可选，按需添加）
extensions = []
html_theme = 'alabaster'    # 或 'sphinx_rtd_theme'（Read the Docs 推荐）
