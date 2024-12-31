import fastapi
from fastapi import Response

app = fastapi.FastAPI()
base = "/curse/fetch/{fileid}/{filename}/{ext}"

@app.head(base + ".pom")
async def head_pom(fileid: str, filename: str, ext: str):
    return Response(headers = {
        "Content-Type": "application/xml",
        "Content-Disposition": f"attachment; filename={filename}.pom"
    })

@app.get(base + ".pom")
async def pom(fileid: str, filename: str, ext: str):
    (filename.replace("&", "&amp;")
     .replace("<", "&lt;")
     .replace(">", "&gt;")
     .replace('"', "&quot;")
     .replace("'", "&apos;"))

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"
    xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <modelVersion>4.0.0</modelVersion>
  <groupId>curse.fetch</groupId>
  <artifactId>{fileid}</artifactId>
  <version>{filename}</version>
</project>"""
    return Response(content = xml, media_type = "application/xml")

@app.get(base)
async def file(fileid: str, filename: str, ext: str):
    print(ext)
    real_name = filename + "." + ext.split(".")[-1]
    if len(fileid) < 4:
        raise Exception("ID must be at least 4 characters long.")
    first_half = fileid[:4]
    second_half = fileid[4:]
    link = f"https://mediafilez.forgecdn.net/files/{first_half}/{second_half}/{real_name}"
    return fastapi.responses.RedirectResponse(link)
