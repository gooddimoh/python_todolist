
## Getting started
```bash
git clone https://github.com/a2975667/flask-gcp-mysql-demo.git
cd flask-gcp-mysql-demo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP = app
flask run
```

## Setting up GCP
Create a `app.yaml` file in the root folder with the following content:
```yaml
runtime: python38 # or another supported version

instance_class: F1

env_variables:
  MYSQL_USER: <user_name> # please put in your credentials
  MYSQL_PASSWORD: <user_pw> # please put in your credentials
  MYSQL_DB: <database_name> # please put in your credentials
  MYSQL_HOST: <database_ip> # please put in your credentials

handlers:
# Matches requests to /images/... to files in static/images/...
- url: /img
  static_dir: static/img

- url: /script
  static_dir: static/script

- url: /styles
  static_dir: static/styles
