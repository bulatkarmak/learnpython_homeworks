from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city('Kazan, Russia')
    if weather:
        return f'Температура в Казани: {weather["temp_C"]} °C (ощущается как {weather["FeelsLikeC"]})'
    else:
        return f'Сервис погоды временно недоступен'

if __name__ == '__main__':
    app.run(debug=True)