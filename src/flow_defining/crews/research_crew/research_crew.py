from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import (YoutubeVideoSearchTool,
                          YoutubeChannelSearchTool,
                          ScrapeWebsiteTool,
                          SeleniumScrapingTool,
                          CodeDocsSearchTool,
                          ArxivPaperTool,
                          FileReadTool,
                          PDFSearchTool,
                          TXTSearchTool,
                          MDXSearchTool,
                          DirectoryReadTool                         
)
                    
# arxiv research paper tool
arxiv_tool = ArxivPaperTool(download_pdfs=True,
                            use_title_as_filename=True)

@CrewBase
class ResearchCrew():
    """ResearchCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # =============================== Agents ===============================
    # defined the agents 
    @agent
    def research_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['research_manager'], # type: ignore[index]
            verbose=True
        )
    @agent
    def youtube_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['youtube_specialist'], # type: ignore[index]
            verbose=True,
            tools=[YoutubeVideoSearchTool(),
                   YoutubeChannelSearchTool()]
        )

    @agent
    def web_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['web_specialist'], # type: ignore[index]
            verbose=True,
            tools=[ScrapeWebsiteTool(),
                   SeleniumScrapingTool(),
                   CodeDocsSearchTool()]
        )
    
    @agent
    def arxiv_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['arxiv_specialist'], # type: ignore[index]
            verbose=True,
            tools=[arxiv_tool]
        )
    
    @agent
    def document_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['document_specialist'], # type: ignore[index]
            verbose=True,
            tools=[FileReadTool(),
                   PDFSearchTool(),
                   TXTSearchTool(),
                   MDXSearchTool(),
                   DirectoryReadTool()]
        )
    
    # ======================== Tasks ==================================
    # defined the tasks 

    @task
    def research_compilation(self) -> Task:
        return Task(
            config=self.tasks_config['research_compilation'], # type: ignore[index]
        )

# ======================== Crew ===================================


    @crew
    def crew(self) -> Crew:
        """Creates the ResearchCrew crew"""
        return Crew(
            agents= [self.youtube_specialist(),
                    self.web_specialist(),
                    self.arxiv_specialist(),
                    self.document_specialist()],
            tasks=[self.research_compilation()],
            manager_agent = self.research_manager(),
            process=Process.hierarchical,
            verbose=True,
        )

def run(inputs: dict[str, str]) -> str:
    """Test Run our crew"""
    research_crew = ResearchCrew().crew()
    result = research_crew.kickoff(inputs)
    return result.raw


if __name__ == "__main__":
    inputs = {
        "youtube_links": "",
        "webpage_links": "https://www.w3schools.com/python/python_for_loops.asp",
        "research_paper_links": "",
        "document_paths": ""
    }
    
    result = run(inputs)
    print(result)