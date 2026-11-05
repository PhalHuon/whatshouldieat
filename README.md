# whatshouldieat

## Requirements
 
You only need Docker Engine and Docker Compose v2 on any Linux distribution. No Python or Postgres is needed on your machine.
 
Check your setup:
 
```
docker --version
docker compose version
docker run hello-world
```
 
1. The second command must print version 2 or higher. If it fails, install the Compose plugin from Docker's official apt repository.
2. The third command must work without sudo. If it says permission denied, run `sudo usermod -aG docker $USER`, then log out and back in.
## Setup
 
1. Clone the repo and enter the project folder:
```
git clone <repo url>
cd whatshouldieat
```
 
2. Create your environment file from the example and fill in the values:
```
cp .env.example .env
```
 
3. Build and start the app and database:
```
docker compose up --build
```
 
Wait until the db service reports it is ready and Django prints that the server started.
 
4. In a second terminal, from the same folder, create the database tables:
```
docker compose run app python manage.py migrate
```
 
5. Optional: create an admin login:
```
docker compose run app python manage.py createsuperuser
```
 
6. Open http://localhost:8000 in your browser.
