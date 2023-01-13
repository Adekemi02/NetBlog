# set base image (host OS)
FROM python:3.9.16-slim-bullseye

# copy the dependencies file to the working directory
COPY NetBlog /opt/NetBlog

# install project dependencies
RUN pip install -r /opt/NetBlog/requirements.txt
RUN pip install flask

# port to run app
EXPOSE 5000

# working directory
WORKDIR /opt/NetBlog

# entry point to start the container
ENTRYPOINT FLASK_APP=/opt/NetBlog/run.py flask run --host=0.0.0.0
