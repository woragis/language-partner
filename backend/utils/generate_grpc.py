# Errors
# 1 -> No argument provided
# 2 -> File not found
# 3 -> Error creating grpc

from sys import argv, exit
import subprocess
from pathlib import Path

# Paths
PROTO_DIR = Path("proto")
OUT_DIR = Path("generated")


def generate_grpc(file_name: str):
    if not PROTO_DIR.exists():
        print(f"❌ Directory {PROTO_DIR} not found.")
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    proto_path = PROTO_DIR / file_name
    if not proto_path.exists():
        print(f"❌ File not found: {proto_path}")
        return exit(2)

    print(f"🔧 Compiling {proto_path}...")

    command = [
        "python", "-m", "grpc_tools.protoc",
        f"-I{PROTO_DIR}",
        f"--python_out={OUT_DIR}",
        f"--grpc_python_out={OUT_DIR}",
        str(proto_path)
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ Failed to compile {proto_path}")
        print(result.stderr)
        return exit(3)
    else:
        print(f"✅ Generated gRPC code for {file_name}")


def get_argv():
    if len(argv) < 2:
        print(
            "❌ You need to provide a proto filename. Example: python generate_grpc.py greeter")
        return None
    proto_file = argv[1]
    if proto_file.endswith('.proto'):
        return proto_file
    return f"{proto_file}.proto"


if __name__ == "__main__":
    proto_file_name = get_argv()
    if proto_file_name:
        generate_grpc(proto_file_name)
        exit(0)
    else:
        exit(1)
