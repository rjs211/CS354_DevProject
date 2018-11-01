#!/bin/bash

cd $1
ls
zip -r final.odt mimetype .
shopt -s extglob
rm -rf !(final.odt)
shopt -u extglob
libreoffice --headless --convert-to pdf final.odt
#UNO_PATH=/usr/lib/libreoffice unoconv -f pdf final.odt
cd ../../../../
