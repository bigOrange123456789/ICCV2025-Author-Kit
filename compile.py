# import subprocess

# # LaTeX源文件路径
# tex_file = "main.tex"

# # 调用pdflatex命令进行编译
# subprocess.run(["pdflatex", tex_file])

# print("PDF文件已生成")


from latex2pdf import process

# LaTeX代码
latex_code = r"""
\documentclass{article}
\begin{document}
Hello, \textbf{world}!
\end{document}
"""

# 将LaTeX代码转换为PDF
process(latex_code, 'example.pdf')