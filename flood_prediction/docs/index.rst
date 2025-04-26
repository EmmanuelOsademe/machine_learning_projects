################################
The Team Jubilee Flood Prediction Tool
################################
 
This package implements a flood risk prediction and visualization tool, designed to help assess flood risks at various geographic levels.
It combines data processing, risk estimation, and visualization functionalities to support decision-making in flood-prone areas.
 
Installation Instructions
-------------------------
 
To install the package, use the following commands:
 
.. code-block:: bash
   pip install ads-deluge-jubilee
 
For development purposes, you can clone the repository and install the dependencies:
 
.. code-block:: bash
 
   git clone https://github.com/ese-ada-lovelace-2024/ads-deluge-jubilee.git
   pip install -r requirements.txt
 
Quick Usage Guide
-----------------
 
Below is an example of how to use the package for estimating annual economic flood risks:
 
.. code-block:: python
 
   from flood_tool import Models
 
   # Initialize the models
   models = Models()
 
   # Example postcodes
   postcodes = ["SW1A 1AA", "EC1A 1BB"]
 
   # Estimate economic flood risk
   risk = models.estimate_annual_flood_economic_risk(postcodes)
   print(risk)
 
Further Documentation
---------------------
 
.. toctree::
   :maxdepth: 2
 
   data_formats
   models
   coordinates
   visualization
 
 
Function APIs
-------------
 
.. automodule:: flood_tool
   :members:
   :imported-members: