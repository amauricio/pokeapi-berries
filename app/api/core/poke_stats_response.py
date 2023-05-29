from fastapi import Response
from typing import Any
import json

class PokeStatsResponse(Response):
    def __init__(self, content, *args, **kwargs):
        
        self.message = kwargs.get("message", "OK")
        self.status_code = kwargs.get("status_code", 200)

        super().__init__(
            content=json.dumps({
                "status": self.status_code,
                "message": self.message,
                "data": content
            }),
            media_type="application/json",
            *args,
            **kwargs,
        )
