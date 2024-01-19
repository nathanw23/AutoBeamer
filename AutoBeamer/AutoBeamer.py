import click
import os
import subprocess

@click.command()
@click.option("--folder_path", required=True, help="The folder containg the images")

def auto_beamer(folder_path):
    latex_code = "\\documentclass{beamer}\n\n"
    latex_code += "\\usepackage{tcolorbox}\n"
    latex_code += "\\usepackage{graphicx}\n"
    latex_code += "\\graphicspath{{Figures/}}\n"
    latex_code += "\\usepackage{booktabs}\n"
    latex_code += "\\usepackage{tikz}\n"
    latex_code += "\\usetikzlibrary{shapes, arrows}\n"
    latex_code += "\\usepackage{pgfpages}\n"
    latex_code += "\\usepackage{todonotes}\n"
    latex_code += "\\presetkeys{todonotes}{inline}{}\n"
    latex_code += "\\usepackage[none]{hyphenat}\n\n"
    latex_code += "\\usetheme{default}\n\n"
    latex_code += "\\definecolor{mypink}{HTML}{FF7878}\n"
    latex_code += "\\definecolor{myblue}{HTML}{51B5F8}\n"
    latex_code += "\\definecolor{mygreen}{HTML}{68E1AA}\n"
    latex_code += "\\definecolor{mypurple}{HTML}{B869EA}\n"
    latex_code += "\\definecolor{myorange}{HTML}{FF5500}\n"
    latex_code += "\\definecolor{title}{RGB}{32,71,105}\n\n"
    latex_code += "\\setbeamertemplate{navigation symbols}{}\n"
    latex_code += "\\setbeamertemplate{footline}{\\raisebox{10pt}{\\makebox[\\paperwidth]{\\hfill\\makebox[20pt]{\\small\\insertframenumber}}}}\n"
    latex_code += "\\setbeamercolor{title}{bg=white,fg=title}\n"
    latex_code += "\\setbeamerfont{title}{size=\\huge \\bfseries}\n"
    latex_code += "\\setbeamercolor{titlelike}{bg=title,fg=white}\n"
    latex_code += "\\setbeamercolor{itemize item}{fg=title}\n"
    latex_code += "\\setbeamercolor{enumerate item}{fg=title}\n"
    latex_code += "\\setbeamercolor{footline}{fg=title}\n"
    latex_code += "\\setbeamercolor{button}{bg=title,fg=white}\n"
    latex_code += "\\setbeamertemplate{sections/subsections in toc}[circle]\n"
    latex_code += "\\setbeamercolor{section number projected}{bg=title,fg=white}\n"
    latex_code += "\\setbeamercolor{section in toc}{fg=black}\n"
    latex_code += "\\setbeamercolor{subsection in toc}{fg=black}\n\n"
    latex_code += "\\newenvironment{purple_block}[1]{\\begin{tcolorbox}[colback=mypurple!10, colframe=mypurple!50, coltitle=mypurple!30!black,fonttitle=\\bfseries, title= #1]}{\\end{tcolorbox}}\n"
    latex_code += "\\newenvironment{blue_block}[1]{\\begin{tcolorbox}[colback=myblue!10, colframe=myblue!50, coltitle=myblue!30!black,fonttitle=\\bfseries, title= #1]}{\\end{tcolorbox}}\n\n"
    latex_code += "\\newcommand{\\keyword}[1]{\\colorbox{mypurple!40}{\\textbf{#1}}}\n\n"
    latex_code += "\\newcommand{\\sectionframe}[1]{{\n"
    latex_code += "\\section{#1}\n"
    latex_code += "\\setbeamercolor{background canvas}{bg=title}\n"
    latex_code += "\\begin{frame}\n"
    latex_code += "\\begin{center}\n"
    latex_code += "\\Huge{\\textcolor{white}{#1}}\n"
    latex_code += "\\end{center}\n"
    latex_code += "\\end{frame}\n"
    latex_code += "}}\n\n"
    latex_code += "\\title{Presentation Title}\n"
    latex_code += "\\subtitle{Presentation Subtitle}\n"
    latex_code += "%\\institute{Institute}\n"
    latex_code += "%\\author{Author}\n"
    latex_code += "\\date{\\today}\n\n"
    latex_code += "\\begin{document}\n\n"
    
    # Title slide
    latex_code += "\\begin{frame}\n"
    latex_code += "\\titlepage\n"
    latex_code += "\\end{frame}\n\n"
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".png") or file_name.endswith(".jpg"):
            image_path = os.path.join(folder_path, file_name)
            frame_title = os.path.splitext(file_name)[0]  # Get the image name without the extension
            frame_code = f"\\begin{{frame}}\n\\frametitle{{{frame_title}}}\n\\includegraphics[width=\\textwidth]{{{file_name}}}\n\\end{{frame}}\n\n"
            latex_code += frame_code
    
    latex_code += "\\end{document}"
    
    # Write the LaTeX code to a .tex file
    latex_file_path = os.path.join(folder_path, "slides.tex")
    with open(latex_file_path, "w") as latex_file:
        latex_file.write(latex_code)
    
    print(f"LaTeX beamer file created: {latex_file_path}")
    
    # Compile the LaTeX file using pdflatex
    subprocess.run(["pdflatex", "-output-directory", folder_path, latex_file_path])
    
    print(f"PDF file created: {os.path.join(folder_path, 'slides.pdf')}")
    
    # Remove auxiliary files
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".aux") or file_name.endswith(".log") or file_name.endswith(".nav") or file_name.endswith(".out") or file_name.endswith(".snm") or file_name.endswith(".toc"):
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
    
    print("Auxiliary files removed.")

    os.system(os.path.join(folder_path, 'slides.pdf'))

if __name__ == "__main__":
    # Specify the folder path here
    auto_beamer(folder_path)

