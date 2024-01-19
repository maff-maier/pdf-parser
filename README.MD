### PDF converter to JSON

You have to download `.pdf file` in root directory.

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
py main.py filename.pdf
```

## JSON structure
### Schema
```json
{
    "sex": "F",
    "champ_type": "Final",
    "distance": "50m",
    "participants": [
        {
            "range_name": "Девушки (13-14)",
            "persons": [
                {
                    "initials": "ФАМИЛИЯ Имя",
                    "distances": [
                        {
                            "distance": "25m",
                            "sum_time": "12.61",
                            "time": "12.61"
                        },
                        {
                            "distance": "50m",
                            "sum_time": "26.44",
                            "time": "13.83"
                        }
                    ]
                }
            ]
        }
    ]
}
```