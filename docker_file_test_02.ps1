docker run --rm `
  --memory="512m" `
  --network=none `
  -v "$(PWD)/basics/docker_file_test.py:/code/eval.py:ro" `
  python-eval-1 python /code/eval.py