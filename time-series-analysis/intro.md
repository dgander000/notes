# Time Series Analysis

## Datasets
[PCoE Datasets](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/)   
[Condition Based Maintenance Fault Database](https://www.mfpt.org/fault-data-sets/)  
[Appliances Energy Prediction](https://www.kaggle.com/loveall/appliances-energy-prediction)   
[Vega shrink-wrapper component degradation](https://www.kaggle.com/inIT-OWL/vega-shrinkwrapper-runtofailure-data)  
[Power Laws: Detecting Anomalies in Usage](https://www.drivendata.org/competitions/52/anomaly-detection-electricity/page/102/)   
[Backblaze Hard Drive Data and Stats](https://www.backblaze.com/b2/hard-drive-test-data.html)  
[Eighty years of Canadian climate data](https://www.kaggle.com/aturner374/eighty-years-of-canadian-climate-data)  
[Melbourne Temperature Data](https://data.melbourne.vic.gov.au/Environment/Sensor-readings-with-temperature-light-humidity-ev/ez6b-syvw)     

## Courses
[Python for Time Series Data Analysis](https://www.udemy.com/course/python-for-time-series-data-analysis/)  
[Practical Time Series Analysis](https://www.coursera.org/learn/practical-time-series-analysis/home/welcome)  
[Intel Time-Series Analysis](https://software.intel.com/content/www/us/en/develop/training/course-time-series-analysis.html)
[Sequences, Time Series and Prediction](https://www.coursera.org/learn/tensorflow-sequences-time-series-and-prediction/home/welcome)    
[Advanced Machine Learning and Signal Processing](https://www.coursera.org/learn/advanced-machine-learning-signal-processing/home/welcome)   


## Youtube Videos
[Modern Time Series Analysis | SciPy 2019 Tutorial](https://www.youtube.com/watch?v=v5ijNXvlC5A)  
[Time Series Analysis with Python Intermediate | SciPy 2016 Tutorial](https://www.youtube.com/watch?v=JNfxr4BQrLk)  

## Articles
[Time Series and Date Axes in Python](https://plotly.com/python/time-series/)  

## Books

## Papers
[Multivariate Time Series Classification with WEASEL+MUSE](https://arxiv.org/pdf/1711.11343.pdf)  

## Libraries
[tsfresh](https://github.com/blue-yonder/tsfresh)  
[statsmodel](https://www.statsmodels.org/stable/index.html)  
[Time Series Data Analytics](https://github.com/patrickzib/SFA)  


## What is a time series
- According to <a href='https://en.wikipedia.org/wiki/Time_series'>wikipedia</a>, 'a time series is a series of data points indexed (or listed or graphed) in time order'.   
- Time series data is data obtained through repeated, successive measurements over time
    - Or put another way a series of data points ordered by time
- Examples include temperature, humidity, stock prices, population, heart rate, electricy consumption


## Goals of time series analysis
- Understand the underlying structure of the data such as trends, repeated patterns, variability, noise, etc
- Time series decomposition
- Extracting signals
- Anomaly detection
- Forecasting


## What makes time series different from other data
- There is an explicit ordering to the data, based on time, resulting in a dependence between observations
- Different from cross-sectional data where each observation is independent of time and each other
- Time series data comes from a process, not a population, so data points come from the same process and may not be independent of each other


## Time series basics
- Univariate time series
    - Only one variable changing over time
- Multivariat time series
    - More than one variable changing over time
- Stationary time series
    - Statistical properties sucah as mean, variance, autocorrelation do not change over time
- Non-stationary time series
    - Statistical properties sucah as mean, variance, autocorrelation do change over time
- Trend
    - Shows the general tendency, for example increasing or decreasing over time  
    - Horizontal/Stationary
    - Upward/Downward
- Seasonal component
    - Peaks and troughs occur at regular intervals
    - Repeating trend
- Cyclical component
    - Up and down movement around a trend that is not seasonal (no set repetition)
- Random component
    - Noise
- Irregularities
    - Abrupt change
- Frequency


## Cleaning time series data
- Resampling
- Outliers
- Missing data

## Filtering and Decomposition
### Hodrick-Prescott filter
- Separates a time series into a trend component and a cyclical component  
- y_t = T_t + C_t

## Exploratory Data Analysis

## Prediction and forecasting

## Classification

## Signal Estimation

## Signal Processing

## Segmentation

## Outlier Detection

## 
