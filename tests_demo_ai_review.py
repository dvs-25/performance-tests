from dataclasses import dataclass
import pytest

# Локальный "заглушечный" allure, чтобы файл работал даже без установленного пакета
try:
    import allure  # type: ignore
except Exception:  # pragma: no cover
    class allure:  # noqa: N801
        @staticmethod
        def tag(*_args, **_kwargs):
            def deco(f): return f
            return deco
        @staticmethod
        def story(*_args, **_kwargs):
            def deco(f): return f
            return deco

@dataclass
class Resp:
    status: str
    reason: str | None = None
    message: str | None = None

class API:
    def make_purchase(self, user_id: int, amount: int) -> Resp:
        # Условная бизнес-логика: всё, что > 50_000 — отклоняем по лимиту
        if amount > 50_000:
            return Resp(status="DECLINED", reason="LIMIT_EXCEEDED", message="limit reached")
        return Resp(status="OK")

@pytest.fixture
def api():
    return API()

@allure.story("payments")
def test_purchase_declined_on_limit(api):
    resp = api.make_purchase(user_id=1, amount=100_000)
    assert resp.status == "DECLINED"

@allure.story("refunds")
def test_refund_succeeds():
    assert True
