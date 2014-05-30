python-oauth2
=============

python-oauth2 repo with working test in flask

#Install on clean centos
yum install wget

wget http://mirror-fpt-telecom.fpt.net/fedora/epel/6/i386/epel-release-6-8.noarch.rpm

rpm -ivh epel-release-6-8.noarch.rpm

yum -y install python-pip git

#Install this deps

sudo pip install flask

sudo pip install SQLAlchemy

sudo pip install Flask-SQLAlchemy

sudo pip install flask_oauthlib

#Installing

git clone git@github.com:mattiashem/python-oauth2.git

cd python-oauth2/

#Config

Change ip address in client and app to match you network

#run the & make they run i background

python app.py  &

python client2.py &


#Disable

/etc/init.d/iptables stop

setenforce 0


