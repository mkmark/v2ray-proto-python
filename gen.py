# %%
import os
from grpc_tools import protoc


def generate_proto_files(proto_dir, output_dir, import_prefix):
    # Recursively find all .proto files in the specified directory
    proto_files = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(proto_dir)
        for file in files
        if file.endswith(".proto")
    ]

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate protobuf files using grpc_tools.protoc
    for proto_file in proto_files:
        output_file = os.path.relpath(proto_file, proto_dir)
        output_pb2_file = os.path.join(
            output_dir, os.path.splitext(output_file)[0] + "_pb2.py"
        )
        output_pb2_grpc_file = os.path.join(
            output_dir, os.path.splitext(output_file)[0] + "_pb2_grpc.py"
        )

        # Use grpc_tools.protoc to generate the protobuf files
        protoc.main(
            [
                "grpc_tools.protoc",
                "--proto_path={}".format(proto_dir),
                "--python_out={}".format(output_dir),
                "--grpc_python_out={}".format(output_dir),
                proto_file,
            ]
        )

        modify_import_paths(output_pb2_file, import_prefix)
        modify_import_paths(output_pb2_grpc_file, import_prefix)


def modify_import_paths(file_path: str, import_prefix):
    with open(file_path, "r") as file:
        content = file.read()

    # Add the import prefix to the generated file
    for base_path in ["app", "common", "proxy", "transport", "config_pb2"]:
        content = content.replace(
            f"\nimport {base_path}", f"\nimport {import_prefix}.{base_path}"
        )
        content = content.replace(
            f"\nfrom {base_path}", f"\nfrom {import_prefix}.{base_path}"
        )

    with open(file_path, "w") as file:
        file.write(content)
    pass


def create_init_files(directory):
    # Add __init__.py to the root directory
    root_init_file_path = os.path.join(directory, "__init__.py")
    if not os.path.exists(root_init_file_path):
        with open(root_init_file_path, "w") as root_init_file:
            pass
        print(f"Created {root_init_file_path}")

    # Add __init__.py to each subdirectory
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            init_file_path = os.path.join(root, dir_name, "__init__.py")
            if not os.path.exists(init_file_path):
                with open(init_file_path, "w") as init_file:
                    pass
                print(f"Created {init_file_path}")


if __name__ == "__main__":
    # Replace 'lib/v2ray-core' and 'lib/v2ray-core-proto' with your actual paths
    # proto_dir = "lib/v2ray-core"
    # output_dir = "v2ray_proto"
    # import_prefix = "v2ray_proto"

    # generate_proto_files(proto_dir, output_dir, import_prefix)
    # create_init_files(output_dir)

    proto_dir = "lib/xray-core"
    output_dir = "xray_proto"
    import_prefix = "xray_proto"

    generate_proto_files(proto_dir, output_dir, import_prefix)
    create_init_files(output_dir)
