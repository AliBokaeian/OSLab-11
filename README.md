# OSLab-11

1)



link : https://stackoverflow.com/questions/68101788/exception-in-tkinter-callback-typeerror-in-python


---------------------------------------------------------


2)


Latex:


\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{graphics}
\usepackage{subfigure}
\usepackage{listings}
\title{OSLab-11}
\author{Ali Boakeian}
\date{June 2021}

\begin{document}

\maketitle

\section{Introduction}
I'm Ali Bokaeian, 21 years old and i live in Mashhad.
I am a bachelor's degree student in computer engineering at Sadjad University and also I'm Python Developer.
My favorite technologies are ALPR and Autonomous Vehicles, and I would love to work in the field of Autonomous Vehicles. I'm currently learning computer vision.
I can also speak English and German.


\section{Table}
\begin{table}[h!]
    \centering
    \begin{tabular}{|c|c|c|}
    \hline
        \textbf number 1 &\textbf number 2 &\textbf result \\
         \hline
         2 & 2 & 4 \\
         \hline
         3 & 8 & 24 \\
         \hline
    \end{tabular}
    \caption{Multiplication}
    \label{tab:my_label}
\end{table}

\section{Math}
$$ \int x^n + y^n-1 $$




\section{Coding}
\begin{lstlisting}

    
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return(fibo(n-1) + fibo(n-2))

number = int(input("Please Enter a Number:  "))
print(fibo(number))
    
\end{lstlisting}



\section{Image}
\begin{figure} 
    \centering
    \includegraphics{AliBi-IMG.jpg}
    \caption{Ali Bokaeian}
    \label{fig:AliBi.jpg}
\end{figure}



\end{document}
