FROM ubuntu:20.04
WORKDIR /fluent-honey

COPY . .

RUN apt update && \ 
    apt install -y vim libgeoip-dev autoconf libmaxminddb-dev curl sudo ruby-dev build-essential && \
    gem install bundler && \
    bundle install && \
    apt remove -y build-essential curl && \
    apt autoremove -y && \
    apt clean &&  rm -rf /var/lib/apt/lists/*

RUN chmod +x /fluent-honey/entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]