You must replace the "system" variable by the value you get when you write
`p &system - &atoll` as that value will change depending of your system
example :
```
gdb prog.bin
run
^C
p &system - &atoll
```

