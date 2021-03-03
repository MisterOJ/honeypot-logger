FROM ubuntu:20.04
RUN groupadd -g 1000 logs
RUN useradd --create-home --shell /bin/bash  --groups 1000 fluent-honey
RUN chown -R fluent-honey.fluent-honey /home/fluent-honey

WORKDIR /home/fluent-honey

COPY . .

RUN apt update && \ 
    apt install -y vim libgeoip-dev autoconf libmaxminddb-dev curl sudo ruby-dev build-essential && \
    gem install bundler && \
    bundle install && \
    apt remove -y build-essential curl && \
    apt autoremove -y && \
    apt clean &&  rm -rf /var/lib/apt/lists/*

RUN chmod +x /home/fluent-honey/entrypoint.sh
USER fluent-honey
ENTRYPOINT [ "./entrypoint.sh" ]