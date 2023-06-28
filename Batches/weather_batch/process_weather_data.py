import logging
import sys

from rc_common import get_zeros, write_dataframe

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def __batch_main__(sub_job_name, scheduled_time, runtime, part_num, num_parts, job_config, rundate, *args):
    logging.info(f"{sub_job_name=}")
    logging.info(f"{scheduled_time=}")
    logging.info(f"{runtime=}")
    logging.info(f"{part_num=}")
    logging.info(f"{num_parts=}")
    logging.info(f"{job_config=}")
    logging.info(f"{rundate=}")

    forecast = args[0]
    temperature = forecast["temperature"].to_dict()
    humidity = forecast["relativeHumidity.value"].to_dict()
    logging.info("Temperature forecast")
    logging.info("-" * 100)
    for k, v in temperature.items():
        logging.info(f"{k: < 3}: {'*' * int(v)}")
    logging.info("-" * 100)

    logging.info("Humidity forecast")
    logging.info("-" * 100)
    for k, v in humidity.items():
        logging.info(f"{k: < 3}: {'*' * int(v)}")
    logging.info(f"Here are 7 zeros: {get_zeros(7)}")

    write_dataframe(forecast, "forecast")


if __name__ == "__main__":
    from get_weather_data import __batch_main__ as get_data

    params = [None] * 6
    __batch_main__(*params, get_data(*params))
