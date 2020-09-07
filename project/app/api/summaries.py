from typing import List

from fastapi import APIRouter, HTTPException, Path

from app.api import crud
from app.models.pydantic import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    SummaryUpdatePayloadSchema,
)
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    return await crud.get_all()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {"id": summary_id, "url": payload.url}
    return response_object


@router.get("/{sid}/", response_model=SummarySchema)
async def read_summary(sid: int = Path(..., gt=0)) -> SummarySchema:
    summary = await crud.get(sid)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary


@router.delete("/{sid}/", response_model=SummaryResponseSchema)
async def delete_summary(sid: int = Path(..., gt=0)) -> SummaryResponseSchema:
    summary = await crud.get(sid)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    await crud.delete(sid)

    return summary


@router.put("/{sid}/", response_model=SummarySchema)
async def update_summary(
    payload: SummaryUpdatePayloadSchema, sid: int = Path(..., gt=0)
) -> SummarySchema:
    summary = await crud.put(sid, payload)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary
