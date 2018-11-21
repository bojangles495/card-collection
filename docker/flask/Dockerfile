FROM python:3.7.1-alpine3.8

RUN set -ex \
    ; apk add --no-cache --virtual build-dependencies \
        build-base \
        linux-headers
RUN set -ex \
    ; mkdir -p "/srv/card-collection"
COPY [ "requirements.txt", "/srv/card-collection/requirements.txt" ]
WORKDIR /srv/card-collection
RUN set -ex \
    ; pip install -r requirements.txt \
    ; apk del build-dependencies
COPY [ ".", "/srv/card-collection" ]

CMD ["uwsgi", "-s", "0.0.0.0:3011", "--manage-script-name", "--mount", "/=run:app"]
