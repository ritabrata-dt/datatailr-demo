import logging
import sys

import pandas
import requests

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def __batch_main__(
        sub_job_name, scheduled_time, runtime, part_num, num_parts, job_config, rundate, *args) -> int :
    logging.info(f"{sub_job_name=}")
    logging.info(f"{scheduled_time=}")
    logging.info(f"{runtime=}")
    logging.info(f"{part_num=}")
    logging.info(f"{num_parts=}")
    logging.info(f"{job_config=}")
    logging.info(f"{rundate=}")
    url = "https://api.weather.gov/gridpoints/TOP/31,80/forecast"
    req = requests.get(url)
    data = req.json()
    forecast = pandas.json_normalize(data["properties"]["periods"])
    start, end = forecast["startTime"].min(), forecast["endTime"].max()
    logging.info(f"Got forecast for {len(forecast)} periods starting at {start} and ending at {end}")
    return forecast



def __app_main__(




        ) -> int:
    return create_app().application


def __service_main__(port
    ) -> None:
        app.run('0.0.0.0', port=int(port), debug=False)




