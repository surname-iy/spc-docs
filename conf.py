# conf.py
project = 'SPC 系统文档'
author = '你的名字'
version = '1.0'
release = '1.0'

# ==== 关键修复 ==== #
# 移除 source_dir 设置（使用默认配置）
# 确保源文件目录正确指向
import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # 添加项目根目录到路径

# 主文档设置
master_doc = 'index'  
source_suffix = '.rst'

# 扩展和主题
extensions = ['sphinx_rtd_theme']
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
}
language = 'zh_CN'

# ==== 添加路径配置 ==== #
# 确保 Sphinx 在 docs/ 目录查找文件
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']
