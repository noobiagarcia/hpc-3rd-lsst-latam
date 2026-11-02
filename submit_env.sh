#!/bin/bash

#SBATCH -p cpu_dev
#SBATCH --ntasks=1
#SBATCH -J my_notebook
#SBATCH --output=/scratch/users/%u/lsst_latam/logs/%x_%j.out

ENV="/scripts/nubia.garcia/LSST_LATAM/lsst_latam_env"

source /opt/conda/etc/profile.d/conda.sh
conda activate "$ENV"

EXEC="/scripts/nubia.garcia/LSST_LATAM/my_notebook.py"

srun python "EXEC"
