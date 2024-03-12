FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /cars
COPY . /cars/
RUN pip install -r requirements.txt


EXPOSE 8000  
# start server  
ENTRYPOINT ["python", "app/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]