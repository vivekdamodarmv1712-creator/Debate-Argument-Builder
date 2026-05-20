from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class DebateArgumentBuilder():

    """DebateArgumentBuilder crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # ---------------- AGENTS ---------------- #

    @agent
    def argument_constructor(self) -> Agent:
        return Agent(
            config=self.agents_config['argument_constructor'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def counterargument_anticipator(self) -> Agent:
        return Agent(
            config=self.agents_config['counterargument_anticipator'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def rebuttal_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['rebuttal_writer'],  # type: ignore[index]
            verbose=True
        )

    # ---------------- TASKS ---------------- #

    @task
    def build_arguments(self) -> Task:
        return Task(
            config=self.tasks_config['build_arguments'],  # type: ignore[index]
        )

    @task
    def predict_counterarguments(self) -> Task:
        return Task(
            config=self.tasks_config['predict_counterarguments'],  # type: ignore[index]
        )

    @task
    def write_rebuttals(self) -> Task:
        return Task(
            config=self.tasks_config['write_rebuttals'],  # type: ignore[index]
            output_file="output/debate_brief.md"
        )

    # ---------------- CREW ---------------- #

    @crew
    def crew(self) -> Crew:
        """Creates the DebateArgumentBuilder crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )