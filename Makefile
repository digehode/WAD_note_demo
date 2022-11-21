#Set up the local database password, user, database name and port
LDBPW = swordfish
LDBUSER = demodb
LDB = demodb
LDBPORT = 3333

#Set up DB container names
CONTAINERNAME = demodb

#Admin port
ADMIN_PORT=90

# Don't change these settings
CWD = $(shell pwd)
DATADIR=data


docs:
	pdoc3 --force --html src/*.py -o docs

start_db:
	docker run  -p ${LDBPORT}:3306 --name ${CONTAINERNAME} -v ${CWD}/${DATADIR}:/var/lib/mysql -e MARIADB_ROOT_PASSWORD=${LDBPW} -e MARIADB_USER=${LDBUSER} -e MARIADB_PASSWORD=${LDBPW} -e MARIADB_ROOT_HOST=localhost -e MARIADB_DATABASE=${LDB} -d mariadb:latest


local_db_shell:
	mysql --user=${LDBUSER} --password=${LDBPW} --host=127.0.0.1 --port=${LDBPORT} ${LDB}

stop:
	-docker kill ${CONTAINERNAME}
	-docker rm ${CONTAINERNAME}
	-docker kill ${CONTAINERNAME}-admin
	-docker rm ${CONTAINERNAME}-admin

clean:
	-sudo rm -rf ./${DATADIR}/*

start_admin:
	-docker volume create ${CONTAINERNAME}-admin-volume
	docker run --name ${CONTAINERNAME}-admin -v ${CONTAINERNAME}-admin-volume:/etc/phpmyadmin/config.user.inc.php --link ${CONTAINERNAME}:db -p ${ADMIN_PORT}:80 -d phpmyadmin/phpmyadmin
