local_build:
	@echo "Build local server..."
	docker-compose -f docker-compose-local.yml build

local_up:
	@echo "Up local server..."
	docker-compose -f docker-compose-local.yml up

web_shell:
	docker exec -it noah_django_container /bin/bash