FROM node:10.13.0-alpine as build
RUN set -ex \
    && mkdir -p "/srv/card-collection/"
WORKDIR /srv/card-collection/
COPY [ "package.json", "/srv/card-collection/package.json" ]
COPY [ "package-lock.json", "/srv/card-collection/package-lock.json" ]
RUN set -ex \
    && npm ci
COPY [ ".", "/srv/card-collection/" ]
RUN set -ex \
    && npm run build:production

FROM nginx:1.14.0-alpine
RUN set -ex \
    && rm -f /etc/nginx/conf.d/default.conf

COPY --from=build [ "/srv/card-collection/obj", "/usr/share/nginx/html/" ]

COPY [ "docker/nginx/default.conf.template", "/etc/nginx/conf.d/default.conf" ]
CMD [ "nginx", "-g", "daemon off;" ]
