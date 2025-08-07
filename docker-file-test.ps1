docker run --rm `
  --memory="512m" `
  --network=none `
  -v "$(pwd)/basics/docker-file-test.py:/code/docker-file-test.py:ro" `
  python-eval-1 python /code/docker-file-test.py