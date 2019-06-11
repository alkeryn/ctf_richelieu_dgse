cat password | gpg --batch --yes --passphrase-fd 0 -d ./lsb_RGB.png.enc > ./lsb_RGB.png
