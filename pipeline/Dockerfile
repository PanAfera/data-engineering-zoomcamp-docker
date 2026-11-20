FROM python:3.14.2-slim

RUN pip install pandas pyarrow

WORKDIR /code

COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]