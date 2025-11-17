import subprocess

subprocess.call(["python", "Scripts/ProcessingScripts/analiza_zysku.py"])
subprocess.call(["python", "Scripts/AnalysisScripts/przetworzone_kolumny.py"])
subprocess.call(["python", "Scripts/AnalysisScripts/date_posprocesingowe.py"])
subprocess.call(["python", "Scripts/ProcessingScripts/modelowanie.py"])