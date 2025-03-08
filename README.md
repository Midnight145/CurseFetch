# CurseFetch

This is a maven repo that allows you to fetch files that are not accessible through the CurseForge API due to the mod requiring website interaction to download the file.
This repo is designed to be used alongside CurseMaven, not a replacement, as CurseMaven is significantly more flexible.

There is currently a public repo hosted at `https://uncomfortable-fey-midnight145-884fba2b.koyeb.app/`.

This project is licensed under the LGPL3 license.

## Usage:

Gradle:
```
repositories {
    maven {
        url "https://uncomfortable-fey-midnight145-884fba2b.koyeb.app"
        content {
            includeGroup "curse.fetch"
        }
    }
}
```

dependencies:
```
compile("curse.fetch:<fileid>:<filename>:<extension>")
```

For example, to fetch [Thaumcraft 4](https://www.curseforge.com/minecraft/mc-mods/thaumcraft/files/2227552):
```
compile("curse.fetch:2227552:Thaumcraft-1.7.10-4.2.3.5:jar")
```

# Self Hosting:

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    
3. Run the app
    ```sh
    python -m uvicorn main:app --host 0.0.0.0 --port <port>
    ```

4. Access your instance at `localhost:<port>`
