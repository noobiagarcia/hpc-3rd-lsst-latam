#!/bin/bash

#SBATCH -p cpu_dev
#SBATCH -J my_notebook
#SBATCH --output=/path/to/%u/lsst_latam/logs/%x_%j.out

ENV="/path/to/env"

source /opt/conda/etc/profile.d/conda.sh
conda activate "$ENV"

EXEC="/path/to/my_notebook.py"

srun python "$EXEC"
