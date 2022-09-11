#!/bin/bash
for arg in ${@:1:$#-1}
do
	echo "Making $arg..."
	bash generateTexFigure.sh $arg ${@: -1} 500
done
