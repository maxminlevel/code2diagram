from parsing.converter import DotConverter


converter = DotConverter()
converter.convert("src/a.json", "test-output/graph")
