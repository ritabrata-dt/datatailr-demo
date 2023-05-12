# Quickstart guide

The repo includes demos for different runnables that can be used on the Datatailr platform.  

To start launching runnables from this repo or developing your own, follow these steps:
1. Clone this repo in your home directory:
    ```
    cd /home/username
    git clone git@bitbucket.org:datatailr/datatailr-demo.git
    ```
2. Open the repo directory in the IDE. Launch a terminal and run:
    ```
    pip install -r requirements.txt
    ```

## Apps
A Streamlit app can be ran locally using:
```
python Apps/hello_world_app.py 12345
```
You can use any free port instead of `12345`.  
An app should be launched in a new browser window. There is no need to repeat this step - any changes in the source file will be visible within an app after a page refresh.
### Hello World app
Simple Streamlit app that prints `"Hello World!"`. 
### Weather app
Another Streamlit app that reads and plots weather data using matplotlib and plotly.  

## Batches
Any code inside the `__batch_main__` function will be executed during the batch run. There can only be one of these functions per file. For an additional job definition a new file should be created.
### get_weather_data
Example of a batch job that downloads weather data from the web.  
### process_weather_data 
Example of a batch job that processes and saves weather data.

## Excel add-ins
### excel_addin  
An example of an excel add-in will be introduced shortly.

## Packages
### rc_common package
Example of a package which can read/write data from/to a blob storage.

## SDLC
All jobs should be deployed from the job-scheduler application.  
### programmatical_batch_job
Example of how to create a batch job programmatically, without using the GUI.

## Services
Example of a simple Streamlit service that prints `"Hello World!"`.
