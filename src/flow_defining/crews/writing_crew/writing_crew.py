from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class WritingCrew():
    """WritingCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    @agent
    def technical_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_writer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer'], # type: ignore[index]
            verbose=True
        )

    @task
    def write_getting_started_guide(self) -> Task:
        return Task(
            config=self.tasks_config['write_getting_started_guide'], # type: ignore[index]
        )

    @task
    def review_and_polish_guide(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_polish_guide'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the WritingCrew crew"""
        return Crew(
            agents=[self.content_writer(),
                    self.technical_writer()],
            tasks=[self.review_and_polish_guide(),
                   self.write_getting_started_guide()],
            process=Process.sequential,
            verbose=True,
        )
