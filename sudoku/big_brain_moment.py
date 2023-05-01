from flask import Flask, jsonify, request
import sudoku
app = Flask(__name__)

# Initial grid string will be done in web.
grids = []
grid_strings = []


@app.route('/grids')
def get_grids():
    return jsonify(grid_strings)


@app.route('/grids', methods=['POST'])
def add_grids():
    grids.append(request.get_json())
    initial_grid = grids[0]["Grid"]
    initial_string: str = sudoku.print_grid(description="Initial grid", grid=initial_grid)
    solved = sudoku.get_solutions(initial_grid=initial_grid)
    print(solved)
    solved_string: str = ''
    for i, solve in enumerate(solved):
        solved_string += sudoku.print_grid(description=f"solution {i + 1}", grid=solved)
    grid_strings.append({"Initial Grid": initial_string, "Solved Grid": solved_string})
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)