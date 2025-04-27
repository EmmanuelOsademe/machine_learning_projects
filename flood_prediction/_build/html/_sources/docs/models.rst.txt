====================================
Regression and Classification models
====================================

Risk Class Prediction Models
============================

All Zero Risk
-------------

This model assumes all unlabeled flood risk data is near zero risk (band 1, the modal class), which is the modal class for the data set, which is strongly unbalanced. This is a baseline model to compare against. While it achieve a moderately good accuracy, it is not a useful model for risk prediction, and has little skill.

Risk Label Prediction Model 
---------------------------

The risk label classification task required identifying correlations among attributes to determine their relevance. All attributes, except those predicted in other tasks, were retained for further training. Wide-range features, such as elevation and distance to watercourses, underwent log transformations in the pipeline to standardize their scales.

Given the imbalanced nature of the dataset, particularly for underrepresented risk labels (e.g., labels 6 and 7), oversampling techniques like SMOTE and ADASYN were applied. SMOTE interpolates new samples, while ADASYN focuses on challenging, sparse areas. Class weights were computed to balance the attention paid to all samples, and model parameters, including `eval_metric='mlogloss'`, were fine-tuned for multi-class classification using XGBoost.

The XGBoost model achieved a higher recall for underrepresented classes and better overall weighted recall compared to Random Forest. This superior performance can be attributed to XGBoost's ability to capture complex global feature interactions during tree building and its use of the Softmax function for more accurate decision boundaries. In contrast, Random Forest relies on random sampling and majority voting, which are less effective for multi-class tasks. These enhancements made XGBoost the optimal choice for this classification problem.  


House Price Prediction Models
=============================

All England median
------------------

This model assumes all unlabeled house price data is the median house price for England. This is a baseline model to compare against. While it achieve a moderately good accuracy, it is not a useful model for risk prediction, and has little skill.

Median House Price Prediction Model
-----------------------------------

Predicting median house prices proved to be highly challenging, with all tested models performing poorly. The normalized root mean squared error (NRMSE) of 1.427 indicates that the model's average prediction error surpasses the natural variability of the observed data, reflecting extreme underperformance. 

Key issues stem from the dataset’s features, which, while contextually relevant (e.g., elevation and proximity to watercourses), lack general applicability to median price prediction. Additionally, the impact of features such as households and headcounts was minimal or detrimental, likely influenced by factors like London's Affordable Homes Programme, which altered population dynamics in affluent areas. Despite preprocessing steps like robust scaling, these features failed to enhance the model’s accuracy.

Testing was primarily limited to Random Forest and XGBoost regressors due to computational constraints. XGBoost consistently outperformed Random Forest, as its boosting approach adapts better to low-quality features by refining errors across iterations. In contrast, Random Forest treats all features equally, making it less suitable for this dataset. Key predictors identified through permutation importance—elevation and distance to watercourses—highlight the role of locational attributes in pricing, though their contribution remains insufficient to achieve meaningful accuracy.

Overall, the model’s performance underscores the limitations of the dataset and the inherent difficulty of median house price prediction with the given features. While XGBoost showed marginally better results, significant improvements would require a more robust feature set.  


Historical Flooding Prediction Model
====================================

For the prediction of historical flooding, we retained all attributes except those designated for prediction in other tasks, as correlation analysis revealed their importance for the target variable, `historicalFlooding`. To address the wide range of values in features such as elevation and distance to watercourses, log transformations were applied during preprocessing.

Given the imbalance in the `historicalFlooding` dataset, oversampling techniques were employed to enhance recall and F1-score. Both SMOTE and SMOTEENN were tested, with SMOTE yielding superior results by generating synthetic samples without excessive noise removal. Random Forest, combined with SMOTE, achieved the highest performance, improving recall and F1-score by 2% over XGBoost. The model’s success is attributed to its balanced treatment of feature values. However, Random Forest incurred higher computational costs compared to XGBoost, which benefits from efficient parallel processing and limited tree depth. Ultimately, Random Forest with SMOTE was selected for its superior experimental performance.  


Predicting Local Authority 
==========================

For predicting local authorities, we used **Random Forest** and **XGBoost** for their scalability and efficiency with large datasets. Other models like KNN and SVM were excluded due to higher computational costs and inefficiencies with large-scale data.

Methodology
-----------

1. **Classification**:
   - Metrics: `mlogloss` (calibrates probabilities) and `merror` (tracks misclassifications).  
   - XGBoost outperformed Random Forest due to better handling of complex class boundaries and imbalanced data.

2. **Regression**:
   - Techniques: **SMOTE** and **ADASYN** were applied to balance training data.  
   - Metrics: **RMSE** and **R²** for model evaluation.  

XGBoost consistently showed better accuracy and model fit, making it the preferred choice for both classification and regression tasks.

