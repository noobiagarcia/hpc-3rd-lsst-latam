#!/bin/bash

#SBATCH -p cpu_dev
#SBATCH -N 1
#SBATCH -J pi-serial
#SBATCH --output=/path/to/%u/lsst_latam/logs/%x-%j.out

EXEC="/path/to/code/pi_serial.py"

srun python "$EXEC"
