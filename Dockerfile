FROM eu.gcr.io/b2w-master/b2w-python:dev AS compile-image
COPY . .

RUN pip-compile
RUN pip-sync

FROM python:3.9-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev 
COPY --from=compile-image /python_app /python_app
ENV PATH="/python_app/venv/bin:$PATH"

WORKDIR /python_app
EXPOSE 80
