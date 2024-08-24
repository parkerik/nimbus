FROM python:3.11-slim

WORKDIR /code

RUN pip install uv

COPY ./requirements.txt /code/requirements.txt

RUN uv pip install --system -r /code/requirements.txt

COPY ./src /code/src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
