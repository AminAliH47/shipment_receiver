from django.core.cache import cache
import requests

from config.envs import envs


def get_data_from_weather_api(city: str) -> dict:
    cache_key = f'weather-{city}'
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data

    url = f'{envs.WEATHER_API_URL}/v4/weather/forecast'
    params = {
        'apikey': envs.WEATHER_APIKEY,
        'location': city,
        'timesteps': '1m',
    }
    try:
        response = requests.get(url, params, timeout=1).json()
    except requests.RequestException:
        return 'Not available!'

    weather = response['timelines']['minutely'][0]['values']
    cache.set(cache_key, weather, 60 * 120)

    return weather
