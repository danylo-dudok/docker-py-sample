from data import get_context
from models import *
from os.path import join
import docker
import sys


def create(client, networks_to_create) -> None:
    for network in networks_to_create:
        client.networks.create(name=network.name)
        print(f'Created {network.name} network.')


def build(client, files_to_build, path) -> None:
    for file in files_to_build:
        client.images.build(path=path, dockerfile=file)
        print(f'Built {file} image.')


def run(client, containers_to_run) -> None:
    for container in containers_to_run:
        log = client.containers.run(
                container.image_name,
                name=container.name,
                detach=container.detach,
                ports={f'{container.ports.internal}/{container.ports.protocol}': container.ports.expose},
                network=container.networks[0] if type(container.networks) is List else container.networks,
                environment=container.environments,
            )
        print(log)
        print(f'Ran {container.name} container.')
        if len(container.networks) > 1:
            raise Exception('Multiple networks in not supported yet!')


def main(arguments: List[str]) -> None:
    config_file_path = join(
        *arguments[
            arguments.index('--config') + 1
        ].split('/\\')
    )

    context = get_context(config_file_path)
    client = docker.from_env()

    create(client, context.networks)
    build(client, context.builds, context.path)
    run(client, context.containers)

    print('All done.')


if __name__ == '__main__':
    main(sys.argv)
