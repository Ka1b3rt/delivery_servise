from fastapi import Request

from app.models.user import User


def get_current_user(request: Request) -> User:
    return request.state.user