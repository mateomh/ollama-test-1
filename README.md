# OLLAMA TEST

This is a project to learn how to use Ollama to run LLMs locally using docker. It also uses Python Langchain to communicate and make the prompts that are passed to the LLM.

## Spin up the application

This application has two parts, the first part is the Ollama server that is set up to run with Docker, all you have to do to get it running is to run the following command

```
docker compose up
```

The second part is the actual script that interacts with the LLM, that one is built with python virtual environments suing `pipenv`, so to run that part of the application you have to run:

```
pipenv install
pipenv shell
python3 main.py
```

You might have to install `pipenv` in your machine to run it.

