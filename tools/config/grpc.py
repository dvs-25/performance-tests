from pydantic import BaseModel


class GRPCClientConfig(BaseModel):
    port: int
    host: str

    @property
    def client_url(self) -> str:
        """
        Возвращает адрес подключения в формате host:port,
        который требуется для создания gRPC-канала через insecure_channel().
        """
        return f"{self.host}:{self.port}"
