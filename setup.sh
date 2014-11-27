#!/bin/bash
# Ce fichier est lancé à l'éxécution de la machine
# Il lance les services requis et donne un accès

cd /var/SimpleNote

IP=$(ip addr | grep 172 | awk '{ print $2 }' | cut --delimiter=/ -f1)
echo "La machine est accessible sur http://$IP"
bash
