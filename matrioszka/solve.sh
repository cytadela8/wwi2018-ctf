#!/usr/bin/bash

mv * asdert
file asdert
file asdert | grep -i uharc && mv asdert asd.uha && wine ~/.wine/drive_c/Program\ Files\ \(x86\)/WinUHA/UHARC.EXE e asd.uha ; rm asd.uha
cp asdert "../backup/$(date)"

cp asdert asdert.kgb
file asdert | grep -i kgb && ../kgb_arch asdert.kgb
rm asdert.kgb

cp asdert asdert.zoo
file asdert | grep -i zoo && zoo -extract asdert.zoo
rm asdert.zoo

cp asdert asdert.zip
file asdert | grep -i zip && unzip asdert.zip
rm asdert.zip

cp asdert asdert2.tar
file asdert | grep -i tar && tar xf asdert2.tar
rm asdert2.tar

cp asdert asdert2.gz
file asdert | grep -i gzip && gzip -d asdert2.gz
rm asdert2.gz

cp asdert asdert2.7z
file asdert | grep -i 7-zip && 7z e asdert2.7z
rm asdert2.7z

cp asdert asdert2.lzma
file asdert | grep -i lzma && lzma -d asdert2.lzma
rm asdert2.lzma

cp asdert asdert.arj
file asdert | grep -i arj && unarj e asdert
rm asdert.arj

cp asdert asdert.bzip
file asdert | grep -i bzip && bzip2 -d asdert.bzip 
rm asdert.bzip

cp asdert asdert2.xz
file asdert | grep -i xz && xz --decompress asdert2.xz
rm asdert2.xz

cp asdert asdert2.rar
file asdert | grep -i rar && unrar e asdert2.rar
rm asdert2.rar

rm asdert
