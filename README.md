# **WAF using AI**
> This is a reverse proxy with AI that drop requests if they are malicious

## **Prerequest**:
> pip install -r requirements.txt

## **Usage**:
### assign origin srever url to .env
> echo "http://www.your-service-server" > .env

### start WAF
> flask --app waf run

## **Todo**:
- Store malicious request information for training model
- Create a whitelist with client for reducing check tasks
