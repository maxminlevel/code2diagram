from parsing.converter import DotConverter


converter = DotConverter()
converter.convert("src/test.json", "test-output/graph")
