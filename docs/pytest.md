# Pytest

The 2 most popular packages for testing are [`unittest`](https://docs.python.org/3/library/unittest.html) and [`pytest`](https://docs.pytest.org/), but [others](https://www.softwaretestinghelp.com/python-testing-frameworks/) also exists. `unittest` is part of Python standard library. We currently use `pytest` as it allows compact test suites, special and simple class fixtures to facilitate testing.

The [Pytest Testing article on the Real Python website](https://realpython.com/pytest-python-testing/) gives a good description of the functionality of `pytest` and compares it to `unittest`. Most of the current examples in the documentation come from there, so see this original article and the [official Pytest documentation](https://docs.pytest.org/) for a complete description.


Run tests with:
```sh
pytest
```

## Pytest features

- Runs test written for `unittest` framework.
- Files prefixed with `test_` will be automatically run as tests.
- Check for [markers](https://docs.pytest.org/en/latest/how-to/mark.html#registering-marks) in the `pytest.ini` config file. Otherwise markers could be mistyped and forgot when the number of tests grows.    
     ```sh
    pytest --strict-markers
    ```

    Define markers in the `pytest.ini` file. (`.toml` file could be also used)
    ```ini
    [pytest]
    markers =
        slow: marks tests as slow (deselect with '-m "not slow"')
        network_access
    ```

    Run tests with a specific marker only:
    ```sh
    pytest -m network_access
    ```

    Deselect some tests:
    ```sh
    pytest -m "not slow"
    ```


    Pytest provides a few marks out of the box:

    - **skip** skips a test unconditionally.
    - **skipif** skips a test if the expression passed to it evaluates to True.
    - **xfail** indicates that a test is expected to fail, so if the test does fail, the overall suite can still result in a passing status.
    - **parametrize** creates multiple variants of a test with different values as arguments. You’ll learn more about this mark shortly.

- Show the `n` slowest tests:
    ```sh
    pytest --durations n
    ```
- Check code coverage
    ```sh
    pip install pytest-cov
    pytest --cov=mymodule tests/
    ```
- [Fixtures](https://docs.pytest.org/en/7.2.x/explanation/fixtures.html#about-fixtures) provide a context for each test. They can be used for common and generic parts such as example input.
    ```py
    @pytest.fixture
    def users():
        return [
            {"id": 1, "name": "foo"},
            {"id": 2, "name": "bar"}
        ]
    ```
    Use the previously defined fixture as a parameter.
    ```py
    def test_users(users):
        assert users[1]["name"] == "bar"
    ```
- `conftest.py` file contains common fixtures and other generic overrides, such as disabling all network connection through the `request.get` command.