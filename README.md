# **WAF using AI**
This is a web application firewall utilizes AI to detect and drop malicious payloads.

## **Prerequest**:
### data
Before executing the init_models.py script in the classifiers folder, create a directory named "data" and place your data within it.

### enviroment
create virtual enviroment (optional)<br>
```
python -m virtualvenv venv<br>
source venv/bin/activate<br>
```

### install pakages
```
pip install -r requirements.txt
```

## **Usage**:
### assign origin srever url to .env
```
echo "http://www.your-service-server" > .env
```

### initilize models
go to classifiers folder and excute following:<br>
```
python init_models.py
```

### start WAF
go to waf folder and excute following command:<br>
```
flask --app waf run
```
