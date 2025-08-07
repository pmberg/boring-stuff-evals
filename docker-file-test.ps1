#Sets a parameter, including a default value if the second argument is omitted
param (
    [string]$FilePath = "basics/docker-file-test.py"
)

# Convert relative path to full path (Docker requires absolute)
$fullPath = Resolve-Path $FilePath

docker run --rm `
  --memory="512m" `
  --network=none `
  -v "$($fullPath):/code/eval.py:ro" `
  python-eval-1 python /code/eval.py