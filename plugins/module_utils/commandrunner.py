import subprocess
from commandresult import CommandResult

class CommandRunner(object):
    """
        Command:

        This is a helper utility for running commandline binaries
    """
    def __init__(self, binary) -> None:
        self.binary = binary

    def run(self, command, subcommand, args) -> CommandResult:
        run_command = [self.binary] + [command] + [subcommand] + args

        try:
            result = subprocess.run(run_command, shell=True, check=True, 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                                    text=True)
            return CommandResult(
                exit_code=result.returncode,
                output=result.stdout.strip(),
                error=result.stderr.strip()
            )
        except subprocess.CalledProcessError as e:
            # Handle errors from running the command
            return CommandResult(
                exit_code=e.returncode,
                output=e.stdout.strip() if e.stdout else "",
                error=e.stderr.strip() if e.stderr else ""
            )

