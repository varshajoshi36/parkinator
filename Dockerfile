#
# `ARG` is the only directive allowed before the `FROM` directive.
#
# This is used to dynamically change the tag for this python image. Use with caution.
ARG PYTHON_VERSION=2.7
FROM python:${PYTHON_VERSION}-alpine

# This is a build arg that could be overwritten, but is unlikely to be.
ARG WWW_ROOT=/usr/src/app

WORKDIR ${WWW_ROOT}

RUN apk upgrade --no-cache

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY www ${WWW_ROOT}

EXPOSE 8080

CMD ["python", "/usr/src/app/app.py"]
