#!/bin/bash

# read and validate arguments
SETUP_ARG="setup"
RUN_ARG="run"
DOWN_ARG="down"
KNOWN_ARGS=("$SETUP_ARG", "$RUN_ARG", "$DOWN_ARG")

CMD_ARG=$1
if [ -z "${CMD_ARG}" ] || [[ ! " ${KNOWN_ARGS[*]} " =~ ${CMD_ARG} ]]; then
    ERR_MSG="must set one of the following args: ${KNOWN_ARGS[*]}"
    echo "$ERR_MSG"

    return 2>/dev/null || exit
fi

### snippet for getting current script dir ###
SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
  SOURCE=$(readlink "$SOURCE")
  # if $SOURCE was a relative symlink,
  # we need to resolve it relative to the path where the symlink file was located
  [[ $SOURCE != /* ]] && SOURCE=$DIR/$SOURCE
done
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
### end of snippet ###

DOCKERFILE_PATH="${DIR}/../compose.yaml"
# prepare local repository for development environment
if [[ "$CMD_ARG" == "$SETUP_ARG" ]]; then
    echo "Setting up local repository for development environment..."
    LOCAL_FOLDER="${DIR}/../local"
    mkdir "$LOCAL_FOLDER"
    touch "${LOCAL_FOLDER}/.env"
    # add development settings
    echo "DJANGO_SETTINGS_MODULE=config.development" >> "${LOCAL_FOLDER}/.env"
    echo "RUN_DAP_PROCESS=True" >> "${LOCAL_FOLDER}/.env"
    echo "DATABASE_URL=\"pgsql://backend-jw:backend-jw@postgres:5432/dev-jw\"" >> "${LOCAL_FOLDER}/.env"
# run the local repository
elif [[ "$CMD_ARG" == "$RUN_ARG" ]]; then
    echo "Running local repository..."
    PRE_UP_ARGS=""
    POST_UP_ARGS=""
    save_next_var=false
    for var in "${@:2}"
    do
        # some arguments as profile need to appear before up command
        if [[ $var =~ ^--profile.* ]]; then
            save_next_var=true
            PRE_UP_ARGS+="$var "
        else
            if [ $save_next_var == true ]; then
                PRE_UP_ARGS+="$var "
                save_next_var=false
            else
                POST_UP_ARGS+="$var "
            fi
        fi
    done
    if [ -z "${PRE_UP_ARGS}" ]; then
        PRE_UP_ARGS="--profile backend" # defaults to backend profile
    fi
    # shellcheck disable=SC2086
    docker compose --file "$DOCKERFILE_PATH" $PRE_UP_ARGS up -d $POST_UP_ARGS --remove-orphans
# stop the local repository
elif [[ "$CMD_ARG" == "$DOWN_ARG" ]]; then
    echo "Stopping local repository..."
    docker compose --file "$DOCKERFILE_PATH" --profile "*" down
fi
