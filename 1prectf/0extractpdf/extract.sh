#!/usr/bin/env bash
pdftotext ./Richelieu.pdf
tail -n +9 Richelieu.txt | base64 -di > Richelieu.jpg
ZIPASSWORD=$(strings Richelieu.jpg | grep est | cut -c 7- | rev | cut -c 3- | rev)
echo $ZIPASSWORD
unzip -P $ZIPASSWORD -d extract ./Richelieu.jpg
