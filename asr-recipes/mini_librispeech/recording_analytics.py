import os
import subprocess

base_path = "/other/users/vaiaada/asr-tts-class-2021/asr-recipes/mini_librispeech/s5/corpus/LibriSpeech/"
dirs = ["train-clean-5","dev-clean-2"]

analytics = {}
for dir in dirs:
    analytics[dir] = {
        "files": 0, 
        "hours": 0
    }
    for dir_path, directories, files in os.walk(base_path + dir):
        for file in files: 
            file_path = os.path.join(dir_path,file)
            if file_path.endswith(".flac"):
                analytics[dir]["files"] += 1
                duration = subprocess.run(["soxi", "-D", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                duration = float(duration.stdout)
                analytics[dir]["hours"] += duration/3600

    print(f"Folder {dir} contains {analytics[dir]['files']} files and {analytics[dir]['hours']:.2f} hours of recording!")
