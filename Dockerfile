# Docker-based environment for regenerating notebooks deterministically; see `regenerate.sh`
FROM python:3.11.8
RUN apt-get update -y \
 && apt-get install -y graphviz \
 && pip install anndata dask graphviz jupyter juq.py papermill 'zarr<3'
WORKDIR src
ENTRYPOINT [ "juq", "papermill", "run", "-iI" ]
