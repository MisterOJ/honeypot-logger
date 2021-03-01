#!/usr/bin/bash
set -e
fluentd -c /fluent-honey/fluent.conf -o /var/log/fluent.log