# **WAF using AI**
This is a web application firewall utilizes AI to detect and drop malicious payloads.

## **Prerequest**:
### Data
Before executing the init_models.py script in the classifiers folder, create a directory named "data" and place your data within it.

### Enviroment (optional)
create virtual enviroment <br>
```
$ python -m virtualvenv venv
$ source venv/bin/activate
```

### Install pakages
```
$ pip install -r requirements.txt
```

## **Usage**:
Assign origin srever url to .env
```
$ echo "http://www.your-service-server" > .env
```

### Initilize models
go to classifiers folder and excute following:<br>
```
$ python init_models.py
```

### Start WAF
go to waf folder and excute following command:<br>
```
$ flask --app waf run
```
