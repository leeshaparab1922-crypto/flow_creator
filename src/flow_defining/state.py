from enum import Enum, auto
from typing import Optional

from pydantic import BaseModel


class StepStatus(Enum):
    NO_SOURCES = auto()
    INPUTS_RECEIVED = auto()
    RESEARCH_COMPLETE = auto()
    RESEARCH_FAILED = auto()
    RESEARCH_SKIPPED = auto()
    WRITING_COMPLETE = auto()
    WRITING_FAILED = auto()
    WRITING_SKIPPED = auto()


class ResearchFlowState(BaseModel):
    youtube_links: Optional[str] = ""
    document_paths: Optional[str] = ""
    webpage_links: Optional[str] = ""
    research_paper_links: Optional[str] = ""

    research_report: str | None = None
    final_guide: str | None = None
