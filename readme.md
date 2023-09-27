# Bike Sharing Demand Prediction

## Background

Bike sharing systems represent a new generation of bike rentals where the entire process, from membership and rental to return, is automated. Users can easily rent a bike from one location and return it to another. There are now over 500 bike-sharing programs worldwide, comprising more than 500,000 bicycles. These systems play a vital role in addressing traffic congestion, environmental concerns, and promoting healthier lifestyles. Moreover, the data generated by these systems is of great interest for research, as it includes explicit information about travel duration, departure and arrival positions, effectively creating a virtual sensor network for monitoring urban mobility.

## Project Structure

The project is organized into the following folders:

  - EDA: This folder contains notebooks and scripts for Exploratory Data Analysis (EDA), where you can delve into data exploration, visualization, and understanding.

  - Regression: In this folder, you will find notebooks and scripts related to bike-sharing demand prediction using regression techniques. These include models for predicting bike rental counts on an hourly or daily basis based on various factors.
  
  - Visualization: The Visualization folder is the highlight of this project. It features an interactive map with layers that can be turned on and off. This map allows you to:

    - View real-time positions of bikes, and stations along with their current capacity in Washington D.C.
    - Highlight or hide the Washington D.C. area.
    - Explore the 100 most popular bike routes for the years 2011, 2014, 2019, and 2023.

## Interactive Map

The interactive map in this project is a unique and engaging feature. It allows you to visualize the real-time positions of bikes in Washington D.C., providing valuable insights into live bike-sharing patterns and availability. While the regression tasks are based on historical data from 2011 and 2012, the interactive map presents current data, giving users a real-time perspective on bike-sharing activity in the city.

Feel free to explore, analyze, and contribute to this project, with special attention to the captivating interactive map in the Visualization folder!


## Data Set

This project revolves around predicting bike-sharing rental demand, which is highly influenced by various environmental and seasonal factors, such as weather conditions, precipitation, day of the week, season, and time of day. The core data set used for regression tasks in this project is derived from the two-year historical log of the Capital Bikeshare system in Washington D.C., USA, covering the years 2011 and 2012. This publicly available dataset is aggregated on both an hourly and daily basis and augmented with weather and seasonal information. Weather data is sourced from Freemeteo.

Note: The regression tasks are based on historical data from 2011 and 2012. The interactive map is in real-time!

## Enriched Features

The dataset has been enriched through extensive feature engineering and integration with a weather API, resulting in the following additional features:

    dtime: Date and time.
    season_name: Name of the season (e.g., spring, summer).
    mnth: Month (1 to 12).
    season_num: Season number (1:spring, 2:summer, 3:fall, 4:winter).
    workingday: Indicates if it's a working day (1) or not (0).
    weathersit: Weather situation code.
    hum: Normalized humidity.
    windspeed: Normalized wind speed.
    casual: Count of casual users.
    registered: Count of registered users.
    total: Count of total rental bikes, including both casual and registered users.
    temp_celsius: Normalized temperature in Celsius.
    temp_celsius_realfeel: Normalized feeling temperature in Celsius.
    weathercode_wmo: Weather condition code.
    temp_max: Maximum temperature.
    temp_min: Minimum temperature.
    precipitation_sum_mm: Total precipitation in millimeters.
    windspeed_km/h: Wind speed in kilometers per hour.
    wind_direction_deg: Wind direction in degrees.
    shortwave_radiation_MJ/m²: Shortwave radiation in MJ/m².
    windy_cat: Wind category.
    day_0 through day_6: Binary indicators for days of the week.
    rainy_no and rainy_yes: Binary indicators for rainy weather.
    year_0 and year_1: Binary indicators for the year (0: 2011, 1: 2012).
    wind_direct_N, wind_direct_E, wind_direct_NE, wind_direct_NW, wind_direct_S, wind_direct_SE, wind_direct_SW, wind_direct_W: Binary indicators for wind direction.
    holiday_0 and holiday_1: Binary indicators for holidays.
    casual_count_lag1: Lagged count of casual users.
    event_no and event_yes: Binary indicators for events.

These enriched features provide a more comprehensive dataset for exploring and predicting bike-sharing demand, taking into account various weather conditions and other contextual factors.

Feel free to explore, analyze, and contribute to this project!