# exam-task-mentee

## Mentee Robotics landing page

Run the Python web app with:

```sh
python3 -m app.app
```

The app requires Python 3.11 or newer. Its semantic version is defined in
`pyproject.toml` and displayed on the landing page. Then open
http://localhost:8000. Set the `PORT` environment variable to use a different
port.

## Docker

Build and run the production image:

```sh
docker build -t mentee-robotics .
docker run --rm -p 8000:8000 mentee-robotics
```

The container runs Gunicorn as a non-root user and includes a `/health`
endpoint for its Docker health check.