FROM ubuntu:18.04
RUN groupadd -g 1000 logs
RUN useradd --create-home --shell /bin/bash --groups 1000 honeydb
WORKDIR /home/honeydb

RUN apt update && apt install -y curl apt-transport-https vim
RUN curl -1sLf \
'https://dl.cloudsmith.io/public/honeydb/honeydb-agent/cfg/setup/bash.deb.sh' \
| distro=ubuntu bash
RUN apt-get install honeydb-agent

COPY ./agent.conf /etc/honeydb/agent.conf
COPY ./entrypoint.sh .

# RUN touch /honeydb/log/auth.log
RUN chmod +x /home/honeydb/entrypoint.sh
USER honeydb
ENTRYPOINT [ "sh", "./entrypoint.sh" ]