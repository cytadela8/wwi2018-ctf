FROM ubuntu:16.04

RUN apt-get -y update
RUN apt-get -y install xinetd python3 python3-crypto

RUN useradd -m ctf

WORKDIR /home/ctf

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh
COPY app.py flag.txt key.txt /home/ctf/


RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf

CMD ["/start.sh"]
