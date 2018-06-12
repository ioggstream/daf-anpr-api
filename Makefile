
YAML=$(shell find * -name \*yaml)
YAMLSRC=$(shell find openapi -name \*yaml.src)
YAMLGEN=$(patsubst %.yaml.src,%.yaml,$(YAMLSRC))


yaml: $(YAMLGEN)

%.yaml: %.yaml.src
	. .tox/py36/bin/activate
	yamllint $<
	python ./scripts/yaml-resolver.py $< $@

#
# dataloader
#
prepare:
	which git-lfs || curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash && apt -y install git-lfs
	git lfs pull

setup: prepare
	docker-compose up -d elastic kibana
	docker-compose up dataloader


yamllint: $(YAML)
	. .tox/py36/bin/activate
	yamllint $?

# Create a simple project starting from OpenAPI v3 spec
#  in simple.yaml.
prj-simple-generate: openapi/core-vocabularies.yaml
	# Convert OpenAPI v3 to a temporary Swagger 2.0 using
	#  docker image ioggstream/api-spec-converter
	./scripts/openapi2swagger.sh openapi/core-vocabularies.yaml > /tmp/swagger.yaml

	# Generate a flask client from v2 spec using
	#  docker image swaggerapi/swagger-codegen-cli
	./scripts/generate-flask.sh /tmp/swagger.yaml  ./prj-simple/

prj-simple: prj-simple-generate
	docker-compose up --build test


prj-simple-quickstart: prj-simple-generate
	# Revert files changed by the codegen.
	git checkout -- prj-simple
	# Test all
	docker-compose up --build test
	# Build and run the application
	docker-compose up simple

