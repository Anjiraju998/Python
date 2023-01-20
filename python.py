html = """
<!DOCTYPE html>
<html>
<head>
<title>Sample HTML Page</title>
</head>
<body>
<h1>Hello World!</h1>
<p>This is a sample HTML page generated using Python.</p>
</body>
</html>
"""

 

with open("sample.html", "w") as f:
    f.write(html)
