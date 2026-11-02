import nbformat

# Cria um notebook Jupyter simples
nb = nbformat.v4.new_notebook()

nb.cells = [

    nbformat.v4.new_markdown_cell(

        "# Multiplicação de matrizes\n"

        "Exemplo simples gerado por um job Slurm."

    ),

    nbformat.v4.new_code_cell(

        "import numpy as np\n\n"

        "A = np.array([[1, 2], [3, 4]])\n"

        "B = np.array([[5, 6], [7, 8]])\n\n"

        "print('Matriz A:')\n"

        "print(A)\n\n"

        "print('\\nMatriz B:')\n"

        "print(B)\n\n"

        "resultado = A @ B\n"

        "print('\\nResultado de A x B:')\n"

        "print(resultado)"

    )
]

nb.metadata = {

    "kernelspec": {

        "display_name": "Python 3",

        "language": "python",

        "name": "python3"

    }

}



with open("multiplicacao_matrizes.ipynb", "w", encoding="utf-8") as arquivo:

    nbformat.write(nb, arquivo)



print("Notebook criado: multiplicacao_matrizes.ipynb")
