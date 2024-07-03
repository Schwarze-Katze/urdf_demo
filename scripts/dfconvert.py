import os
import subprocess
import sys

def convert_urdf_to_sdf(urdf_path, sdf_path):
    try:
        subprocess.check_call(['gz', 'sdf', '-p', urdf_path], stdout=open(sdf_path, 'w'))
        print(f"Successfully converted {urdf_path} to {sdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting URDF to SDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    urdf_path = sys.argv[1]
    sdf_path = sys.argv[2]
    convert_urdf_to_sdf(urdf_path, sdf_path)
