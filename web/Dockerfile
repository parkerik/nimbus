FROM python:3.11-slim

WORKDIR /code

RUN pip install uv

COPY ./requirements.txt /code/requirements.txt

RUN uv pip install --system -r /code/requirements.txt

COPY  ./src /code/src
COPY ./.streamlit /code/.streamlit

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "src/main.py"]
