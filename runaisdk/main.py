import httpx


class RunClient:
    _users = None
    _projects = None
    _accessToken = None

    def __init__(
        self,
        appId: str,
        appSecret: str,
        realm: str,
        base_url: str = "https://app.run.ai",
    ) -> None:
        self._client = httpx.Client(base_url=base_url)
        self._appId = appId
        self._appSecret = appSecret
        self._realm = realm


def main():
    RunClient("api", "1234541", "testing")

if __name__ == "__main__":
    main()
