def pytest_addoption(parser):
    parser.addoption(["--full", "-f"], action="store_true", help="run all tests")

def pytest_configure(config):
    if config.getoption("full"):
        config.option.markexpr = config.getini("addopts_full")