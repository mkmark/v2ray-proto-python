# v2ray_proto

generate pb2.py of v2ray/xray proto for use in python

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
```

## manual fix

for xray, two places need manual fix

`from core import config_pb2 as core_dot_config__pb2` to `from xray_proto.core import config_pb2 as core_dot_config__pb2`

`importlib.import_module('transport.global.config_pb2')` to `importlib.import_module('xray_proto.transport.global.config_pb2')`
