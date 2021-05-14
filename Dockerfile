FROM python

COPY . /dir
WORKDIR /dir

CMD python code.py