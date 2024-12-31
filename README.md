# CurseFetch

This is a repo that allows you to fetch files that are not accessible through the CurseForge API due to the mod requiring website interaction to download the file.
This repo is designed to be used alongside CurseMaven, not a replacement, as CurseMaven is significantly more powerful flexible.

Currently, there is no public instance of this repo, so you will need to host it yourself.

This project is licensed under the LGPL3 license.

## Usage:

Gradle:
```
repositories {
    maven {
        url "curse-fetch-url"
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
