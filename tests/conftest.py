def pytest_addoption(parser):
    parser.addoption("--full", action="store_true", help="run all tests")
    parser.addoption("--api", action="store_true", help="run api tests")
    parser.addoption("--db", action="store_true", help="run database tests")


def pytest_configure(config):
    if config.getoption("--full"):
        # If --full is specified, clear any markers
        config.option.markexpr = ""
    elif config.getoption("--api"):
        # If --api is specified, only run api tests
        config.option.markexpr = "api"
    elif config.getoption("--db"):
        # If --db is specified, only run db tests
        config.option.markexpr = "db"
    else:
        # If no option is specified, exclude api and db tests
        config.option.markexpr = "not api and not db"