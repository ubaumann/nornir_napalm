from typing import List

from nornir.core.task import Result, Task

from nornir_napalm.plugins.connections import CONNECTION_NAME


def napalm_cli(task: Task, commands: List[str]) -> Result:
    """
    Run commands on remote devices using napalm

    Arguments:
      commands: commands to execute

    Returns:
      Result object with the following attributes set:
        * result (``dict``): result of the commands execution
    """
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    result = device.cli(commands)
    return Result(host=task.host, result=result)
