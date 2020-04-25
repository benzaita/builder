from dockerized.core.commands.dockercomposecommand import DockerComposeCommand


class CleanCommand(DockerComposeCommand):
    def __init__(self, env=None, docker_compose=None):
        super().__init__(env, docker_compose)

    def run(self):
        self.docker_compose.down()
        self.project.set_prepared(False)
