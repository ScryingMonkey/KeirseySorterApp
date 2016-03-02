apt-get -qqy update
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-sqlalchemy
apt-get -qqy install python-pip
pip install werkzeug==0.8.3
pip install flask==0.9
pip install Flask-Login==0.1.3
pip install oauth2client
pip install requests
pip install httplib2

apt-get install git    
apt-get install ruby-full
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
gem install foreman

pip freeze >requirements.txt

