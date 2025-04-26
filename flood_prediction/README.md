# Project Title

**The Deluge** - Predicting Flood Risk in the UK

## Project Overview

This project develops a series of machine learning models to analyze and predict outcomes related to flood risk, historical flooding, property prices, and local authority classifications in the UK. By leveraging geographic, environmental, and socioeconomic data, the models provide actionable insights for urban planning, emergency preparedness, real estate evaluation, and policymaking.

---

## Key Features

1. **Flood Risk Model**  
   Predicts the likelihood of flooding in specific postcode areas.

2. **Historical Flooding Model**  
   Identifies locations with a history of flooding based on environmental and historical data.

3. **House Price Prediction Model**  
   Estimates median property values based on geographic and environmental attributes.

4. **Risk Label Classification Model**  
   Classifies risk labels for UK regions based on environmental and socioeconomic features.

---

## Data Description

- **Source**: The dataset includes geographic, environmental, and socioeconomic data related to UK postcodes.

- **Key Columns**:
  - `elevation`: Elevation of the area.
  - `distanceToWatercourse`: Distance from properties to water bodies.
  - `medianPrice`: Median property prices by postcode.
  - `nearestWatercourse`: Closest water body to the area.
  - Categorical features, including local authority identifiers and postcode details.

- **Preprocessing**:
  - Log transformations for skewed numerical features.
  - Robust scaling to address outliers in population-related data.
  - Oversampling using SMOTE and ADASYN for imbalanced classification tasks.

---

## Pipeline Architecture

### Data Preprocessing
- Log transformations for specific features (e.g., elevation, distanceToWatercourse).
- Scaling and encoding pipelines for numerical and categorical data.
- Handling class imbalance with oversampling techniques.

### Model Training
- **Flood Risk**: Random Forest for binary classification tasks.
- **Historical Flooding**: Logistic Regression for binary outcomes.
- **House Price Prediction**: XGBoost Regressor for property value estimation.
- **Risk Label Classification**: XGBoost for multi-class classification tasks.

### Model Evaluation
- Negative Root Mean Squared Error (NRMSE) for regression tasks.
- Recall and weighted recall metrics for imbalanced classification tasks.

---
## Project Organisation

| Path                                   | Description                                                                                                                                                              |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Root/flood_tool/models.py              | This script contains the Models class. This contains methods which return pipelines for all the ML models used in our project. It also contains helper methods, that are used in the preprocessing pipelines that are a component of the model pipelines. |
| Root/flood_tool/tool.py                | This file contains most of the starter code. We implemented methods in the Tools class including the imputer, the fitting method and the different prediction methods. It also contains helper methods for smaller tasks for example normalising UK postcodes. |
| Root/dev/EDA.ipynb                     | This contains a lot of the graphs that are part of the EDA which guided the design of ML model preprocessing pipelines.                                                  |
| Root/dev/[task notebooks]              | The models in the Models class (integrated into the Tools class) are not our best-performing ones due to integration issues. Therefore, we provide notebooks with our top-performing models. |
| Root/Home.py                           | Main script implementing Streamlit dashboard.                                                                                                                           |
| Root/notebooks/Data Visualization.ipynb | Additional visualization maps (not using Streamlit).                                                                                                                    |
| Root/flood_tool/common/utils_visualization.py | Helper function for the Streamlit page.                                                                                                                           |

## Dependencies

To replicate or run the project, install the following dependencies:

- `numpy`
- `scipy`
- `pandas`
- `folium`
- `scikit-learn`
- `matplotlib`
- `xgboost`
- `imblearn`
- `ipywidgets`
- `seaborn`
- `geojson`
- `streamlit_extras`
- `folium.plugins`
- `streamlit_folium`
- `plotly.express`

Install all dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/ese-ada-lovelace-2024/ads-deluge-jubilee.git
   cd ads-deluge-jubilee
   ```

2. Prepare the dataset:
   - Place the labeled data in `resources/postcodes_labelled.csv`.

3. Run the preprocessing pipeline:

   ```python
   from models import Models
   model_instance = Models()
   preprocessed_data = model_instance.preprocessor.transform(data)
   ```

4. Train and evaluate models:

   ```python
   flood_model = model_instance.flood_risk_model()
   flood_model.fit(X_train, y_train)
   ```
5. To launch the streamlit visualization
   
   ```python
   $ streamlit run Home.py
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contact

For inquiries, contact any of the Team Jubilee members via mail:

- [miles.weberman24@imperial.ac.uk]
- [julia.metz24@imperial.ac.uk]
- [david.mamane24@imperial.ac.uk]
- [precious.okon24@imperial.ac.uk]
- [yixuan.yan24@imperial.ac.uk]
- [haoran.sun24@imperial.ac.uk]
- [yiyu.yang24@imperial.ac.uk]
- [yixuan.yan24@imperial.ac.uk]

 or visit the project repository:
 [https://github.com/ese-ada-lovelace-2024/ads-deluge-jubilee].
