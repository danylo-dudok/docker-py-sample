from models import Context, Port, Container, Network
import json


def get_context(file_path: str) -> Context:
    with open(file_path, 'r') as file:
        context_dict = json.load(file)

        context = Context(**context_dict)

        for i in range(len(context.containers)):
            container = context.containers[i] = Container(**context.containers[i])
            container.ports = Port(**container.ports)

        for i in range(len(context.networks)):
            context.networks[i] = Network(**context.networks[i])

        return context
