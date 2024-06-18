FROM python:3.9-slim
# Uses the official slim Python 3.9 image as the base image, which is a minimalistic version of Python.

ENV PYTHONUNBUFFERED=1
# Ensures that Python output is sent straight to the terminal without being buffered.

ENV PYTHONWRITEBYTECODE=1
# Prevents Python from writing .pyc files to the disk, which can save space and speed up the build process.

WORKDIR /app
# Sets the working directory inside the container to /app.

COPY requirements.txt /app/
# Copies the requirements.txt file from the host to the /app directory inside the container.

RUN pip3 install --upgrade pip
# Upgrades pip to the latest version.

RUN pip3 install -r requirements.txt
# Installs the Python packages specified in the requirements.txt file.

COPY ./core /app
# Copies the local core directory to the /app directory inside the container.

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# Sets the default command to run the Django development server, listening on all network interfaces at port 8000.
