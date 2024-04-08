### PDF converter to JSON

Install venv:
```sh
py -m venv venv
```

Install dependencies:
```sh
pip install -r requirements.txt
```

Run program with:
```sh
uvicorn main:app --reload
```

## Request JSON structure
### Schema
```json
{
    "files": bfile
}
```


## Response JSON structure
### Schema
```json
{
    "distance": "100m",
    "swimmers": [
        {
            "initials": "ФАМИЛИЯ Имя",
            "distances": [
                {
                    "distance": "50m",
                    "time": "12.61",
                    "total": "12.61"
                },
                {
                    "distance": "100m",
                    "time": "13.83",
                    "total": "26.44",
                }
            ]
        }
    ]
}
```
