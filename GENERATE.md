# Swagger CodeGen

## To regenerate the code

run:
```bash
docker run --rm -v ${PWD}:/local --user 1000:1000 \
    swaggerapi/swagger-codegen-cli-v3 generate \
    -i https://developer.here.com/documentation/routing-api/swagger/v8.yaml \
    -l python \
    --api-package api \
    --model-package models \
    --git-user-id madpin \
    --git-repo-id scg-here-public-transit-api \
    -c /local/config.json \
    -o /local/
```