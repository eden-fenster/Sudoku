document.write('<!DOCTYPE html>');
document.write('<html lang="en">');
document.write('<head>');
document.write('    <title>Sudoku Solver Server</title>');
document.write('</head>');
document.write('   <body>');
document.write('      <form action = "http://localhost:5000/results" method = "POST"');
document.write('         enctype = "multipart/form-data">');
document.write('         <p>Welcome to the Sudoku Solver server, upload a file.</p>');
document.write('         <input type = "file" name = "file" accept=".txt"/>');
document.write('         <input type = "submit" value="Upload"/>');
document.write('      </form>');
document.write('   </body>');
document.write('</html>');