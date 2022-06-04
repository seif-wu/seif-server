FROM python:3.9

WORKDIR /app

# RUN pip install wheel

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

RUN flask db upgrade

CMD ["gunicorn", "manage:app", "-c", "./gunicorn.conf.py"]
