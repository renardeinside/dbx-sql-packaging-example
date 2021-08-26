install-in-docker:
	docker run -it -v "$(pwd)/dist:/dist" python:3.7 /bin/bash