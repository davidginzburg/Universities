FROM python:3.6
WORKDIR /code
# COPY SolarEdge/ .
COPY *.* .
RUN pip install -r requirements.txt
RUN pip install -e .
CMD python ./generate_csv.py
CMD python ./update_csv.py