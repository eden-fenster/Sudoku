from server_template import Server


DEFAULT_PATH = "index.html"


class SudokuServer(Server):
    super().do_GET(path=DEFAULT_PATH)
