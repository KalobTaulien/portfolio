This is a clone of the [wagtail-basic-portfolio](https://github.com/stevedya/wagtail-basic-portfolio) repo.

## Running the project

This project can use Docker for it's virtual enviroment. Or a standard venv, Pipenv, virtualenv, etc.

### Docker
To get up and running with Docker:

```bash
make build
make up
make enter
python manage.py runserver 0.0.0.0:8000
```

### Venv
To get up and running with venv

```bash
python -m venv .venv
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

## Frontend assets

Make sure you compile your front end assets with:
```bash
npm install
npm run build
```

### Frontend development commands
```bash
npm run build
npm run watch
npm run dist
```

1. Run `npm run build` to run the development build (creates/updates .css and .js files)
2. Run `npm run watch` if you're actively updating your frontend code
3. Run `npm run dist` to minify your .css and .js files for production
