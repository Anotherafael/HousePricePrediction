FROM python:3.12.3-bookworm

WORKDIR /backend

COPY ./requirements.txt .
 
RUN pip install -r requirements.txt

COPY ./backend .

CMD ["python", "/backend/server.py"]