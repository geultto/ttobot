from starlette import status
from fastapi import APIRouter, Depends, Query
from app.api.deps import api_service
from app.api.services import ApiService
from app.api import dto


router = APIRouter()


@router.get(
    "/paper_planes/sent",
    status_code=status.HTTP_200_OK,
    response_model=dto.PaperPlaneResponse,
)
async def fetch_sent_paper_planes(
    user_id: str,
    offset: int = 0,
    limit: int = Query(default=50, le=50),
    service: ApiService = Depends(api_service),
) -> dto.PaperPlaneResponse:
    """조건에 맞는 종이비행기를 가져옵니다."""
    count, data = service.fetch_sent_paper_planes(
        user_id=user_id, offset=offset, limit=limit
    )
    return dto.PaperPlaneResponse(
        count=count, data=[each.model_dump() for each in data]
    )


@router.get(
    "/paper_planes/received",
    status_code=status.HTTP_200_OK,
    response_model=dto.PaperPlaneResponse,
)
async def fetch_received_paper_planes(
    user_id: str,
    offset: int = 0,
    limit: int = Query(default=50, le=50),
    service: ApiService = Depends(api_service),
) -> dto.PaperPlaneResponse:
    """조건에 맞는 종이비행기를 가져옵니다."""
    count, data = service.fetch_received_paper_planes(
        user_id=user_id, offset=offset, limit=limit
    )
    return dto.PaperPlaneResponse(
        count=count, data=[each.model_dump() for each in data]
    )