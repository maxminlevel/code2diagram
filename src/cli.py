def simple_path(inputPath, outputPath):
    from parsing.converter import DotConverter
    converter = DotConverter()
    converter.convert(inputFile=inputPath, outputFile=outputPath)

def complex_path(inputPaht, outputPath, customInput, customOutput, customToken):
    print("These features are in develope")
    pass

if __name__ == "__main__":
    import os
    import cli.cli as cli

    cli.args['input'] = os.getcwd()+"/"+cli.args['input']
    if not (cli.args['output']):
        cli.args['output'] = "output/output.jpeg"
    if (cli.args['format_input'] or cli.args['format_output'] or cli.args['token']):
        complex_path(cli.args['input'], cli.args['output'],cli.args['format_input'], cli.args['format_output'], cli.args['token'])
    else:
        simple_path(cli.args['input'], cli.args['output'])
else:
    print("Run in main mode to use CLI tools")