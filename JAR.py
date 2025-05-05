import os
import zipfile
import subprocess

def extract_jar(jar_path, extract_to):
    with zipfile.ZipFile(jar_path, 'r') as jar:
        jar.extractall(extract_to)
        print(f"Extracted {jar_path} to {extract_to}")

def decompile_class_files(decompiled_dir):
    for root, dirs, files in os.walk(decompiled_dir):
        for file in files:
            if file.endswith(".class"):
                class_file_path = os.path.join(root, file)
                decompile_to_java(class_file_path, root)

def decompile_to_java(class_file_path, output_dir):
    try:
        subprocess.run(['jadx', '--output-dir', output_dir, class_file_path], check=True)
        print(f"Decompiled {class_file_path} to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error decompiling {class_file_path}: {e}")

def main():
    jar_path = r'C:\Users\PieMu\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\dist\Jar\AbsoluteLayout.jar'  # Update this with the path to your JAR file
    extract_to = 'extracted_files'  # Directory to extract the JAR contents
    decompiled_dir = 'decompiled_files'  # Directory to save decompiled .java files

    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    if not os.path.exists(decompiled_dir):
        os.makedirs(decompiled_dir)

    extract_jar(jar_path, extract_to)
    decompile_class_files(decompiled_dir)

if __name__ == "__main__":
    main()
