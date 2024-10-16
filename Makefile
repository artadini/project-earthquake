.PHONY: niko help prod stop logs terminal commit
.DEFAULT_GOAL := help

prod: # delete pull changes build and run a new container
	git pull
	docker build -t project-earthquake:latest .
	docker run -p 8000:8000 project-earthquake:latest

run: # run the container
	docker run -p 8000:8000 project-earthquake:latest

logs: # show logs of the running container
	docker logs -f project-earthquake --since 60m