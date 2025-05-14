
FROM python:3.12

WORKDIR /usr/app/src

COPY ./pages/* requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_test.py", "--server.port=8501", "--server.address=0.0.0.0"]