import streamlit as st
import numpy as np
import pandas as pd
import dt.streamlit
import plotly.express as px


@st.cache_data
def generate_dataframe():
    # Generate random data
    data = np.random.randn(100, 8)
    columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7', 'Column 8']
    
    # Create a DataFrame
    dframe = pd.DataFrame(data, columns=columns)
    return dframe


def plot_column(data, column):
    plot = px.line(data, x=data.index, y=column, title=f"Plot of {column}")
    st.plotly_chart(plot, use_container_width=True)
    return


def main():
    st.title("Data generation and visualization")
    st.markdown("This simple app can generate sample data and visualize it column by column")
    df = generate_dataframe()
    if st.button("Regenerate DataFrame"):
        st.cache_data.clear()
        st.experimental_rerun()
    st.dataframe(df, use_container_width=True)
    col_to_plot = st.selectbox('Column to plot', df.columns.tolist(), key='col-to-plot')
    plot_column(df, col_to_plot)

    
application = dt.streamlit.Streamlit()

def __app_main__():
    return application

if __name__ == '__main__':
    application.run(port=int(sys.argv[1]))