import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from info_helper import InformationHelper

class NutrientGrapher:

    def __init__(self):
        self.info_helper = InformationHelper()

    def plot_nutrient_graph(self, data):
        df = pd.DataFrame(data)
        # Create subplot with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Add trace for macronutrients
        fig.add_trace(
            go.Bar(
                x=df[df["Type"] == "Macro"]["Nutrient"],
                y=df[df["Type"] == "Macro"]["Amount"],
                name="Macronutrients",
                marker_color="royalblue",
            ),
            secondary_y=False,
        )

        # Add trace for micronutrients
        fig.add_trace(
            go.Bar(
                x=df[df["Type"] == "Micro"]["Nutrient"],
                y=df[df["Type"] == "Micro"]["Daily Value"],
                name="Micronutrients",
                marker_color="lightgreen",
            ),
            secondary_y=True,
        )

        # Add horizontal line at 100% DV for micronutrients
        fig.add_hline(y=100, line_dash="dot", line_color="red", secondary_y=True)

        # Customize layout
        fig.update_layout(
            title_text="Daily Nutrient Intake",
            xaxis_title="Nutrients",
            barmode="group",
            legend_title="Nutrient Type",
        )

        # Set y-axes titles
        fig.update_yaxes(title_text="Amount (g)", secondary_y=False)
        fig.update_yaxes(title_text="% Daily Value", secondary_y=True)

        # Display the chart in Streamlit
        st.plotly_chart(fig)

        # Display data table
        st.subheader("Nutrient Data")
        st.dataframe(df)
