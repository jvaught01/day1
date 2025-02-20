import requests
import boto3
import dotenv
import os
import datetime
import json

dotenv.load_dotenv()


class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv("OPEN_WEATHER_API_KEY")
        self.bucket_name = os.getenv("AWS_BUCKET_NAME")
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_SERVER_PUBLIC_KEY"),
            aws_secret_access_key=os.getenv("AWS_SERVER_SECRET_KEY"),
        )

    def get_weather(self, city):
        print(f"Getting weather for {city}")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url)
        print("writing weather data to file")
        filename = (
            f"{city}-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.json"
        )
        with open(filename, "w") as file:
            file.write(json.dumps(response.json()))
        return filename

    def create_bucket(self):
        print(f"Creating bucket {self.bucket_name}")
        try:
            self.s3_client.create_bucket(Bucket=self.bucket_name)
            return f"Bucket {self.bucket_name} created"
        except Exception as e:
            return f"Error creating bucket: {e}"

    def upload_file(self, file):
        print(f"Uploading file {file} to {self.bucket_name}")
        try:
            self.s3_client.upload_file(file, self.bucket_name, f"{file}")
            print(f"File {file} uploaded to {self.bucket_name}")
            return f"File {file} uploaded to {self.bucket_name}"
        except Exception as e:
            return f"Error uploading file: {e}"


def main():
    cities = ["London", "Paris", "New York", "Tokyo", "Sydney", "Berlin", "Madrid"]
    weather_dashboard = WeatherDashboard()
    weather_dashboard.create_bucket()
    for city in cities:
        filename = weather_dashboard.get_weather(city)
        if filename:
            with open(filename, "r") as file:
                weather_data = json.load(file)
            temp = weather_data["main"]["temp"]
            feels_like = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["weather"][0]["description"]
            print(f"Temperature: {temp}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")

        weather_dashboard.upload_file(filename)


if __name__ == "__main__":
    main()
