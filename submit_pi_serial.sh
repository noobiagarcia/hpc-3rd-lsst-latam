#!/bin/bash

#SBATCH --partition=cpu_dev                   #Partition Name
#SBATCH -J pi-serial                          #Job Name
#SBATCH --output=/path/to/%u/lsst_latam/logs/%x-%j.out #Path to output

EXEC="/path/to/code/pi_serial.py"

srun python "$EXEC"
