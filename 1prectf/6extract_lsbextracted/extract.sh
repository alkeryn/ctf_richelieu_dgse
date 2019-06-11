#!/usr/bin/env bash
head -n18594 lsbextracted | xxd -r | bbe -e 's/ALD/UPX/g' > binary
upx -d binary
chmod +x binary
