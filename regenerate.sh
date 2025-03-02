#!/usr/bin/env bash
# Deterministically regenerate notebooks in this directory:
# ```bash
# ./regenerate.sh anndata_dask_array  # Regenerate a single notebook
# ./regenerate.sh                     # Regenerate all notebooks
# ```

set -eo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

name=anndata-notebooks
docker build -t $name .

if [ $# -eq 0 ]; then
    set -- *.ipynb
fi

for nb in "$@"; do
    nb="${nb%.ipynb}.ipynb"
    echo "Executing nb: $nb" >&2
    docker run -i --rm "--name=$name" -v "$PWD:/src" "$name" "$nb"
done
