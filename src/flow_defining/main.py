import logging

from dotenv import load_dotenv
from crewai.flow.flow import Flow, listen, start

from flow_defining.state import ResearchFlowState, StepStatus
from flow_defining.utils import banner, configure_logging, SOURCE_PROMPTS
from flow_defining.crews.research_crew.research_crew import ResearchCrew
from flow_defining.crews.writing_crew.writing_crew import WritingCrew

load_dotenv()
configure_logging()
logger = logging.getLogger(__name__)


class GuideGeneratorFlow(Flow[ResearchFlowState]):
    """
    Main flow that orchestrates the complete guide generation process.

    Flow Steps:
    1. receive_user_inputs - Accept and Validate user inputs
    2. run_research_crew - Execute Crew 1 (hierarchical research)
    3. run_writing_crew - Execute Crew 2 (sequential writing)
    """

    @start()
    def receive_user_inputs(self) -> StepStatus:
        banner("GUIDE GENERATOR FLOW STARTED")

        sources = {
            "YouTube": self.state.youtube_links,
            "Web Pages": self.state.webpage_links,
            "Documents": self.state.document_paths,
            "Research Papers": self.state.research_paper_links,
        }
        provided = [name for name, value in sources.items() if value]

        if not provided:
            logger.warning("No sources provided. Please provide at least one source type.")
            return StepStatus.NO_SOURCES

        logger.info("Sources provided: %s", ", ".join(provided))
        return StepStatus.INPUTS_RECEIVED

    @listen(receive_user_inputs)
    def run_research_crew(self, prev_status: StepStatus) -> StepStatus:
        """Executes Crew 1: Research Crew (manager + 4 specialists -> research report)."""
        if prev_status != StepStatus.INPUTS_RECEIVED:
            logger.info("Skipping research crew - no sources provided")
            return StepStatus.RESEARCH_SKIPPED

        banner("CREW 1: RESEARCH CREW (Hierarchical)")
        logger.info("Specialists: YouTube, Web Content, Academic Paper, Document")

        try:
            research_crew = ResearchCrew().crew()
            result = research_crew.kickoff(inputs={
                "youtube_links": self.state.youtube_links or "Not provided",
                "webpage_links": self.state.webpage_links or "Not provided",
                "research_paper_links": self.state.research_paper_links or "Not provided",
                "document_paths": self.state.document_paths or "Not provided",
            })
            self.state.research_report = result.raw
            banner("RESEARCH CREW COMPLETED")
            return StepStatus.RESEARCH_COMPLETE

        except Exception:
            logger.exception("Research Crew failed")
            return StepStatus.RESEARCH_FAILED

    @listen(run_research_crew)
    def run_writing_crew(self, prev_status: StepStatus) -> StepStatus:
        """Executes Crew 2: Writing Crew (Technical Writer -> Content Editor)."""
        if prev_status != StepStatus.RESEARCH_COMPLETE:
            logger.info("Skipping writing crew - research was not completed")
            return StepStatus.WRITING_SKIPPED

        banner("CREW 2: WRITING CREW (Sequential)")
        logger.info("Steps: Technical Writer -> Content Editor")

        try:
            writing_crew = WritingCrew().crew()
            result = writing_crew.kickoff(inputs={"research_report": self.state.research_report})
            self.state.final_guide = result.raw
            banner("WRITING CREW COMPLETED")
            return StepStatus.WRITING_COMPLETE

        except Exception:
            logger.exception("Writing Crew failed")
            return StepStatus.WRITING_FAILED


def get_inputs() -> dict:
    """Interactive terminal interface to collect user inputs. All inputs are optional."""
    banner("GUIDE GENERATOR - INPUT COLLECTION")
    logger.info("All source inputs are OPTIONAL. You can skip any by pressing Enter.")

    inputs = {}
    for source in SOURCE_PROMPTS:
        banner(source["title"], char="-")
        for hint in source["hints"]:
            logger.info("- %s", hint)
        inputs[source["key"]] = input(f"\n{source['prompt']}").strip()

    return inputs


def kickoff():
    """Execute the flow."""
    inputs = get_inputs()
    flow = GuideGeneratorFlow()
    flow_result = flow.kickoff(inputs=inputs)

    banner("FINAL RESULT")
    logger.info(flow_result)


if __name__ == "__main__":
    kickoff()
