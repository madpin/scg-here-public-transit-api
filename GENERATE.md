# Swagger CodeGen

## To regenerate the code

run:
```bash
docker run --rm -v ${PWD}:/local --user 1000:1000 \
    swaggerapi/swagger-codegen-cli-v3 generate \
    -i https://developer.here.com/documentation/public-transit/swagger/transit_api.yaml \
    -l python \
    --api-package api \
    --model-package models \
    --git-user-id madpin \
    --git-repo-id scg-here-public-transit-api \
    --ignore-file-override .\
    -c /local/config.json \
    -o /local/
```

To remove the current run:
```bash
rm -rf .swagger-codegen-ignore .travis.yml git_push.sh README.md \
   requirements.txt setup.py test-requirements.txt tox.ini .swagger-codegen \
   docs here_public_transit_api test
```