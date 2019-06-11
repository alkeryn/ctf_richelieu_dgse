#/usr/env bash
cat motDePasseGPG.txt.enc | openssl rsautl -decrypt -inkey priv.key
