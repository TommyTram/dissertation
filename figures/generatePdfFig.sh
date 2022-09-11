#!/bin/bash
pdflatex --jobname=$1 $2.tex
mv $1.pdf imgs/$1.pdf
rm *.log
