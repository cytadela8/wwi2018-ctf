FROM nsjail

RUN apt-get update --fix-missing && \
    apt-get -y upgrade

RUN groupadd -r pwn       && \
    useradd -r -g pwn pwn

RUN mkdir /app
WORKDIR /app


COPY nsjail.sh pwn.e flag ./


RUN chown root:pwn -R ./ && \
    chmod 710 nsjail.sh  && \
    chmod 710 pwn.e      && \
    chmod 740 flag


ENTRYPOINT ["./nsjail.sh"]
CMD ["./pwn.e"]
