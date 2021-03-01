FROM python:3

WORKDIR /decoder

RUN apt-get update
RUN apt-get -y install python3-pip

# Add necessary files
COPY . .

# Install requirements
RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh

# Run the command on container startup
ENTRYPOINT [ "sh", "entrypoint.sh" ]