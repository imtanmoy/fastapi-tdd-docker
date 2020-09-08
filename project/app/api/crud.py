from typing import List, Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="")
    await summary.save()
    return summary.id


async def get(sid: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=sid).first().values()
    if summary:
        return summary[0]
    return None


async def delete(sid: int) -> int:
    summary = await TextSummary.filter(id=sid).first().delete()
    return summary


async def put(sid: int, payload: SummaryPayloadSchema) -> Union[dict, None]:
    summary = await TextSummary.filter(id=sid).update(
        url=payload.url, summary=payload.summary
    )
    if summary:
        updated_summary = await TextSummary.filter(id=sid).first().values()
        return updated_summary[0]
    return None
