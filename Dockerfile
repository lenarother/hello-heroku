FROM python:3.10.0-alpine

COPY resources/requirements.txt /project/
RUN pip install -r /project/requirements.txt

COPY src/ /project/src/
COPY setup.py /project/

RUN pip install -e /project
WORKDIR /project

# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "teachertools.wsgi:application"]
CMD gunicorn hello_world.wsgi:application --bind 0.0.0.0:$PORT