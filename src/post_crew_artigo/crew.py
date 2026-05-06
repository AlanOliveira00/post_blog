from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, llm


@CrewBase
class PostCrewArtigo():
    """PostCrewArtigo crew"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @llm
    def meu_modelo(self) -> LLM:
        return LLM(
            model="anthropic/claude-sonnet-4-6", 
            temperature=0.7,
        )

    @agent
    def desenvolvedor_de_ideias(self) -> Agent:
        return Agent(
            config=self.agents_config['desenvolvedor_de_ideias'],
            verbose=True,
            llm=self.meu_modelo()
        )

    @agent
    def planejador_de_conteudo(self) -> Agent:
        return Agent(
            config=self.agents_config['planejador_de_conteudo'],
            verbose=True,
            llm=self.meu_modelo()
        )

    @agent
    def escritor_do_post(self) -> Agent:
        return Agent(
            config=self.agents_config['escritor_do_post'],
            verbose=True,
            llm=self.meu_modelo()
        )

    @agent
    def revisor_do_post(self) -> Agent:
        return Agent(
            config=self.agents_config['revisor_do_post'],
            verbose=True,
            llm=self.meu_modelo()
        )

    @task
    def cria_ideias(self) -> Task:
        return Task(
            config=self.tasks_config['cria_ideias'],
        )

    @task
    def seleciona_ideias(self) -> Task:
        return Task(
            config=self.tasks_config['seleciona_ideias'],
            output_file='report.md'
        )

    @task
    def planeja_conteudo(self) -> Task:
        return Task(
            config=self.tasks_config['planeja_conteudo'],
            output_file='outline.md'
        )

    @task
    def escreve_post(self) -> Task:
        return Task(
            config=self.tasks_config['escreve_post'],
            output_file='post.md'
        )

    @task
    def revisa_post(self) -> Task:
        return Task(
            config=self.tasks_config['revisa_post'],
            output_file='post_revisado.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PostCrewArtigo crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            #llm=self.meu_modelo()
        )