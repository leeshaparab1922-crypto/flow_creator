from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class QACrew():
    """QACrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def tutor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["tutor_agent"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def answer_question(self) -> Task:
        return Task(
            config=self.tasks_config["answer_question"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the QACrew crew"""
        return Crew(
            agents=[self.tutor_agent()],
            tasks=[self.answer_question()],
            process=Process.sequential,
            verbose=True,
        )