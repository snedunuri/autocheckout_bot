from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

USER_AGENT_REL_PATH = Path('data/user_agents.txt').resolve()
USER_AGENT_DATA_PATH = BASE_DIR.joinpath(USER_AGENT_REL_PATH)
