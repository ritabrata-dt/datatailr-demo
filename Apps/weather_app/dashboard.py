import sys

import dt.streamlit
import dt.user
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
from dt.cloud.blob_storage import get_blob_store, load_dataframe


def main():
    st.set_page_config(page_title="Weather data forecast", page_icon="🏠")
    st.markdown("# Weather data")
    st.sidebar.title("Parameters")

    scale_selector = st.sidebar.slider("Scaling", 1, 10, 1)
    units_selector = st.sidebar.radio("Temperature units", ["Celsisus", "Fahrenheit"], index=0)

    data = pd.read_parquet(load_dataframe("forecast"))
    data = data[["startTime", "temperature", "relativeHumidity.value"]].set_index("startTime")

    data["temperature"] = data["temperature"] * scale_selector

    if units_selector == "Fahrenheit":
        data["temperature"] = data["temperature"] * 9 / 5 + 32

    st.markdown("## Matplotlib")
    fig, ax = plt.subplots()
    data.plot(ax=ax, rot=45)
    st.pyplot(fig)

    st.markdown("## Plotly")
    fig = px.scatter(data, x="relativeHumidity.value", y="temperature", log_y=True)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    latest_update_time = max([ob.last_modified for ob in get_blob_store().list_objects() if ob.name == "forecast"])
    st.markdown(f"### Last update time: {latest_update_time}")


application = dt.streamlit.Streamlit()


def __app_main__():
    return application


if __name__ == "__main__":
    application.run(port=int(sys.argv[1]))
