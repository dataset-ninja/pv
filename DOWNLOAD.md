Dataset **PV** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/o/M/iG/UG1cNN0qpiEREfCWDfeUFUTLZIZrhnowclhQTC9CsvvoBjiwzs5t2Ip3CfroRV4pOY0G7QTrGbYI8f7vbvp5ha0mA6qGeUIOPIBOmybXBw7trPK16q114ZNeYhvK.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PV', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

