from server_template import Server


DEFAULT_PATH = "/Index.html"


class SudokuServer(Server):
    super().do_GET(path=DEFAULT_PATH)
