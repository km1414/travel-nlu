FROM python:3.7
RUN pip install -U pip
RUN addgroup --gid 1000 nlu && adduser --uid 1000 --ingroup nlu --shell /bin/sh --disabled-password --gecos '' --home /home/nlu nlu
USER nlu
WORKDIR /home/nlu
COPY --chown=nlu:nlu requirements.txt requirements.txt
RUN pip install --user -r requirements.txt
RUN python -m spacy download --user en_core_web_md
RUN python -m spacy link en_core_web_md en
ENV PATH="/home/nlu/.local/bin:${PATH}"
COPY --chown=nlu:nlu . app
WORKDIR app
CMD rasa shell nlu
