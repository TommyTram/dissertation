#!/bin/bash
echo -n Converting pdf...
pdflatex --jobname=$1 $2 > /dev/null
echo "done"

if [ -z "$3" ]; then
	png_density=500
else
	png_density=$3
fi
echo -n "Converting to png with density $png_density..."
pdftoppm -r $png_density $1.pdf $1 -png
mv $1*.png $1.png
echo "done"
echo -n "Removing random build files and original pdf..."
rm -rf *.auxlock *.dpth *.log *.dvi *.aux *md5 *.log *.synctex.gz $1.pdf
echo "done"
