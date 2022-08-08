FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install pandas
RUN pip install beautifulsoup4
RUN pip install requests

WORKDIR /repo
COPY . /repo
