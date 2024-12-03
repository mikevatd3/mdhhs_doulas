from pathlib import Path
import json
import logging
import logging.config
from sqlalchemy import create_engine
import tomli


# Walk out the the module base path
with open(Path().cwd() / "config.toml", "rb") as f:
    app_config = tomli.load(f)


db_engine = create_engine(
    f"postgresql+psycopg2://{app_config['db']['user']}:{app_config['db']['password']}"
    f"@{app_config['db']['host']}:{app_config['db']['port']}/{app_config['db']['name']}",
    connect_args={'options': f'-csearch_path={app_config["app"]["name"]},public'}
)


def setup_logging():
    with open(Path.cwd() / "logging_config.json") as f:
        logging_config = json.load(f)

    logging.config.dictConfig(logging_config)
