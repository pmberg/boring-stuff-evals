# How prior work on AI evals has been done

This section focuses on the methodology used to perform previous AI evals. It does not focus on precisely what those evals have found, but rather on which of their methodology can be borrowed for the sake of consistency.

Existing repos along these lines are OpenAI's evals package and EleutherAI's lm-evaluation-harness package. 

Taking OpenAI's evals package as an example, the package contains a runner that takes in command line calls and then:

1. Takes in a prompt from a dataset
2. Makes an API call to the language model being tested, based on the prompt, and
3. Checks it, using either software tests like assert statements or another LLM as a "judge" against ground truth in the dataset 

Since model output here is not necessarily trusted code, one should always wrap any code-generation evals in a security sandbox. A common approach for sandboxing seems to be the use of a Docker container to constrain network access, CPU access, and RAM use. Often, this could involve cutting off Internet access altogether, but in cases where it does need Internet access to run (e.g. web scraping evals) one can limit access to only certain websites or restrict the frequency of HTTP calls.