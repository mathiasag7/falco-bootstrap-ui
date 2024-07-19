set dotenv-load := true

# List all available commands
_default:
    @just --list --unsorted


@run-demo:
    cd demo && hatch run python manage.py tailwind runserver