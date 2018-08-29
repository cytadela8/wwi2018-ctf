FROM python:3.7-stretch

RUN pip3 install flask

RUN useradd -m ctf

COPY app.py /home/ctf/
COPY templates/page.html /home/ctf/templates/
COPY flag.txt /flag

RUN chown -R root:ctf /home/ctf /flag && \
    chmod -R 750 /home/ctf            && \
    chmod 740 /flag

USER ctf:ctf

WORKDIR "/home/ctf"

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
