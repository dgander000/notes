# Time Series Analysis

## Learning Checklist
- [x] Define a time series
- [x] Motivation for time series analysis
- [x] What are the components of a time series 
- [] Time series decomposition
- [] What is stationarity
- [] How to test if a time series is stationary
- [] How to make a time series stationary
- [] What is autocorrelation
- [] What is lag
- [] What is cross Correlation
- [] How to de-trend a time series
- [] How to de-seasonalize a time series



## Datasets
[PCoE Datasets](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/)   
[Condition Based Maintenance Fault Database](https://www.mfpt.org/fault-data-sets/)  
[Appliances Energy Prediction](https://www.kaggle.com/loveall/appliances-energy-prediction)   
[Vega shrink-wrapper component degradation](https://www.kaggle.com/inIT-OWL/vega-shrinkwrapper-runtofailure-data)  
[Power Laws: Detecting Anomalies in Usage](https://www.drivendata.org/competitions/52/anomaly-detection-electricity/page/102/)   
[Backblaze Hard Drive Data and Stats](https://www.backblaze.com/b2/hard-drive-test-data.html)  
[Eighty years of Canadian climate data](https://www.kaggle.com/aturner374/eighty-years-of-canadian-climate-data)  
[Melbourne Temperature Data](https://data.melbourne.vic.gov.au/Environment/Sensor-readings-with-temperature-light-humidity-ev/ez6b-syvw)     
[INGV - Volcanic Eruption Prediction](https://www.kaggle.com/c/predict-volcanic-eruptions-ingv-oe)  

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
- Time series data is data obtained through repeated, successive measurements over time (equally spaced points)  
    - Or put another way a series of data points ordered by time
- Examples include temperature, humidity, stock prices, population, heart rate, electricy consumption


## Motivation for time series analysis
- Understand the underlying generative process 
- Understand the underlying structure of the data such as trends, repeated patterns, variability, noise, etc
- Time series decomposition
- Extracting signals
- Anomaly detection
- Forecasting


## What makes time series different from other data
- There is an explicit ordering to the data, based on time, resulting in a dependence between observations
- Different from cross-sectional data where each observation is independent of time and each other
- Time series data comes from a process, not a population, so data points come from the same process and may not be independent of each other


## Time series types
- Univariate time series
    - Only one variable changing over time
- Multivariate time series
    - More than one variable changing over time


## Time series components
- Trend
    - Shows the general tendency
        - increasing, decreasing or constant over time  
        - Horizontal/Stationary
        - Upward/Downward
    - Stationary time series
        - Statistical properties sucah as mean, variance, autocorrelation do not change over time
    - Non-stationary time series
        - Statistical properties sucah as mean, variance, autocorrelation do change over time
- Seasonality component
    - Peaks and troughs occur at regular intervals
    - Periodic behavior resulting in a repeating trend
- Residual component
    - Random fluctuations or noise left over when trend and seasonality are removed
    - Could be random or part of the trend or seasonality components missed during decomposition


## Other time series components
- Cyclical component
    - Up and down movement around a trend that is not seasonal (no set repetition)
- Irregularities
    - Abrupt change


## Time series decomposition
- Moving average smoothing
    - Simple moving average
    - Weighted moving average
- Exponential smoothing
- Hodrick-Prescott filter
    - Separates a time series into a trend component and a cyclical component  
    - y_t = T_t + C_t
- Decomposition models
    - Additive decomposition
        - Assumes time series is the sum of its components
        - Observation = Trend + Seasonality + Residual
    - Multiplicative decomposition
        - Assumes time series is the product of its components
        - Observation = Trend * Seasonality * Residual
        - Can transform multiplicative model to an additive model by applying a log transfom
            - log(Time * Seasonality * Residual) = log(Time) + log(Seasonality) + log(Residual)
    - Pseudoadditive decomposition
    - Seasonal and Trend decomposition using Loess (STL)
- Frequency based methods


## Autocorrelation
- The correlation between a measurement at two different times
- Lag - time interval between the values
- Autocorrelation typically results in a pattern, without autocorrelation looks random


## Stationarity
- Constant mean (no trend)
- Constant variance (no heteroscedasticity)
- No periodicity (no seasonality)
- Constant autocorrelation
    - If autocorrelation is constant through the series then autocorrelation can be removed with a simple transformation
- Many time series forecasting models assume stationarity
- 


## Cleaning time series data
- Resampling
- Outliers
- Missing data


## Exploratory Data Analysis

## Prediction and forecasting

## Classification

## Signal Estimation

## Signal Processing

## Segmentation

## Outlier Detection

## 
