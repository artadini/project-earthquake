.PHONY: niko help prod stop logs terminal commit
.DEFAULT_GOAL := help

prod: # delete pull changes build and run a new container
	git pull
	docker build -t project-earthquake:latest .
	docker rm -f project-earthquake
	docker run -d --name project-earthquake --restart=always -v $(shell pwd)/failed:/failed -v $(shell pwd)/files:/files project-earthquake:latest
	docker logs -f project-earthquake --since 60m

stop: # stop the running container
	docker stop project-earthquake

logs: # show logs of the running container
	docker logs -f project-earthquake --since 60m

terminal: # open a terminal in the running container
	docker exec -it project-earthquake bash

commit: # commit changes to the git repository
	git add .
	git commit -m "Committing changes"
	git push

help: # show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'