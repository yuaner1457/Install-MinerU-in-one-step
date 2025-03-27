import subprocess as sp
import json

ret = sp.run(
    "pip install -U magic-pdf[full] --extra-index-url https://wheels.myhloli.com",
    shell=True,
    encoding="utf-8",
)
if ret.returncode != 0:
    raise ValueError(f"Pip install magic-pdf Error: {ret.stderr}")
ret = sp.run("pip install huggingface_hub", shell=True, encoding="utf-8")
if ret.returncode != 0:
    raise ValueError(f"Pip install huggingface_hub Error: {ret.stderr}")
ret = sp.run("python -u Everything_to_markdown.py", shell=True, encoding="utf-8")
if ret.returncode != 0:
    raise ValueError(f"Download models Error: {ret.stderr}")
filepath = ret.stdout
print(f'User File Path{filepath}')
with open(filepath, "r", encoding="utf-8") as file:
    data = json.load(file)
data["device-mode"] = "cuda"
with open(filepath, "w", encoding="utf-8") as file:
    json.dump(data, file)
ret = sp.run(
    "python -m pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/",
    shell=True,
    encoding="utf-8",
)
if ret.returncode != 0:
    raise ValueError(f"CUDA accelerate init Error: {ret.stderr}")
print("magic-pdf install success")