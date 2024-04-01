import pathlib
from dataclasses import dataclass
from typing import Any

from jinja2 import Environment, FileSystemLoader
from sqlalchemy import Engine, text

TEST_DATA_DIR = pathlib.Path(__file__).parent / "test_data"


def render_sql_template(template_file: pathlib.Path, **kwargs) -> str:
    env = Environment(loader=FileSystemLoader(template_file.parent))
    template = env.get_template(template_file.name)
    return template.render(**kwargs)


@dataclass
class TestData:
    template: pathlib.Path
    params: list[dict[str, Any]]


def add_test_data(db_engine: Engine, test_data: list[TestData]):
    with db_engine.connect() as connection:
        for td in test_data:
            sql = render_sql_template(td.template, rows=td.params)
            connection.execute(text(sql))

        connection.commit()
