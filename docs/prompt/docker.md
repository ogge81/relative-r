
"Connection refused" means nothing is listening on port 5432. Check these in order:

**1. Start Docker**
```bash
# Start Docker Desktop (or your Docker daemon)
```

**2. Start the Postgres container**
```bash
cd /home/dev/projects/relative-r
docker compose up -d
```

**3. Confirm the container is running**
```bash
docker compose ps
```
You should see the `db` service with status `running`.

**4. Confirm Postgres is listening**
```bash
docker compose logs db
```
Look for something like `database system is ready to accept connections`.

**5. Test the connection**
```bash
docker compose exec db psql -U market -d marketdb -c "SELECT 1"
```

---

**Typical causes**

- Docker daemon not running
- `docker compose up -d` not run yet
- Port 5432 already used by another Postgres (e.g. system install)
- Container exited (check with `docker compose ps` and `docker compose logs db`)

If another Postgres is on 5432, either stop it or change the port in `docker-compose.yml` (e.g. `"5433:5432"`) and set `DB_PORT=5433` in `.env`.