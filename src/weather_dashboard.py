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
        with open("weather.json", "w") as file:
            file.write(json.dumps(response.json()))
        return response.json()

    def create_bucket(self):
        print(f"Creating bucket {self.bucket_name}")
        try:
            self.s3_client.create_bucket(Bucket=self.bucket_name)
            return f"Bucket {self.bucket_name} created"
        except Exception as e:
            return f"Error creating bucket: {e}"

    def upload_file(self, file_name, file_path):
        print(f"Uploading file {file_name} to {self.bucket_name}")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        try:
            self.s3_client.upload_file(
                file_name, self.bucket_name, f"{timestamp}-{file_name}"
            )
            print(f"File {file_name} uploaded to {self.bucket_name}")
            return f"File {file_name} uploaded to {self.bucket_name}"
        except Exception as e:
            return f"Error uploading file: {e}"


def main():
    cities = ["London", "Paris", "New York", "Tokyo", "Sydney", "Berlin", "Madrid"]
    weather_dashboard = WeatherDashboard()
    for city in cities:
        weather_dashboard.get_weather(city)
    weather_dashboard.create_bucket()
    weather_dashboard.upload_file("weather.json", "weather.json")


if __name__ == "__main__":
    main()
