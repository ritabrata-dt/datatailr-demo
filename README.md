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

## Entrypoints

Every Datatailr runnable requires an entrypoint. Entrypoint is basically a function with a signature, specific for a runnable type. It points to a location or a function in a package/batch/app/service that serves as the starting point for executing code. 

## Apps
App entrypoint function: `__app_main__`.
An app can be ran locally using:
```
python app.py 12345
```
Where `app.py` is your app, and `12345` is a port. You can use any free port instead of `12345`.  
After executing the command, an app should be launched in a new browser window. There is no need to repeat this step - any changes in the source file will be visible within an app after a page refresh.
### Hello World app
Simple Streamlit app that prints `Hello World!`. 
### Weather app
Another Streamlit app that reads and plots weather data using matplotlib and plotly.  

## Batches
Batch entrypoint function: `__batch_main__`.
Any code inside the `__batch_main__` function will be executed during the batch run. There can only be one of these functions per file. For an additional job definition a new file should be created.
### get_weather_data
Example of a batch job that downloads weather data from the web.  
### process_weather_data 
Example of a batch job that processes and saves weather data.

## Excel addins
Excel entrypoint function: `__excel_main__`.
### simple_addin  
Example of a simple excel addin that can do basic math operations.
### pca_addin
Example of an excel addin that can generate random data and calculate PCA.

## Packages
### rc_common package
Example of a package which can read/write data from/to a blob storage.

## SDLC
All jobs should be deployed from the Job Scheduler application.  
### programmatical_batch_job
Example of how to create a batch job programmatically, without using the GUI.

## Services
Service entrypoint function: `__service_main__`.
## service
Example of a simple Streamlit service that prints `Hello World!`.
