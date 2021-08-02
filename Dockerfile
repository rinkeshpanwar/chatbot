FROM ubuntu:20.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3.6 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip install --no-cache rasa
ADD . /app/
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh