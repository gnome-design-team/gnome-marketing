#!/usr/bin/bash
#ffmpeg -r 24 -f image2 -i %04d.png -b:v 500000000 -an unlock.mp4
for dir in `find . -type d`; do
  echo $dir
	if [ ! -f $dir.mov ]
  	then ffmpeg -r 30 -f image2 -i $dir/%04d.png -vcodec mpeg4 -acodec ac3 -strict -2 -r 30 -g 5 -ab 128k -b:v 100000k -threads 0 $dir.mov > /dev/null
	fi
done

