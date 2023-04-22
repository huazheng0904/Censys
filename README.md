## Overview
This tool is developed with python3 and dandas, matplotlib. 
please make sure all required software and libraries are installed before running the tool


## Prerequisites

1. Install python 3
2. Install pandas 

```bash
pip install pandas
```
3. Install matplotlib
```bash
pip install matplotlib
```


## Usage


```python
python main.py
```
The log will show the number of processed of file, the destination of processed result. the sample log looks like:

```
Start reading CSV files....
7  files are imported!
Invalid rows detected and saved to invalid_event_type.cvs
The statics number of each event type per device_id is saved to event_type_agg_by_device_id.cvs
Histogram data for the counts of squirrel event_type is saved to histogram_squirrel.pdf
```



## Thoughts on further development

1 To increase flexibility, it is recommended to extract the currently hard-coded parameters, 
    such as valid event types, bin size, input/output files, and other parameters, and make them configurable.
    
2 Automation
    Is there a way to automate the tool and integrate it with an existing scheduler to run automatically?
    
3 Observability 
    Observability is important to gain insights into the input data's quality, quantity, 
and other essential metrics. 
Having a dashboard to provide information on the number of files processed and the time it takes would be helpful. 
Additionally, alerts can be set up to detect anomalous data and exceptions.
                 
    

