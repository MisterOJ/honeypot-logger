FROM python:3
RUN useradd --create-home --shell /bin/bash decoder
WORKDIR /home/decoder

RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get -y install build-essential
RUN apt-get -y install libgeoip-dev
RUN apt-get -y install libmaxminddb-dev

# Add necessary files
COPY . .

# Install requirements
RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh
USER decoder
# Run the command on container startup
ENTRYPOINT [ "sh", "entrypoint.sh" ]