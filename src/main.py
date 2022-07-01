import os
import cli.cli as cli

cli.args['input'] = os.getcwd()+"/"+cli.args['input']
print(cli.args)