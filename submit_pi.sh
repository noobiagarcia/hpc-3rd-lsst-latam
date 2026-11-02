#!/bin/bash

#SBATCH -p cpu_dev
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH -J pi-multiprocessing
#SBATCH --output=/scratch/users/%u/lsst_latam/logs/%x-%j.out

EXEC="/scripts/nubia.garcia/LSST_LATAM/pi_multiprocessing.py"

srun python "$EXEC"
