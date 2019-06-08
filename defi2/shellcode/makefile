all: compile

compile:
	nasm -f elf64 shellcode.asm
	ld -m elf_x86_64 shellcode.o -o shellcode
	@objdump -M intel -d shellcode |  grep -Po '\s\K[a-f0-9]{2}(?=\s)' | sed '1,2d;s/^/\\x/g' |  sed -z 's/\n//g'
# @objdump -M intel -d shellcode |  grep -Po '\s\K[a-f0-9]{2}(?=\s)' | sed '1,2d;s/^/\\x/g;s/\\x00//g' |  sed -z 's/\n//g'
clean:
	@-rm -f shellcode shellcode.o
