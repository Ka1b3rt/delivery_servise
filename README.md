# SUPERB Delivery

## Delivery service web API
**For academic purpose only**

Supporting features:
- Add\Get parcel
- Parcels bind to user session
- Automatic delivery-cost calc depends on actual exchange rate USD/RUB

**Installation**
1. Clone repo
```commandline
git clone https://github.com/Simonstools/delivery_service.git \
&& cd delivery_service \
&& git checkout dev
```
2. Setup .env file relying on .envexample, but it does not require. App will be launched properly with current settings in .envexample file, if changes will not be perfomed then just rename .envexample to .env.
```commandline
mv .env.example .env
```
3. Build and run application
```commandline
docker-compose up --build -d
```

**API endpoints**

GET
```
/parcel
/parcel_types
/update_rate
```

POST
```
/parcel
```

**Testing**

Prepare .venv
```commandline
uv sync --frozen \
&& source .venv/bin/activate
```
Run tests
```commandline
pytest
```
