LOCAL_SERVER 	= "http:\\/\\/localhost:5001"
PROD_SERVER 	= "http:\\/\\/server.jawsapps.com\\/bikerite"
HOST_REGEX		= "host\:\ \'[a-zA-Z0-9:/.]*\'"

env_local:
	@sed -i "" -e "s/$(HOST_REGEX)/host: '$(LOCAL_SERVER)'/g" ./public/index.html

env_prod:
	@sed -i "" -e "s/$(HOST_REGEX)/host: '$(PROD_SERVER)'/g" ./public/index.html

compile:
	@./node_modules/.bin/hem build

upload:
	@s3cmd sync --acl-public ./public/ s3://bikerite.jawsapps.com

clean:
	@rm -f ./public/application.*

deploy: clean compile env_prod upload env_local clean
