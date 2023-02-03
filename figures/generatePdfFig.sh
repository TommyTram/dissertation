#!/bin/bash
pdflatex --jobname=$2 $1
mv $2.pdf imgs/$2.pdf
rm *.log
