# WWI2018 CTF
CTF z Wakacyjnych Warsztatów Wielodyscyplinarych 2018 (WWI2018)

## Uruchamianie

1. `git clone --recurse-submodules https://github.com/cytadela8/wwi2018-ctf.git`

`--recurse-submodules` jest bardzo ważne ze względu na podmoduł `nsjail` i podmoduł `nsjail/kafel`

2. Zainstaluj i ruchom dockera - https://docs.docker.com/install/

3. `docker-compose up --build` zbudowanie i uruchomienie wszystkich kontenterów. Aby zatrzymać naciśnij Ctrl-C

Alternatywnie można uruchomić wyłącznie jeden kontener poleceniem `docker-compose up --build NAZWA_KONTENERA`

4. Poszczególne kontery znajdują się na portach:
- drone - 1000
- drone2 - 1001
- pwn - 1002
- aes_ecb_text - 1003
- bash_injection - 1004
- glebokie_ukrycie - 1005
