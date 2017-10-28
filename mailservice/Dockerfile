FROM python:3.4.2-slim
EXPOSE 8002
ENV WSGI_CONF /etc/apache2/sites-available/000-default.conf
WORKDIR /var/www

# Install Dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends libmysqlclient-dev gcc unzip cron apache2 python3-dev libapache2-mod-wsgi-py3 libsasl2-dev \
    libldap2-dev libssl-dev libcurl4-openssl-dev libbz2-dev \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /dev/stdout /var/log/apache2/access.log
RUN ln -sf /dev/stderr /var/log/apache2/error.log

RUN pip install --upgrade awscli && pip install -i https://pypi.swarm.devfactory.com/simple/ iws-logging
ADD . .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
COPY ./apache-conf.conf ${WSGI_CONF}
RUN chmod +x run.sh
RUN chmod -R 757 /var/www
CMD ./run.sh