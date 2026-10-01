# Month 2 – Week 2: Exploratory Data Analysis and Data Visualization

## Topics Covered

* Exploratory Data Analysis (EDA)
* Data quality inspection
* Data types and categorical variables
* Missing-value analysis and imputation
* MCAR, MAR, and MNAR
* Distribution analysis
* Skewness and transformations
* Outlier detection
* IQR and Z-score methods
* Correlation analysis
* Pearson and Spearman correlation
* Categorical analysis
* Rare-category handling
* Data visualization
* Visualization storytelling
* Data leakage
* Train/test splitting
* Feature engineering
* Categorical encoding
* Feature scaling
* ML-ready data preparation
* Reproducible preprocessing pipelines
* Train-serve skew

## Assignment

### Ames Housing Dataset — EDA and Data Visualization

Performed a complete exploratory data analysis and preprocessing workflow using the Ames Housing dataset.

The assignment covered the analysis of `SalePrice` and other housing features, identification of data-quality issues, visualization of important relationships, and preparation of the dataset for machine learning.

## Main Tasks

### Part A — First Look and Data Quality

* Inspected the dataset structure and dimensions.
* Checked column names, data types, summary statistics, and unique values.
* Identified categorical and numerical variables.
* Checked duplicate rows and near-constant columns.
* Investigated suspicious and impossible values.
* Reviewed columns whose stored data type did not match their actual meaning.

### Part B — Missing Values

* Performed a missing-value audit.
* Investigated the meaning of missing values for different features.
* Distinguished between genuinely missing values and values representing the absence of a feature.
* Studied MCAR, MAR, and MNAR.
* Compared different imputation strategies.
* Investigated `LotFrontage` missingness and used neighborhood information for imputation.
* Created missingness indicators where appropriate.

### Part C — Distributions, Outliers and Transformations

* Analyzed the distribution of `SalePrice`.
* Compared mean, median, minimum, maximum, and skewness.
* Applied log transformation to the target.
* Investigated skewed numerical features.
* Detected outliers using IQR and Z-score methods.
* Investigated unusual observations in important variables.
* Compared the effect of outliers on correlations.
* Applied appropriate transformations and capping decisions.

### Part D — Relationships and Correlation

* Analyzed categorical feature frequencies.
* Identified rare categories.
* Compared `SalePrice` across important categorical and ordinal variables.
* Created correlation visualizations.
* Identified features strongly correlated with `SalePrice`.
* Compared Pearson and Spearman correlations.
* Investigated highly correlated feature pairs.
* Examined possible feature redundancy.

### Part E — Visualization and Storytelling

* Created time-based features using `YrSold` and `MoSold`.
* Analyzed sales volume and median sale prices over time.
* Used rolling statistics to identify trends.
* Investigated seasonal patterns.
* Created and improved visualizations using appropriate chart-design principles.
* Developed a data story explaining important factors related to `SalePrice`.

### Part F — Making the Dataset ML-Ready

#### F1 — Split First

* Started from the raw dataset.
* Applied only row-independent preprocessing before splitting.
* Split the data into 80% training and 20% test sets.
* Used `random_state=42`.
* Obtained:

  * 1,168 training rows
  * 292 test rows
* Avoided data leakage by learning preprocessing statistics from the training data only.

#### F2 — Imputation and Outlier Handling

* Imputed missing values using training-set information.
* Applied appropriate fallback strategies.
* Handled remaining missing values.
* Learned outlier-capping limits from training data.
* Applied the same learned preprocessing rules to the test data.

#### F3 — Feature Engineering

Created additional features such as:

* `TotalSF`
* `HouseAge`
* `YearsSinceRemodel`
* `TotalBathrooms`
* `HasGarage`
* `HasPool`
* `HasFireplace`
* `Has2ndFloor`

Compared engineered features with their original features using their relationships with the target.

#### F4 — Encoding Categorical Variables

* Ordinal-encoded quality-related variables.
* Encoded `CentralAir`.
* Grouped rare categories.
* One-hot encoded nominal categorical variables.
* Ensured training and test datasets had aligned columns.

#### F5 — Transformation, Scaling and Saving

* Applied `log1p` transformations to selected skewed features.
* Standardized continuous numerical features using training-set statistics.
* Kept binary indicators and the target appropriately unscaled.
* Compared feature distributions before and after transformation.
* Saved the prepared training and test datasets.
* Verified that the final datasets contained numeric values and no missing values.
* Created a data-preparation log.

## Part G — Written Questions

Answered questions related to:

* Data leakage before train/test splitting.
* Why the test set should represent unseen data.
* Preprocessing steps that depend on the model.
* Information available at prediction time.
* Assumptions behind `LotFrontage` imputation.
* Mean versus median imputation.
* How visualizations influenced preprocessing decisions.
* Preprocessing decisions that require further validation.

## Bonus

### Reproducible Preparation Pipeline

Created a reproducible preprocessing workflow that:

* Takes the raw training data.
* Performs the required preprocessing steps.
* Learns preprocessing values only from training data.
* Produces prepared training and test datasets.
* Produces consistent results when executed again.

### Train-Serve Skew

Compared the real test dataset with the training dataset to identify differences such as:

* Missing values appearing at prediction time.
* Categories present in the test data but not seen during training.
* How the preprocessing workflow handles these differences.

## How to Run

Make sure you are inside the **Month 2 – Week 2** assignment folder.

Open the notebook using Jupyter:

```bash
jupyter notebook assignment2.ipynb
```

Or open `assignment2.ipynb` directly in VS Code and run the cells in order.

Make sure the required dataset files are available in the expected location before running the notebook.

## What I Learned

During Month 2 – Week 2, I learned how to perform a complete Exploratory Data Analysis workflow on a real-world dataset.

I practiced inspecting data quality, handling missing values, understanding distributions, detecting outliers, analyzing categorical variables, and studying relationships between features and the target variable.

I learned how transformations, encoding, feature engineering, and scaling can prepare raw data for machine learning.

One of the most important concepts I learned was data leakage. Preprocessing statistics and decisions that depend on the data should be learned from the training set and then applied to the test set.

I also learned how visualization can help identify patterns, unusual observations, relationships, and problems in a dataset before building a machine-learning model.

## Challenges Faced

One challenge was determining whether a missing value represented unknown information or the absence of a feature. This required understanding the meaning of individual variables before choosing an imputation strategy.

Another challenge was handling skewed features and outliers because different situations require different approaches such as transformation, capping, or creating indicator variables.

Understanding data leakage was also challenging. I learned that even calculating statistics such as medians, category frequencies, scaling parameters, or outlier limits using the complete dataset can allow information from the test set to influence the training process.

Another challenge was preparing categorical variables because ordinal and nominal categories require different encoding techniques.

Finally, building the ML-ready preprocessing workflow required ensuring that the same rules learned from the training data were consistently applied to the test data.
