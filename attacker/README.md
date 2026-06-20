# Attacker image

This Dockerfile builds a minimal Alpine-based image with networking/debugging tools used by the attacker service in docker-compose.yml.

To build and run:

```bash
docker-compose up --build attacker
```

You can then attach to the container with:

```bash
docker exec -it attacker sh
```
