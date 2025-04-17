import sys
import os
import asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from evaluations.Architecture import start_analysis

# run with async
if __name__ == "__main__":
    asyncio.run(start_analysis())
