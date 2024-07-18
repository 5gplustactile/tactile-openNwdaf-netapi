#!/bin/bash
HOSTNAME=localhost
echo Nginx hostname will be $HOSTNAME and deploy $DEPLOY


NWDAF_HOSTNAME=$HOSTNAME docker compose -f "docker-compose.yml" up --detach --build
status=$?
if [ $status -eq 0 ]; then
    echo "*** All NWDAF services are running ***"
else
    echo "*** Some NWDAF services failed to start ***"
    exit $status
fi

exit $status