# Description   
This repository demonstrates how the mechanism for handling links can be implemented using processes and threads.
A thousand links with this implementation on 8 cores work out for:
```text
 data processed with time 44.96057987213135 
```
python 3.10

# Running app
There are two ways to launch an application.

- On bare metal:
Then you need install packages with command: 
```text
    pip3 install -r requirements.txt --no-cache-dir
```
after that just run:
```shell
  python3.10 main.py
```
- Or in a docker container:
```shell
  docker-compose up --build
```

# Running Tests
```shell
    pytest
```

## Notes
I have 8 cores, so I did not describe the behavior when the number of links is divided with the remainder.
This problem could be solved by adding the rest of the links to the last thread along with the main chunk.
Please keep this in mind.
