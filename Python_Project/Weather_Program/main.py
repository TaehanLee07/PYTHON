import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] != 200:
        print("날씨 정보를 가져오는 데 실패했습니다.")
        return
    
    print(f"현재 온도: {weather_data['main']['temp']}°C")
    print(f"체감 온도: {weather_data['main']['feels_like']}°C")
    print(f"습도: {weather_data['main']['humidity']}%")
    print(f"날씨: {weather_data['weather'][0]['description']}")
    print(f"풍속: {weather_data['wind']['speed']}m/s")

def main():
    api_key = "본인의 API 키를 넣어주세요"
    location = input("날씨를 확인할 위치를 입력하세요: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
