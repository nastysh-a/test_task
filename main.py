from dotenv import load_dotenv
import os, sys
import inp

load_dotenv("env.env")
SUPPORTED_LENS = list(map(int, os.getenv("SUPPORTED_LENS").split(",")))

if __name__ == "__main__":
    inp.cli()