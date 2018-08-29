FROM python:3.7.0-slim-stretch

RUN apt-get update --fix-missing && \
    apt-get -y upgrade

RUN groupadd -r drone            && \
    useradd -r -g drone drone

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN chmod 700 requirements.txt
RUN python3 -m pip install -r requirements.txt && \
    rm requirements.txt


COPY app.py parse_map.py map.png ./
RUN chown root:drone -R ./ && \
    chmod 750 ./           && \
    chmod 740 ./*


USER drone:drone
CMD ["python3", "app.py"]
