# Project SalmonSpy

### Background:
Salmon return to Bristol Bay, Alaska every summer to spawn.  The exact timing and magnitude of the salmon run is unknown, but predictions are made by ADFG at the start of every year.  The goal of this project is the develop a more accurate prediction of the Bristol Bay salmon run then what's currently provided by ADFG.

### Work Items:
1. Data fetch/scrape
    1. fishing boat activity = 'http://globalfishingwatch.org/'
    * Docs and SDK = https://github.com/GlobalFishingWatch?language=python
    * More technical docs: https://github.com/GlobalFishingWatch/paper-global-footprint-of-fisheries/blob/master/data_documentation/fishing_effort.md
    1. historical salmon catches = 'http://www.adfg.alaska.gov/index.cfm?adfg=commercialbyareabristolbay.harvestsummary'
    1. historical salmon counts (what escapes upriver) = 'http://www.adfg.alaska.gov/index.cfm?adfg=commercialbyareabristolbay.salmon#fishcounts'
    1. historical salmon catches in "test" fishery = 'https://www.bbsri.org/'
    1. stream and lake levels = 'https://waterdata.usgs.gov'
    1. tide activity = 'http://kapadia.github.io/usgs/reference/api.html'
    1. land weather = 'https://graphical.weather.gov/xml/'
    1. marine weather = https://www.ncdc.noaa.gov/data-access/marineocean-data
    1. more marina data to checkou = https://www.ncdc.noaa.gov/cdo-web/datasets
    1. NOAA web data services guide = https://www.ndbc.noaa.gov/docs/ndbc_web_data_guide.pdf
    1. tides & currents = https://opendap.co-ops.nos.noaa.gov/

##### Station IDs
    Port Moller         9463502
    Adak Island         9461380
    Unalaska            9462620
    St Paul Island      9464212 
    > more here:    https://opendap.co-ops.nos.noaa.gov/stations/index.jsp
   
    
    
    
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
    
