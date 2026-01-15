import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "34eb629903d82f7d11e930556dc585a2"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
ICON_URL = "https://openweathermap.org/img/wn/"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x500")

        self.unit = "metric"

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Weather Application", font=("Arial", 18, "bold")).pack(pady=10)

        self.city_entry = tk.Entry(self.root, font=("Arial", 14))
        self.city_entry.pack(pady=5)

        tk.Button(self.root, text="Get Weather", command=self.get_weather).pack(pady=5)

        self.unit_button = tk.Button(self.root, text="Switch to °F", command=self.switch_unit)
        self.unit_button.pack(pady=5)

        self.icon_label = tk.Label(self.root)
        self.icon_label.pack()

        self.result_label = tk.Label(self.root, font=("Arial", 12), justify="center")
        self.result_label.pack(pady=10)

    def switch_unit(self):
        if self.unit == "metric":
            self.unit = "imperial"
            self.unit_button.config(text="Switch to °C")
        else:
            self.unit = "metric"
            self.unit_button.config(text="Switch to °F")

    def get_weather(self):
        city = self.city_entry.get().strip()

        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        params = {
            "q": city,
            "appid": API_KEY,
            "units": self.unit
        }

        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            data = response.json()

            if response.status_code != 200:
                raise ValueError(data.get("message", "Failed to fetch weather"))

            self.display_weather(data)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_weather(self, data):
        temp_unit = "°C" if self.unit == "metric" else "°F"

        city = data["name"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].title()
        wind = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        icon = data["weather"][0]["icon"]

        # Load icon safely
        icon_response = requests.get(f"{ICON_URL}{icon}@2x.png")
        img = Image.open(BytesIO(icon_response.content))
        photo = ImageTk.PhotoImage(img)

        self.icon_label.config(image=photo)
        self.icon_label.image = photo

        self.result_label.config(
            text=(
                f"{city}\n\n"
                f"Temperature: {temp}{temp_unit}\n"
                f"Condition: {desc}\n"
                f"Wind Speed: {wind}\n"
                f"Humidity: {humidity}%"
            )
        )

if __name__ == "__main__":
    root = tk.Tk()
    WeatherApp(root)
    root.mainloop()
