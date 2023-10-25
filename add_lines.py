from pathlib import Path

texts = Path.cwd().glob("*.md")

for t in texts:
	string = t.read_text()
	lines = string.split("\n")
	new_text = ""
	for line in lines:
		line = line.rstrip() + "  "
		print(f">>>{line}<<<")
		new_text += line + "\n"
	t.write_text(new_text)
	
	
