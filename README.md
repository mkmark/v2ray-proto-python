# v2ray_proto

generate pb2.py of v2ray proto for use in python

## usage

```sh
pip install .
```

## regenerate

```sh
conda env create -p ./env -f ./environment.yml
conda activate ./env
git submodule init
git submodule update
rm -r v2ray_proto
python gen.py
pip install .
```
