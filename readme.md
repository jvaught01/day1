# Weather Dashboard

A Python application that fetches weather data for multiple cities using the OpenWeather API and stores the data in AWS S3 buckets.

## Features

- Fetches current weather data for specified cities
- Creates AWS S3 buckets for data storage
- Uploads weather data as JSON files to S3
- Processes and displays temperature, feels-like temperature, humidity, and weather conditions

## Prerequisites

- Python 3.x
- AWS account with appropriate credentials
- OpenWeather API key

## Required Libraries

```python
import requests
import boto3
import dotenv
import os
import datetime
import json
```

## Environment Variables

The following environment variables must be set in a `.env` file:

```plaintext
OPEN_WEATHER_API_KEY=your_openweather_api_key
AWS_BUCKET_NAME=your_bucket_name
AWS_SERVER_PUBLIC_KEY=your_aws_public_key
AWS_SERVER_SECRET_KEY=your_aws_secret_key
```

## Class: WeatherDashboard

### Methods

#### `__init__()`
Initializes the WeatherDashboard with API keys and AWS credentials.

#### `get_weather(city)`
Fetches weather data for a specified city.

Parameters:
- `city` (str): Name of the city to fetch weather data for

Returns:
- `filename` (str): Name of the file where weather data is saved

#### `create_bucket()`
Creates an S3 bucket using the specified bucket name.

Returns:
- str: Success or error message

#### `upload_file(file)`
Uploads a file to the S3 bucket.

Parameters:
- `file` (str): Path to the file to upload

Returns:
- str: Success or error message

## Main Function

The main function:
1. Defines a list of cities
2. Creates a WeatherDashboard instance
3. Creates an S3 bucket
4. For each city:
   - Fetches weather data
   - Extracts and displays:
     - Temperature
     - Feels-like temperature
     - Humidity
     - Weather conditions
   - Uploads data to S3

## Usage

```python
if __name__ == "__main__":
    main()
```

## Sample Cities

The application comes preconfigured with the following cities:
- London
- Paris
- New York
- Tokyo
- Sydney
- Berlin
- Madrid

## Output Format

For each city, the program outputs:
- Temperature in Fahrenheit
- Feels-like temperature in Fahrenheit
- Humidity percentage
- Weather conditions description

## File Naming Convention

Weather data files are saved with the following format:
`{city}-{YYYY-MM-DD-HH-MM-SS}.json`

Example: `London-2025-01-06-14-30-45.json`