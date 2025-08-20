import requests

API_URL = "https://open.er-api.com/v6/latest/USD"

class ExchangeError(Exception):
    pass

def get_usd_to_uzs_rate() -> float:
    """Fetch USD→UZS from open.er-api. Raises ExchangeError on failure."""
    try:
        r = requests.get(API_URL, timeout=10)
        r.raise_for_status()
        data = r.json()
        # Validate expected structure
        if data.get("result") != "success":
            raise ExchangeError(f"API error: {data.get('error-type') or data.get('result')}")
        uzs = data["rates"].get("UZS")
        if not isinstance(uzs, (int, float)):
            raise ExchangeError("UZS rate not found in response")
        return float(uzs)
    except requests.RequestException as e:
        raise ExchangeError(f"Network error: {e}") from e
    except (KeyError, ValueError, TypeError) as e:
        raise ExchangeError(f"Parse error: {e}") from e
