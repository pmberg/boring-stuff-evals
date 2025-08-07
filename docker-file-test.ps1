$volumePath = "${PWD.Path}/basics/docker-file-test.py:/code/docker-file-test.py:ro"

docker run --rm `
  --memory="512m" `
  --network=none `
  -v "C:/Users/pmbpa/OneDrive/Documents/Summer-2025-Internship/boring-stuff-evals/basics/docker-file-test.py:/code/docker-file-test.py:ro" `
  python-eval-1 python /code/docker-file-test.py