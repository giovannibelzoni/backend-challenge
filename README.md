# The Q-CTRL Back-end Challenge

The goal of this challenge is to create a web-based API using [Django](https://www.djangoproject.com/). The API should be backed by a [MySQL](https://www.mysql.com/) database and conform to the [JSON API](http://jsonapi.org/) specification.

To get started please fork this repository and when you're finished create a pull request.

## Build + Run

Use Docker Compose to build and run. Ensure host port `8000` is available for use.

```
$ docker-compose up -d
```

You may need to run `restart` after first build as database initialisation is slow.

```
$ docker-compose restart
```

Base URL: [http://localhost:8000/](http://localhost:8000/)

## Test

```
$ docker-compose exec app pytest
```

## Endpoints

See tests for examples.

List/Create Pulses:

```
[ GET | POST ] /api/pulse/
```

Update/Delete Pulse:

```
[ PUT | PATCH | DELETE ] /api/pulse/[id]/
```

Download Pulses in CSV format:

```
GET /api/pulse/download/
```

Upload Pulses in CSV format:

```
POST /api/pulse/upload/
```

## Code Test Philosophy + Goals

- Easy bootstrap to ease the pain in assessment
- Leverage community apps to reduce errors and increase eyes on code
- Achieve test goals in least amount of code lines as humanly possible
- Prefer less code / simplicity over handling large input/output and edge cases to save time


## Brief

The brief has been divided into three parts:

1.  [Manage pulses](#manage-pulses)
1.  [Upload pulses](#upload-pulses)
1.  [Download pulses](#download-pulses)

---

### Manage pulses

Implement endpoints that can:

- Create a new pulse
- List all pulses (five per page)
- Get a specific pulse
- Update a specific pulse
- Delete a specific pulse

---

### Upload pulses

Implement an endpoint that can accept a [CSV file](doc/files/pulses.csv) where each row represents a pulse.

---

### Download pulses

Implement an endpoint that returns all pulses in CSV format. The CSV should not include a header row.

---

## Additional Information

Below are the attributes of a pulse. All attributes are required.

| Name              | Type   | Description                                                                         |
|-------------------|--------|-------------------------------------------------------------------------------------|
| name              | string | The name of the pulse (e.g. "My Awesome Pulse")                                     |
| type              | string | The type of pulse. Valid pulse types are: primitive, corpse, gaussian, cinbb, cinsk |
| maximum_rabi_rate | float  | A floating-point number between 0 and 100                                           |
| polar_angle       | float  | A floating-point number between 0 and 1                                             |
