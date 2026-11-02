#!/bin/bash

#SBATCH -p cpu_dev
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH -J pi-multiprocessing
#SBATCH --output=/path/to/%u/lsst_latam/logs/%x-%j.out

EXEC="/path/to/pi_multiprocessing.py"

srun python "$EXEC"
