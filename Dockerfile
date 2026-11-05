FROM python:3.13-slim

COPY ./requirements.txt /requirements.txt
COPY ./source /app
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home whatshouldieat-user

ENV PATH="/py/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER whatshouldieat-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
