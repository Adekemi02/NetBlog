# set base image (host OS)
FROM ubuntu

# update apt and installpython and pip
RUN apt update
RUN apt install -y python3  python3-pip

# copy the dependencies file to the working directory
COPY NetBlog /opt/NetBlog

# install project dependencies
RUN pip3 install -r /opt/NetBlog/requirements.txt
RUN pip3 install flask

# entry point to start the container
ENTRYPOINT FLASK_APP=/opt/NetBlog/run.py flask run --host=0.0.0.0
