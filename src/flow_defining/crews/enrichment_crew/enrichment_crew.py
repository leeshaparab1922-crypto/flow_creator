from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class EnrichmentCrew():
    """EnrichmentCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def web_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["web_search_agent"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def gap_fill_task(self) -> Task:
        return Task(
            config=self.tasks_config["gap_fill_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EnrichmentCrew crew"""
        return Crew(
            agents=[self.web_search_agent()],
            tasks=[self.gap_fill_task()],
            process=Process.sequential,
            verbose=True,
        )