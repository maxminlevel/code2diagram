def simple_path(inputPath, outputPath):
    pass

def complex_path(inputPaht, outputPath, customInput, customOutput, customToken):
    pass

if __name__ == "__main__":
    import os
    import cli.cli as cli

    cli.args['input'] = os.getcwd()+"/"+cli.args['input']
    print(cli.args)
    if (cli.args['output']):
        cli.args['output'] = "output/output.jpeg"
    if not (cli.args['format_input'] and cli.agrs['format_output'] and cli.args['token']):
        complex_path(cli.args['input'], cli.args['output'],cli.args['format_input'], cli.agrs['format_output'], cli.args['token'])
    else:
        simple_path(cli.args['input'], cli.args['output'])
else:
    print("Run in main mode to use CLI tools")