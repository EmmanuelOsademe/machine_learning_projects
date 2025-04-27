#!/usr/bin/env python

from setuptools import setup


setup(
    name="Flood Tool",
    version="0.5",
    description="Flood Risk Analysis Tool",
    author="ACDS Project Team Jubilee"
    packages=["flood_tool"],
    install_requires=[
        "matplotlib",
        "numpy",
        "pandas",
        "folium",
        "scikit-learn",
        "xgboost",
        "streamlit_extras",
        "streamlit_folium",
        "streamlit",
        "plotly.express",
        "scipy",
        "imblearn",
        "ipywidgets",
        "seaborn",
        "geojson",
        "folium.plugins",
        "pytest",
        "pytest-cov",
        "pytest-timeout",
    ]
)
