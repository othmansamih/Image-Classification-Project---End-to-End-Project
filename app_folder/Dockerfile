# This sets up the container with Python 3.10 installed
FROM python:3.10-slim

# This copies everything in the current directory into the /app directory in the container
COPY . /app

# This sets the /app directory as the working directory for any RUN, CMD, ENTRYPOINT, or COPY that follows
WORKDIR /app

# This run pip install to all the packages listed in the requirements file
RUN pip install -r requirements.txt

# This tells docker to lister on port 80 at runtime. Port 80 is the standard port for HTTP
EXPOSE 80

# This creates a .streamlit directory in the home directory of the container
RUN mkdir ~/.streamlit

# This copies the streamlit configuration file to the .streamlit directory you just created
RUN cp config.toml ~/.streamlit/config.toml

# This copies the credentials file to the .streamlit directory you just created
RUN cp credentials.toml ~/.streamlit/credentials.toml

# This sets the default command for the container to run the app with streamlit
ENTRYPOINT ["streamlit", "run"]

# This command tells streamlit to run main.py when the container starts
CMD ["main.py"]