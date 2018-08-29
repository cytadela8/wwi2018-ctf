gcc -Wall -Wextra -Wconversion -fPIE -Wno-unused-parameter -Wformat=2 -Wformat-security -fstack-protector-all -Wstrict-overflow \
    -pie \
    -o pwn.e pwn.c
