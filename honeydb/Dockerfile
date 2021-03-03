FROM ubuntu:18.04
WORKDIR /honeydb

RUN apt update && apt install -y curl apt-transport-https vim
RUN curl -1sLf \
'https://dl.cloudsmith.io/public/honeydb/honeydb-agent/cfg/setup/bash.deb.sh' \
| distro=ubuntu bash
RUN apt-get install honeydb-agent

COPY ./agent.conf /etc/honeydb/agent.conf
COPY ./entrypoint.sh .

# RUN touch /honeydb/log/auth.log
RUN chmod +x /honeydb/entrypoint.sh
ENTRYPOINT [ "sh", "./entrypoint.sh" ]