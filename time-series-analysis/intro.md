# Time Series Analysis

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
- Cyclical component
    - Up and down movement around a trend that is not seasonal
- Seasonal component
    - Peaks and troughs occur at regular intervals
- Random component
    - Noise
- Irregularities
    - Abrupt change
- Frequency


## Cleaning time series data
- Resampling
- Outliers
- Missing data

