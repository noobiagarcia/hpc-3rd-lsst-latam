import nbformat
import numpy
import astropy


nb = nbformat.v4.new_notebook()

nb.cells = [

    nbformat.v4.new_markdown_cell(

        "# Matrix Multiplication \n"

        "Simple example."

    ),

    nbformat.v4.new_code_cell(

        "import numpy as np\n\n"

        "A = np.array([[1, 2], [3, 4]])\n"

        "B = np.array([[5, 6], [7, 8]])\n\n"

        "print('Matrix A:')\n"

        "print(A)\n\n"

        "print('\\nMatrix B:')\n"

        "print(B)\n\n"

        "value = A @ B\n"

        "print('\\nA x B:')\n"

        "print(value)"

    )
]

nb.metadata = {

    "kernelspec": {

        "display_name": "Python 3",

        "language": "python",

        "name": "python3"

    }

}



with open("matrix_multiplication.ipynb", "w", encoding="utf-8") as arquivo:

    nbformat.write(nb, arquivo)



print("Notebook created: matrix_multiplication.ipynb")
