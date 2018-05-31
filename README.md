# Project SalmonSpy

### Background:
Salmon return to Bristol Bay, Alaska every summer to spawn.  The exact timing and magnitude of the salmon run is unknown, but predictions are made by ADFG at the start of every year.  The goal of this project is the develop a more accurate prediction of the Bristol Bay salmon run then what's currently provided by ADFG.

### Work Items:
1. Data fetch/scrape
    1. historical salmon catches = 'http://www.adfg.alaska.gov/index.cfm?adfg=commercialbyareabristolbay.harvestsummary'
    1. historical salmon counts (what escapes upriver) = 'http://www.adfg.alaska.gov/index.cfm?adfg=commercialbyareabristolbay.salmon#fishcounts'
    1. historical salmon catches in "test" fishery = 'https://www.bbsri.org/'
    1. stream and lake levels = 'https://waterdata.usgs.gov'
    1. tide activity = 'http://kapadia.github.io/usgs/reference/api.html'
    1. weather activity = 'https://www.wunderground.com/weather/api/d/docs?d=data/history'
    1. fishing boat activity = 'http://globalfishingwatch.org/'
    
1. Data clean and transform
    1. Verify data integrity
    1. Standardize column names
    1. Convert all files to CSV
    
1. AWS setup
    1. Spin up micro EC2
    1. Create an S3 bucket
    1. Setup Sagemaker
    
1. Train the model
    1. Use built-in algorithms with Sagemaker
    2. Pre-process with Jupyter
    
1. Evaluate the model
    
