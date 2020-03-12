#!/bin/bash

cd /home/arista/atd-docker

# docker build --build-arg UID=$(id -u arista) -t atddocker_login:1.0 login/.
docker build --build-arg UID=$(id -u arista) -t atddocker_kvmbuilder:1.0 kvmbuilder/.
docker build --build-arg UID=$(id -u arista) -t atddocker_desktop:1.0 desktop/.
docker build --build-arg UID=$(id -u arista) -t atddocker_cvpupdater:1.0 cvpUpdater/.
docker build --build-arg UID=$(id -u arista) -t atddocker_gitconfigletsync:1.0 gitConfigletSync/.
docker build --build-arg UID=$(id -u arista) -t atddocker_sslupdater:1.0 sslUpdater/.
docker build --build-arg UID=$(id -u arista) -t atddocker_labguides:1.0 labguides/.
docker build -t atddocker_freerad:1.1 freeradius/.
docker build -t atddocker_nginx:1.0 nginx/.
docker build -t atddocker_http:1.1 http/.
docker build -t atddocker_guacd:1.0 guacd/.
docker build -t atddocker_guacamole:1.0 guacamole/.
docker build -t atddocker_jenkins:1.0 jenkins/.
