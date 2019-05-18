weather = {"city": "Москва", "temperature": "20"}
print(weather["city"])
weather["temperature"] = str(int(weather["temperature"]) - 8)
print(weather)

print("country" in weather)
print(weather.get("country", "Россия"))
weather["date"] = "27.05.2019"
print(len(weather))