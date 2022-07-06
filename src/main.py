from parsing.converter import DotConverter


converter = DotConverter()
converter.convert("src/dict.json", "test-output/graph")
