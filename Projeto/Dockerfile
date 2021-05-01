FROM python
RUN apt-get update && apt-get install python-pip -y && apt-get install python-dev -y
WORKDIR /projetoFlask
ADD flask_app /projetoFlask
RUN pip install -r requirements.txt 
CMD ["python","app.py"]