import pathlib

file = pathlib.Path(__file__)
root_dir = file.parent.parent.parent
package_src = root_dir / "fastapicrud"


def test_py_typed_file_exists():
    assert (package_src / "py.typed").exists()
    assert (package_src / "py.typed").is_file()


def test_virtualenv(virtualenv):
    assert (root_dir).exists()
    assert (root_dir / "setup.py").exists()

    virtualenv.run(f"pip install -e {root_dir}")
    virtualenv.run(f"pip install mypy")
    virtualenv.run(f"mypy {file}")


if __name__ == "__main__":
    from pydantic import BaseModel
    from fastapi import FastAPI

    import fastapicrud

    class User(BaseModel):
        id: int
        name: str
        email: str

    router = fastapicrud.MemoryCRUDRouter(schema=User)
    app = FastAPI()
    app.include_router(router)
