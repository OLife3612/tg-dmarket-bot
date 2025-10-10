from typing import Optional, Tuple
import httpx


class DMarketClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = httpx.Client(timeout=15.0, headers={
            "X-Api-Key": api_key,
            "Accept": "application/json",
        })

    def best_price_usd(self, market_item_id: str) -> Optional[Tuple[float, str]]:
        """
        Верни (price, currency) или None. market_item_id — твой стабильный идентификатор.
        TODO: подставь актуальный endpoint/параметры из Swagger DMarket.
        Примерно нужно получить минимальный ask по предмету в CS2.
        """
        # TODO: пример запроса (замени на реальный):
        # resp = self.client.get("https://api.dmarket.com/marketplace-api/v1/market-depth", params={
        #     "Title": market_item_id,
        #     "GameId": "csgo"  # или актуальный id CS2
        # })
        # if resp.status_code == 200:
        #     data = resp.json()
        #     price = ... # вытащи best ask
        #     return float(price), "USD"
        return None
