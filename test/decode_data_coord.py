import csv
import pandas as pd

coord = [
    {
        "deviceId": 256,
        "position": [
            {
                "lng": "103.358614",
                "lat": "29.920493",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357401",
                "lat": "29.920921",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357428",
                "lat": "29.921254",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.357419",
                    "lat": "29.921145",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357428",
                    "lat": "29.921254",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.35741",
                    "lat": "29.921029",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357413",
                    "lat": "29.92107",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357413",
                    "lat": "29.92107",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357428",
                    "lat": "29.921254",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357485",
                    "lat": "29.920891",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357401",
                    "lat": "29.920921",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357401",
                    "lat": "29.920921",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357428",
                    "lat": "29.921254",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357603",
                    "lat": "29.92085",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357401",
                    "lat": "29.920921",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357401",
                    "lat": "29.920921",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357413",
                    "lat": "29.92107",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357413",
                    "lat": "29.92107",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357416",
                    "lat": "29.921103",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357781",
                    "lat": "29.920787",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357401",
                    "lat": "29.920921",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357401",
                    "lat": "29.920921",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357402",
                    "lat": "29.920937",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358014",
                    "lat": "29.920705",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357797",
                    "lat": "29.920781",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357797",
                    "lat": "29.920781",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357635",
                    "lat": "29.920838",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358134",
                    "lat": "29.920662",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357797",
                    "lat": "29.920781",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357797",
                    "lat": "29.920781",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357755",
                    "lat": "29.920796",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358387",
                    "lat": "29.920573",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357989",
                    "lat": "29.920714",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358588",
                    "lat": "29.920502",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358136",
                    "lat": "29.920662",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358614",
                    "lat": "29.920493",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358464",
                    "lat": "29.920546",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 257,
        "position": [
            {
                "lng": "103.357539",
                "lat": "29.914197",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.35747",
                "lat": "29.914147",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.357539",
                    "lat": "29.914197",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35747",
                    "lat": "29.914147",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357471",
                    "lat": "29.914148",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35747",
                    "lat": "29.914147",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 258,
        "position": [
            {
                "lng": "103.362447",
                "lat": "29.917809",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362628",
                "lat": "29.917967",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.362447",
                    "lat": "29.917809",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362461",
                    "lat": "29.917821",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362447",
                    "lat": "29.917809",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36249",
                    "lat": "29.917847",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362447",
                    "lat": "29.917809",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362628",
                    "lat": "29.917967",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 259,
        "position": [
            {
                "lng": "103.362647",
                "lat": "29.917984",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362665",
                "lat": "29.918001",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363208",
                "lat": "29.918502",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363424",
                "lat": "29.918706",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363756",
                "lat": "29.919101",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363873",
                "lat": "29.919238",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364125",
                "lat": "29.919598",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364275",
                "lat": "29.919819",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364539",
                "lat": "29.920341",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364903",
                "lat": "29.921192",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364987",
                "lat": "29.92146",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36509",
                "lat": "29.921818",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365183",
                "lat": "29.922192",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365246",
                "lat": "29.922552",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365267",
                "lat": "29.922855",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.365184",
                    "lat": "29.922196",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365237",
                    "lat": "29.9225",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365237",
                    "lat": "29.9225",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365246",
                    "lat": "29.922552",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36526",
                    "lat": "29.922747",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365159",
                    "lat": "29.922095",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365183",
                    "lat": "29.922192",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365183",
                    "lat": "29.922192",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365237",
                    "lat": "29.9225",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365237",
                    "lat": "29.9225",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365245",
                    "lat": "29.922546",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.3651",
                    "lat": "29.921859",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365129",
                    "lat": "29.921973",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365129",
                    "lat": "29.921973",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365183",
                    "lat": "29.922192",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365183",
                    "lat": "29.922192",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365201",
                    "lat": "29.922296",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365029",
                    "lat": "29.921608",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36509",
                    "lat": "29.921818",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36509",
                    "lat": "29.921818",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365129",
                    "lat": "29.921973",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365129",
                    "lat": "29.921973",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365176",
                    "lat": "29.922165",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364969",
                    "lat": "29.921402",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364987",
                    "lat": "29.92146",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364987",
                    "lat": "29.92146",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36509",
                    "lat": "29.921818",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36509",
                    "lat": "29.921818",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365097",
                    "lat": "29.921847",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364925",
                    "lat": "29.921263",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364929",
                    "lat": "29.921274",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364929",
                    "lat": "29.921274",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364987",
                    "lat": "29.92146",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364987",
                    "lat": "29.92146",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365055",
                    "lat": "29.921696",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36488",
                    "lat": "29.921138",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364903",
                    "lat": "29.921192",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364903",
                    "lat": "29.921192",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364987",
                    "lat": "29.92146",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364987",
                    "lat": "29.92146",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365021",
                    "lat": "29.921577",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364794",
                    "lat": "29.920937",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364903",
                    "lat": "29.921192",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364903",
                    "lat": "29.921192",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364929",
                    "lat": "29.921274",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364929",
                    "lat": "29.921274",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364962",
                    "lat": "29.921382",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364738",
                    "lat": "29.920806",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364772",
                    "lat": "29.920886",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364772",
                    "lat": "29.920886",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364903",
                    "lat": "29.921192",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364903",
                    "lat": "29.921192",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364923",
                    "lat": "29.921257",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364685",
                    "lat": "29.920683",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364748",
                    "lat": "29.92083",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364748",
                    "lat": "29.92083",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364772",
                    "lat": "29.920886",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364772",
                    "lat": "29.920886",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364874",
                    "lat": "29.921123",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36456",
                    "lat": "29.920391",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364748",
                    "lat": "29.92083",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364748",
                    "lat": "29.92083",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364755",
                    "lat": "29.920846",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364463",
                    "lat": "29.920191",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364539",
                    "lat": "29.920341",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364539",
                    "lat": "29.920341",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364702",
                    "lat": "29.920722",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364368",
                    "lat": "29.920003",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364539",
                    "lat": "29.920341",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364539",
                    "lat": "29.920341",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364594",
                    "lat": "29.920469",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36427",
                    "lat": "29.919812",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364275",
                    "lat": "29.919819",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364275",
                    "lat": "29.919819",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364479",
                    "lat": "29.920222",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364191",
                    "lat": "29.919695",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364275",
                    "lat": "29.919819",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364275",
                    "lat": "29.919819",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364412",
                    "lat": "29.920089",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364016",
                    "lat": "29.919442",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364074",
                    "lat": "29.919525",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364074",
                    "lat": "29.919525",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364125",
                    "lat": "29.919598",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364125",
                    "lat": "29.919598",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364275",
                    "lat": "29.919819",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364275",
                    "lat": "29.919819",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364281",
                    "lat": "29.919831",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363901",
                    "lat": "29.919278",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364125",
                    "lat": "29.919598",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364125",
                    "lat": "29.919598",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364164",
                    "lat": "29.919655",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363776",
                    "lat": "29.919124",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363873",
                    "lat": "29.919238",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363873",
                    "lat": "29.919238",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364074",
                    "lat": "29.919525",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364074",
                    "lat": "29.919525",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364088",
                    "lat": "29.919545",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363661",
                    "lat": "29.918988",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363756",
                    "lat": "29.919101",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363756",
                    "lat": "29.919101",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363873",
                    "lat": "29.919238",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363873",
                    "lat": "29.919238",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363949",
                    "lat": "29.919347",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36351",
                    "lat": "29.918808",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363512",
                    "lat": "29.918811",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363512",
                    "lat": "29.918811",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363756",
                    "lat": "29.919101",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363873",
                    "lat": "29.919238",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363877",
                    "lat": "29.919244",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363333",
                    "lat": "29.91862",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363424",
                    "lat": "29.918706",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363424",
                    "lat": "29.918706",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363648",
                    "lat": "29.918973",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363156",
                    "lat": "29.918454",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363208",
                    "lat": "29.918502",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363208",
                    "lat": "29.918502",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363424",
                    "lat": "29.918706",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363424",
                    "lat": "29.918706",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363512",
                    "lat": "29.918811",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363512",
                    "lat": "29.918811",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363612",
                    "lat": "29.918929",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36306",
                    "lat": "29.918366",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363122",
                    "lat": "29.918423",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363122",
                    "lat": "29.918423",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363208",
                    "lat": "29.918502",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363208",
                    "lat": "29.918502",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363416",
                    "lat": "29.918698",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362834",
                    "lat": "29.918157",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363122",
                    "lat": "29.918423",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363122",
                    "lat": "29.918423",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363187",
                    "lat": "29.918483",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362647",
                    "lat": "29.917984",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362665",
                    "lat": "29.918001",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362665",
                    "lat": "29.918001",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362997",
                    "lat": "29.918307",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362665",
                    "lat": "29.918001",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362813",
                    "lat": "29.918138",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362665",
                    "lat": "29.918001",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362715",
                    "lat": "29.918047",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 260,
        "position": [
            {
                "lng": "103.36527",
                "lat": "29.922878",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365319",
                "lat": "29.923238",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365312",
                "lat": "29.923653",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365283",
                "lat": "29.924311",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365185",
                "lat": "29.925019",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365021",
                "lat": "29.925943",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 261,
        "position": [
            {
                "lng": "103.362425",
                "lat": "29.917827",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361755",
                "lat": "29.917331",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.360546",
                "lat": "29.916468",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357461",
                "lat": "29.91425",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.362425",
                    "lat": "29.917827",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36223",
                    "lat": "29.917683",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36223",
                    "lat": "29.917683",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362019",
                    "lat": "29.917526",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362425",
                    "lat": "29.917827",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362205",
                    "lat": "29.917664",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362205",
                    "lat": "29.917664",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362201",
                    "lat": "29.917661",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362201",
                    "lat": "29.917661",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362035",
                    "lat": "29.917538",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362365",
                    "lat": "29.917783",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362332",
                    "lat": "29.917758",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362332",
                    "lat": "29.917758",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362224",
                    "lat": "29.917678",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362224",
                    "lat": "29.917678",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362205",
                    "lat": "29.917664",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362205",
                    "lat": "29.917664",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362203",
                    "lat": "29.917663",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362203",
                    "lat": "29.917663",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362201",
                    "lat": "29.917661",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362425",
                    "lat": "29.917827",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362332",
                    "lat": "29.917758",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362332",
                    "lat": "29.917758",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362231",
                    "lat": "29.917684",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362425",
                    "lat": "29.917827",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362224",
                    "lat": "29.917678",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362224",
                    "lat": "29.917678",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362171",
                    "lat": "29.917639",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362171",
                    "lat": "29.917639",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362128",
                    "lat": "29.917607",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.3624",
                    "lat": "29.917808",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36223",
                    "lat": "29.917683",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36223",
                    "lat": "29.917683",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362203",
                    "lat": "29.917663",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362203",
                    "lat": "29.917663",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362201",
                    "lat": "29.917661",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362201",
                    "lat": "29.917661",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362171",
                    "lat": "29.917639",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362171",
                    "lat": "29.917639",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362048",
                    "lat": "29.917548",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362235",
                    "lat": "29.917687",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361829",
                    "lat": "29.917386",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362008",
                    "lat": "29.917518",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361755",
                    "lat": "29.917331",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361755",
                    "lat": "29.917331",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361655",
                    "lat": "29.917259",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361829",
                    "lat": "29.917386",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361755",
                    "lat": "29.917331",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361755",
                    "lat": "29.917331",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361424",
                    "lat": "29.917094",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361619",
                    "lat": "29.917234",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361263",
                    "lat": "29.91698",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361503",
                    "lat": "29.917151",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361146",
                    "lat": "29.916896",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361279",
                    "lat": "29.916992",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360905",
                    "lat": "29.916724",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361086",
                    "lat": "29.916854",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36084",
                    "lat": "29.916678",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36084",
                    "lat": "29.916678",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360717",
                    "lat": "29.91659",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36098",
                    "lat": "29.916778",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36084",
                    "lat": "29.916678",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36084",
                    "lat": "29.916678",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360546",
                    "lat": "29.916468",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360546",
                    "lat": "29.916468",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360488",
                    "lat": "29.916426",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360678",
                    "lat": "29.916562",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360546",
                    "lat": "29.916468",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360546",
                    "lat": "29.916468",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360296",
                    "lat": "29.916288",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360541",
                    "lat": "29.916465",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36015",
                    "lat": "29.916184",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360432",
                    "lat": "29.916386",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360052",
                    "lat": "29.916113",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360102",
                    "lat": "29.916149",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359717",
                    "lat": "29.915872",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359983",
                    "lat": "29.916063",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359588",
                    "lat": "29.915779",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359693",
                    "lat": "29.915855",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359305",
                    "lat": "29.915576",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359502",
                    "lat": "29.915717",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359192",
                    "lat": "29.915494",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359192",
                    "lat": "29.915494",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359129",
                    "lat": "29.915449",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359331",
                    "lat": "29.915594",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359192",
                    "lat": "29.915494",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359192",
                    "lat": "29.915494",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358977",
                    "lat": "29.91534",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359157",
                    "lat": "29.915469",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358899",
                    "lat": "29.915284",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358899",
                    "lat": "29.915284",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358804",
                    "lat": "29.915216",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358928",
                    "lat": "29.915305",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358899",
                    "lat": "29.915284",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358899",
                    "lat": "29.915284",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358723",
                    "lat": "29.915157",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358723",
                    "lat": "29.915157",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358591",
                    "lat": "29.915062",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358773",
                    "lat": "29.915193",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358723",
                    "lat": "29.915157",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358723",
                    "lat": "29.915157",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358438",
                    "lat": "29.914953",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358491",
                    "lat": "29.91499",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35838",
                    "lat": "29.91491",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.35838",
                    "lat": "29.91491",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358178",
                    "lat": "29.914766",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358382",
                    "lat": "29.914912",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35838",
                    "lat": "29.91491",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.35838",
                    "lat": "29.91491",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357963",
                    "lat": "29.914611",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358115",
                    "lat": "29.91472",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357795",
                    "lat": "29.91449",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358",
                    "lat": "29.914638",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357549",
                    "lat": "29.914313",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357657",
                    "lat": "29.914391",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357461",
                    "lat": "29.91425",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357554",
                    "lat": "29.914317",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357461",
                    "lat": "29.91425",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 262,
        "position": [
            {
                "lng": "103.372312",
                "lat": "29.923939",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.373315",
                "lat": "29.923215",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.377758",
                "lat": "29.919981",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.377703",
                    "lat": "29.920021",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377758",
                    "lat": "29.919981",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.377552",
                    "lat": "29.920131",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377758",
                    "lat": "29.919981",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.377255",
                    "lat": "29.920347",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377387",
                    "lat": "29.920251",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.377387",
                    "lat": "29.920251",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377664",
                    "lat": "29.920049",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.377221",
                    "lat": "29.920372",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377589",
                    "lat": "29.920104",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.37702",
                    "lat": "29.920518",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377387",
                    "lat": "29.920251",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.377387",
                    "lat": "29.920251",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377395",
                    "lat": "29.920245",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.376892",
                    "lat": "29.920612",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.37725",
                    "lat": "29.920351",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.376628",
                    "lat": "29.920803",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.376996",
                    "lat": "29.920536",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.376431",
                    "lat": "29.920947",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.37681",
                    "lat": "29.920671",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.376278",
                    "lat": "29.921058",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.376653",
                    "lat": "29.920785",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.376142",
                    "lat": "29.921157",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.376523",
                    "lat": "29.92088",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.375692",
                    "lat": "29.921485",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.376061",
                    "lat": "29.921216",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.375221",
                    "lat": "29.921828",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.375599",
                    "lat": "29.921553",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.375049",
                    "lat": "29.921953",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.375248",
                    "lat": "29.921807",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.375248",
                    "lat": "29.921807",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.375423",
                    "lat": "29.92168",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.374816",
                    "lat": "29.922122",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.375248",
                    "lat": "29.921807",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.375248",
                    "lat": "29.921807",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.375315",
                    "lat": "29.921759",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.374348",
                    "lat": "29.922463",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.374629",
                    "lat": "29.922258",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.374285",
                    "lat": "29.922509",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.374575",
                    "lat": "29.922298",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.374101",
                    "lat": "29.922643",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.37438",
                    "lat": "29.92244",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373895",
                    "lat": "29.922793",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.374262",
                    "lat": "29.922525",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.37369",
                    "lat": "29.922942",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.374018",
                    "lat": "29.922703",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373467",
                    "lat": "29.923104",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373509",
                    "lat": "29.923074",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373509",
                    "lat": "29.923074",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373578",
                    "lat": "29.923024",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373578",
                    "lat": "29.923024",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.37367",
                    "lat": "29.922957",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373398",
                    "lat": "29.923155",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373578",
                    "lat": "29.923024",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373578",
                    "lat": "29.923024",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373746",
                    "lat": "29.922901",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373243",
                    "lat": "29.923267",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373315",
                    "lat": "29.923215",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373315",
                    "lat": "29.923215",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373509",
                    "lat": "29.923074",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373509",
                    "lat": "29.923074",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373588",
                    "lat": "29.923016",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373061",
                    "lat": "29.923399",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373315",
                    "lat": "29.923215",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.373315",
                    "lat": "29.923215",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373392",
                    "lat": "29.923159",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.372982",
                    "lat": "29.923455",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.373201",
                    "lat": "29.923297",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.372759",
                    "lat": "29.923616",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.372976",
                    "lat": "29.923459",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.372592",
                    "lat": "29.923737",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.372855",
                    "lat": "29.923547",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 263,
        "position": [
            {
                "lng": "103.401427",
                "lat": "29.911818",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.401481",
                "lat": "29.911662",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.40138",
                "lat": "29.911632",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.401427",
                    "lat": "29.911818",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.40144",
                    "lat": "29.91178",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401427",
                    "lat": "29.911818",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401461",
                    "lat": "29.911719",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401427",
                    "lat": "29.911818",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401481",
                    "lat": "29.911662",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.40138",
                    "lat": "29.911632",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.40142",
                    "lat": "29.911644",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.40138",
                    "lat": "29.911632",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 264,
        "position": [
            {
                "lng": "103.401354",
                "lat": "29.911625",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.399342",
                "lat": "29.911028",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.396715",
                "lat": "29.910252",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.395115",
                "lat": "29.909765",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.395015",
                "lat": "29.909687",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394918",
                "lat": "29.909591",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394892",
                "lat": "29.909488",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394866",
                "lat": "29.909313",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394858",
                "lat": "29.909108",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394924",
                "lat": "29.908663",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394747",
                "lat": "29.908637",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394746",
                "lat": "29.908397",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394711",
                "lat": "29.908239",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394619",
                "lat": "29.908104",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394457",
                "lat": "29.907963",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394155",
                "lat": "29.907776",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.393568",
                "lat": "29.907434",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.39293",
                "lat": "29.907058",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.39291",
                "lat": "29.907081",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.392845",
                "lat": "29.907044",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.392865",
                "lat": "29.907019",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.392381",
                "lat": "29.906751",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.3922",
                "lat": "29.906651",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.392002",
                "lat": "29.906581",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.391812",
                "lat": "29.906505",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.391582",
                "lat": "29.906411",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.391226",
                "lat": "29.906281",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.390943",
                "lat": "29.906173",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.390208",
                "lat": "29.905962",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.389823",
                "lat": "29.905918",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.389624",
                "lat": "29.905895",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.389159",
                "lat": "29.905864",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.388972",
                "lat": "29.905857",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.388513",
                "lat": "29.905901",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.38791",
                "lat": "29.906064",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.386407",
                "lat": "29.906536",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.385682",
                "lat": "29.906777",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.384888",
                "lat": "29.907035",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.384835",
                "lat": "29.90692",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383553",
                "lat": "29.907347",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383321",
                "lat": "29.907417",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383196",
                "lat": "29.907429",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383071",
                "lat": "29.907405",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383026",
                "lat": "29.907383",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382915",
                "lat": "29.907293",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382806",
                "lat": "29.90719",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382468",
                "lat": "29.906726",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382133",
                "lat": "29.906291",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.38209",
                "lat": "29.906228",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382072",
                "lat": "29.906138",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382078",
                "lat": "29.906031",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382108",
                "lat": "29.905938",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382217",
                "lat": "29.905735",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.401354",
                    "lat": "29.911625",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.40119",
                    "lat": "29.911576",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401354",
                    "lat": "29.911625",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400904",
                    "lat": "29.911491",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401239",
                    "lat": "29.911591",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400956",
                    "lat": "29.911507",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400956",
                    "lat": "29.911507",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400646",
                    "lat": "29.911415",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400993",
                    "lat": "29.911518",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400956",
                    "lat": "29.911507",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400956",
                    "lat": "29.911507",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400404",
                    "lat": "29.911343",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400787",
                    "lat": "29.911457",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400177",
                    "lat": "29.911276",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400511",
                    "lat": "29.911375",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400284",
                    "lat": "29.911307",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400284",
                    "lat": "29.911307",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400092",
                    "lat": "29.91125",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400092",
                    "lat": "29.91125",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400048",
                    "lat": "29.911237",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.40033",
                    "lat": "29.911321",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400284",
                    "lat": "29.911307",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400284",
                    "lat": "29.911307",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399946",
                    "lat": "29.911207",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399946",
                    "lat": "29.911207",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399808",
                    "lat": "29.911166",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400183",
                    "lat": "29.911277",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400092",
                    "lat": "29.91125",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400092",
                    "lat": "29.91125",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399946",
                    "lat": "29.911207",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399946",
                    "lat": "29.911207",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39965",
                    "lat": "29.911119",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39965",
                    "lat": "29.911119",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399523",
                    "lat": "29.911082",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399904",
                    "lat": "29.911195",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39965",
                    "lat": "29.911119",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39965",
                    "lat": "29.911119",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399342",
                    "lat": "29.911028",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399342",
                    "lat": "29.911028",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399254",
                    "lat": "29.911002",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399412",
                    "lat": "29.911049",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399342",
                    "lat": "29.911028",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399342",
                    "lat": "29.911028",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398995",
                    "lat": "29.910926",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398995",
                    "lat": "29.910926",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398918",
                    "lat": "29.910903",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399294",
                    "lat": "29.911014",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398995",
                    "lat": "29.910926",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398995",
                    "lat": "29.910926",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398803",
                    "lat": "29.910869",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399037",
                    "lat": "29.910938",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398783",
                    "lat": "29.910863",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398783",
                    "lat": "29.910863",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398575",
                    "lat": "29.910801",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398974",
                    "lat": "29.910919",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398783",
                    "lat": "29.910863",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398783",
                    "lat": "29.910863",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39835",
                    "lat": "29.910735",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39873",
                    "lat": "29.910847",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398175",
                    "lat": "29.910683",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39851",
                    "lat": "29.910782",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39792",
                    "lat": "29.910608",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39834",
                    "lat": "29.910732",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397679",
                    "lat": "29.910537",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397905",
                    "lat": "29.910603",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397416",
                    "lat": "29.910459",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397791",
                    "lat": "29.91057",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397182",
                    "lat": "29.91039",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39756",
                    "lat": "29.910502",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39708",
                    "lat": "29.91036",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39708",
                    "lat": "29.91036",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396898",
                    "lat": "29.910306",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39728",
                    "lat": "29.910419",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39708",
                    "lat": "29.91036",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39708",
                    "lat": "29.91036",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396715",
                    "lat": "29.910252",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396715",
                    "lat": "29.910252",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396628",
                    "lat": "29.910225",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397085",
                    "lat": "29.910361",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396715",
                    "lat": "29.910252",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396715",
                    "lat": "29.910252",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396414",
                    "lat": "29.91016",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396833",
                    "lat": "29.910287",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396715",
                    "lat": "29.910252",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396715",
                    "lat": "29.910252",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396286",
                    "lat": "29.910121",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396286",
                    "lat": "29.910121",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396186",
                    "lat": "29.910091",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396583",
                    "lat": "29.910212",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396286",
                    "lat": "29.910121",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396286",
                    "lat": "29.910121",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395931",
                    "lat": "29.910013",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395931",
                    "lat": "29.910013",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395914",
                    "lat": "29.910008",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396222",
                    "lat": "29.910102",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395732",
                    "lat": "29.909953",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396062",
                    "lat": "29.910053",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395931",
                    "lat": "29.910013",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395931",
                    "lat": "29.910013",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395529",
                    "lat": "29.909891",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395873",
                    "lat": "29.909996",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395292",
                    "lat": "29.909819",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39572",
                    "lat": "29.909949",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395115",
                    "lat": "29.909765",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395115",
                    "lat": "29.909765",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395041",
                    "lat": "29.909707",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39532",
                    "lat": "29.909827",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395115",
                    "lat": "29.909765",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395115",
                    "lat": "29.909765",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395015",
                    "lat": "29.909687",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395015",
                    "lat": "29.909687",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394918",
                    "lat": "29.909591",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394918",
                    "lat": "29.909591",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394905",
                    "lat": "29.909539",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395227",
                    "lat": "29.909799",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395115",
                    "lat": "29.909765",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394918",
                    "lat": "29.909591",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394907",
                    "lat": "29.909547",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 265,
        "position": [
            {
                "lng": "103.401458",
                "lat": "29.911826",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.401427",
                "lat": "29.911818",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.401458",
                    "lat": "29.911826",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401427",
                    "lat": "29.911818",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 266,
        "position": [
            {
                "lng": "103.382262",
                "lat": "29.916926",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.379325",
                "lat": "29.91895",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.382262",
                    "lat": "29.916926",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382144",
                    "lat": "29.917007",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382262",
                    "lat": "29.916926",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382064",
                    "lat": "29.917063",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382212",
                    "lat": "29.91696",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381826",
                    "lat": "29.917226",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381826",
                    "lat": "29.917226",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381777",
                    "lat": "29.91726",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382113",
                    "lat": "29.917029",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381691",
                    "lat": "29.917319",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381691",
                    "lat": "29.917319",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381575",
                    "lat": "29.917399",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38188",
                    "lat": "29.917189",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381826",
                    "lat": "29.917226",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381826",
                    "lat": "29.917226",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381691",
                    "lat": "29.917319",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381691",
                    "lat": "29.917319",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381343",
                    "lat": "29.917559",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381577",
                    "lat": "29.917398",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381175",
                    "lat": "29.917675",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381453",
                    "lat": "29.917483",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.380966",
                    "lat": "29.917819",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381154",
                    "lat": "29.917689",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.380777",
                    "lat": "29.917949",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38103",
                    "lat": "29.917775",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.380596",
                    "lat": "29.918074",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.380768",
                    "lat": "29.917956",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38048",
                    "lat": "29.918154",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.380335",
                    "lat": "29.918254",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.379969",
                    "lat": "29.918506",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.380071",
                    "lat": "29.918436",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.379694",
                    "lat": "29.918695",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.379879",
                    "lat": "29.918568",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.37955",
                    "lat": "29.918795",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.37955",
                    "lat": "29.918795",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.379465",
                    "lat": "29.918854",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.379754",
                    "lat": "29.918655",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.37955",
                    "lat": "29.918795",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.37955",
                    "lat": "29.918795",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.379325",
                    "lat": "29.91895",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.379411",
                    "lat": "29.918891",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.379325",
                    "lat": "29.91895",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 267,
        "position": [
            {
                "lng": "103.379303",
                "lat": "29.918964",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.377758",
                "lat": "29.919981",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.379303",
                    "lat": "29.918964",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.379268",
                    "lat": "29.918987",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.379303",
                    "lat": "29.918964",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.379036",
                    "lat": "29.91914",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.379141",
                    "lat": "29.91907",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378779",
                    "lat": "29.919309",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378974",
                    "lat": "29.919181",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378612",
                    "lat": "29.919419",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378612",
                    "lat": "29.919419",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378589",
                    "lat": "29.919434",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378871",
                    "lat": "29.919248",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378622",
                    "lat": "29.919413",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378622",
                    "lat": "29.919413",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378612",
                    "lat": "29.919419",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378612",
                    "lat": "29.919419",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378483",
                    "lat": "29.919504",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378627",
                    "lat": "29.919409",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378622",
                    "lat": "29.919413",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378622",
                    "lat": "29.919413",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378209",
                    "lat": "29.919684",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378478",
                    "lat": "29.919507",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378162",
                    "lat": "29.919715",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378162",
                    "lat": "29.919715",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378057",
                    "lat": "29.919784",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378362",
                    "lat": "29.919583",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.378162",
                    "lat": "29.919715",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378162",
                    "lat": "29.919715",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377901",
                    "lat": "29.919887",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.377901",
                    "lat": "29.919887",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377892",
                    "lat": "29.919893",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.378099",
                    "lat": "29.919757",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377901",
                    "lat": "29.919887",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.377901",
                    "lat": "29.919887",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377758",
                    "lat": "29.919981",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.37796",
                    "lat": "29.919848",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.377758",
                    "lat": "29.919981",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 268,
        "position": [
            {
                "lng": "103.378725",
                "lat": "29.905419",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.378725",
                "lat": "29.905406",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.380077",
                "lat": "29.905516",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.38095",
                "lat": "29.90558",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.38162",
                "lat": "29.90563",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.381897",
                "lat": "29.905653",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.381983",
                "lat": "29.90569",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 269,
        "position": [
            {
                "lng": "103.369859",
                "lat": "29.905575",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370165",
                "lat": "29.905471",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.37061",
                "lat": "29.905417",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371715",
                "lat": "29.905312",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372923",
                "lat": "29.905232",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.373022",
                "lat": "29.905226",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.374536",
                "lat": "29.905132",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.375528",
                "lat": "29.905133",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.376734",
                "lat": "29.905206",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.378725",
                "lat": "29.905406",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 270,
        "position": [
            {
                "lng": "103.35865",
                "lat": "29.91363",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.358129",
                "lat": "29.913984",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.358115",
                "lat": "29.914054",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.35811",
                "lat": "29.914134",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.35814",
                "lat": "29.914184",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.359081",
                "lat": "29.914877",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.359087",
                "lat": "29.914871",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.358993",
                    "lat": "29.914812",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359047",
                    "lat": "29.914852",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358843",
                    "lat": "29.914702",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358886",
                    "lat": "29.914733",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358528",
                    "lat": "29.91447",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358664",
                    "lat": "29.91457",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358343",
                    "lat": "29.914333",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35855",
                    "lat": "29.914486",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358188",
                    "lat": "29.91422",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358254",
                    "lat": "29.914268",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 136,
        "position": [
            {
                "lng": "103.363136",
                "lat": "29.915129",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363305",
                "lat": "29.915355",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363023",
                "lat": "29.915522",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362895",
                "lat": "29.915533",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361928",
                "lat": "29.916095",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361945",
                "lat": "29.916118",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361679",
                "lat": "29.916325",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361673",
                "lat": "29.91632",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 137,
        "position": [
            {
                "lng": "103.362336",
                "lat": "29.916304",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362346",
                "lat": "29.916318",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 138,
        "position": [
            {
                "lng": "103.362297",
                "lat": "29.916345",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362288",
                "lat": "29.916331",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 139,
        "position": [
            {
                "lng": "103.362623",
                "lat": "29.916086",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362607",
                "lat": "29.916074",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 140,
        "position": [
            {
                "lng": "103.362828",
                "lat": "29.915874",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362839",
                "lat": "29.915882",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362879",
                "lat": "29.915847",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362867",
                "lat": "29.915837",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 141,
        "position": [
            {
                "lng": "103.362584",
                "lat": "29.916123",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362571",
                "lat": "29.916111",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 142,
        "position": [
            {
                "lng": "103.361603",
                "lat": "29.916253",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361671",
                "lat": "29.9162",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361664",
                "lat": "29.916194",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361698",
                "lat": "29.916168",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36169",
                "lat": "29.916161",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.3617",
                "lat": "29.916152",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 143,
        "position": [
            {
                "lng": "103.361845",
                "lat": "29.91609",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.3619",
                "lat": "29.916046",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361939",
                "lat": "29.916087",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36194",
                "lat": "29.916088",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 144,
        "position": [
            {
                "lng": "103.362213",
                "lat": "29.915868",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36222",
                "lat": "29.915864",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362251",
                "lat": "29.915907",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 145,
        "position": [
            {
                "lng": "103.362122",
                "lat": "29.915763",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362163",
                "lat": "29.915734",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362241",
                "lat": "29.91569",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362319",
                "lat": "29.915788",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36232",
                "lat": "29.915848",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36233",
                "lat": "29.915861",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 146,
        "position": [
            {
                "lng": "103.36204",
                "lat": "29.915811",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362006",
                "lat": "29.915828",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361982",
                "lat": "29.915839",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361917",
                "lat": "29.915757",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361922",
                "lat": "29.915741",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362101",
                "lat": "29.915638",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362123",
                "lat": "29.915637",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362186",
                "lat": "29.91572",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 147,
        "position": [
            {
                "lng": "103.362661",
                "lat": "29.915543",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362728",
                "lat": "29.91563",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 148,
        "position": [
            {
                "lng": "103.362598",
                "lat": "29.915486",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362641",
                "lat": "29.915456",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362718",
                "lat": "29.915413",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362795",
                "lat": "29.91551",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362837",
                "lat": "29.915565",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 149,
        "position": [
            {
                "lng": "103.362516",
                "lat": "29.915533",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362482",
                "lat": "29.915547",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362457",
                "lat": "29.915563",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36239",
                "lat": "29.915477",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362402",
                "lat": "29.915461",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362576",
                "lat": "29.915361",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362603",
                "lat": "29.915365",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362664",
                "lat": "29.915443",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 150,
        "position": [
            {
                "lng": "103.36302",
                "lat": "29.915366",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363008",
                "lat": "29.915373",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363014",
                "lat": "29.915382",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362977",
                "lat": "29.915402",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362983",
                "lat": "29.915411",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362911",
                "lat": "29.915454",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 151,
        "position": [
            {
                "lng": "103.362966",
                "lat": "29.915527",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362964",
                "lat": "29.915518",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362911",
                "lat": "29.915454",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362846",
                "lat": "29.91537",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362924",
                "lat": "29.915325",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362959",
                "lat": "29.915311",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362977",
                "lat": "29.915304",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 152,
        "position": [
            {
                "lng": "103.363102",
                "lat": "29.915317",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36311",
                "lat": "29.915317",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363121",
                "lat": "29.915316",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363156",
                "lat": "29.915299",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363162",
                "lat": "29.915307",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363236",
                "lat": "29.915265",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 153,
        "position": [
            {
                "lng": "103.363053",
                "lat": "29.915264",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363058",
                "lat": "29.915258",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363053",
                "lat": "29.91525",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 154,
        "position": [
            {
                "lng": "103.363048",
                "lat": "29.915255",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363067",
                "lat": "29.915241",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363173",
                "lat": "29.915179",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 155,
        "position": [
            {
                "lng": "103.36319",
                "lat": "29.915202",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363308",
                "lat": "29.915133",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363437",
                "lat": "29.915155",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363477",
                "lat": "29.91521",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363366",
                "lat": "29.91532",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363311",
                "lat": "29.915373",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.3633",
                "lat": "29.915358",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 156,
        "position": [
            {
                "lng": "103.362288",
                "lat": "29.916331",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362269",
                "lat": "29.916302",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 157,
        "position": [
            {
                "lng": "103.362607",
                "lat": "29.916074",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362585",
                "lat": "29.916057",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 158,
        "position": [
            {
                "lng": "103.362801",
                "lat": "29.915852",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362828",
                "lat": "29.915874",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 159,
        "position": [
            {
                "lng": "103.36249",
                "lat": "29.915768",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362626",
                "lat": "29.915931",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362635",
                "lat": "29.915937",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362546",
                "lat": "29.916021",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362591",
                "lat": "29.916051",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 160,
        "position": [
            {
                "lng": "103.361707",
                "lat": "29.916304",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361768",
                "lat": "29.916363",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36191",
                "lat": "29.916258",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361915",
                "lat": "29.916254",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361936",
                "lat": "29.916274",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362072",
                "lat": "29.91637",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362092",
                "lat": "29.916376",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362114",
                "lat": "29.916376",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362141",
                "lat": "29.916371",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362317",
                "lat": "29.916277",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362336",
                "lat": "29.916304",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 161,
        "position": [
            {
                "lng": "103.361943",
                "lat": "29.91628",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361931",
                "lat": "29.916293",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 162,
        "position": [
            {
                "lng": "103.361525",
                "lat": "29.916182",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361627",
                "lat": "29.916101",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361642",
                "lat": "29.916089",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 163,
        "position": [
            {
                "lng": "103.361647",
                "lat": "29.916107",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361635",
                "lat": "29.916095",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 164,
        "position": [
            {
                "lng": "103.361716",
                "lat": "29.916048",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361718",
                "lat": "29.916042",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361713",
                "lat": "29.916034",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 165,
        "position": [
            {
                "lng": "103.361673",
                "lat": "29.91632",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361525",
                "lat": "29.916181",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36151",
                "lat": "29.916158",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.3615",
                "lat": "29.916134",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361494",
                "lat": "29.916109",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361495",
                "lat": "29.916094",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.3615",
                "lat": "29.916076",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361676",
                "lat": "29.915938",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361694",
                "lat": "29.915937",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361756",
                "lat": "29.916",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361721",
                "lat": "29.916028",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361709",
                "lat": "29.916038",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 166,
        "position": [
            {
                "lng": "103.362974",
                "lat": "29.915315",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36297",
                "lat": "29.915307",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 167,
        "position": [
            {
                "lng": "103.362571",
                "lat": "29.916111",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362546",
                "lat": "29.916092",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362585",
                "lat": "29.916057",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362801",
                "lat": "29.915852",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36284",
                "lat": "29.915815",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362867",
                "lat": "29.915837",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 168,
        "position": [
            {
                "lng": "103.372368",
                "lat": "29.922031",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372209",
                "lat": "29.92206",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 169,
        "position": [
            {
                "lng": "103.372183",
                "lat": "29.922064",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36713",
                "lat": "29.922908",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 170,
        "position": [
            {
                "lng": "103.37018",
                "lat": "29.90905",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370117",
                "lat": "29.909064",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 171,
        "position": [
            {
                "lng": "103.37009",
                "lat": "29.909069",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369948",
                "lat": "29.909099",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369775",
                "lat": "29.909139",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369371",
                "lat": "29.909233",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368967",
                "lat": "29.909326",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368563",
                "lat": "29.909419",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368159",
                "lat": "29.909513",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367501",
                "lat": "29.909672",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 172,
        "position": [
            {
                "lng": "103.371845",
                "lat": "29.91745",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371954",
                "lat": "29.917421",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372044",
                "lat": "29.917394",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 173,
        "position": [
            {
                "lng": "103.369832",
                "lat": "29.905583",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369807",
                "lat": "29.905592",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368955",
                "lat": "29.906482",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368618",
                "lat": "29.906674",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368709",
                "lat": "29.906807",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367602",
                "lat": "29.907534",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.366349",
                "lat": "29.908357",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.366278",
                "lat": "29.908404",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365128",
                "lat": "29.909213",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364865",
                "lat": "29.909399",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363895",
                "lat": "29.91006",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362657",
                "lat": "29.910902",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362114",
                "lat": "29.911271",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 174,
        "position": [
            {
                "lng": "103.362092",
                "lat": "29.911286",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36142",
                "lat": "29.911744",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.360595",
                "lat": "29.912305",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.360182",
                "lat": "29.912586",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.358945",
                "lat": "29.913429",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.35865",
                "lat": "29.91363",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.358542",
                "lat": "29.913516",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357735",
                "lat": "29.914063",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357435",
                "lat": "29.914268",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357336",
                "lat": "29.914355",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.357749",
                    "lat": "29.914054",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357735",
                    "lat": "29.914063",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357735",
                    "lat": "29.914063",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357603",
                    "lat": "29.914154",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357788",
                    "lat": "29.914027",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357735",
                    "lat": "29.914063",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357735",
                    "lat": "29.914063",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357435",
                    "lat": "29.914268",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357435",
                    "lat": "29.914268",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357357",
                    "lat": "29.914336",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357703",
                    "lat": "29.914085",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357435",
                    "lat": "29.914268",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357435",
                    "lat": "29.914268",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357359",
                    "lat": "29.914335",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 175,
        "position": [
            {
                "lng": "103.366604",
                "lat": "29.9088",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36662",
                "lat": "29.908816",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 176,
        "position": [
            {
                "lng": "103.366636",
                "lat": "29.908835",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.366878",
                "lat": "29.909097",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367122",
                "lat": "29.909361",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367401",
                "lat": "29.909676",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 177,
        "position": [
            {
                "lng": "103.367466",
                "lat": "29.90983",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367491",
                "lat": "29.90989",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36756",
                "lat": "29.910116",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367722",
                "lat": "29.911243",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 178,
        "position": [
            {
                "lng": "103.367401",
                "lat": "29.909676",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367457",
                "lat": "29.909808",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 179,
        "position": [
            {
                "lng": "103.367727",
                "lat": "29.911267",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367747",
                "lat": "29.911445",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 180,
        "position": [
            {
                "lng": "103.367391",
                "lat": "29.914469",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367325",
                "lat": "29.915147",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367373",
                "lat": "29.915303",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367571",
                "lat": "29.915383",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367974",
                "lat": "29.915233",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 181,
        "position": [
            {
                "lng": "103.367717",
                "lat": "29.912176",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367632",
                "lat": "29.912941",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367524",
                "lat": "29.913633",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367395",
                "lat": "29.914424",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367393",
                "lat": "29.914446",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 182,
        "position": [
            {
                "lng": "103.367751",
                "lat": "29.911807",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36772",
                "lat": "29.912144",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367719",
                "lat": "29.912153",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 183,
        "position": [
            {
                "lng": "103.36839",
                "lat": "29.922708",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368527",
                "lat": "29.922775",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368641",
                "lat": "29.922857",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368666",
                "lat": "29.922951",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 184,
        "position": [
            {
                "lng": "103.368672",
                "lat": "29.922974",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368702",
                "lat": "29.923091",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369181",
                "lat": "29.925207",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 185,
        "position": [
            {
                "lng": "103.367405",
                "lat": "29.912958",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367502",
                "lat": "29.911954",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 186,
        "position": [
            {
                "lng": "103.367397",
                "lat": "29.911948",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367347",
                "lat": "29.911945",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 187,
        "position": [
            {
                "lng": "103.367817",
                "lat": "29.911791",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367751",
                "lat": "29.911807",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367541",
                "lat": "29.911904",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367502",
                "lat": "29.911954",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367424",
                "lat": "29.911949",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 188,
        "position": [
            {
                "lng": "103.367347",
                "lat": "29.911945",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365916",
                "lat": "29.913076",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.366154",
                "lat": "29.913282",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365193",
                "lat": "29.914004",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 189,
        "position": [
            {
                "lng": "103.36498",
                "lat": "29.914336",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365193",
                "lat": "29.914004",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365238",
                "lat": "29.914037",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36518",
                "lat": "29.914113",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365158",
                "lat": "29.914172",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365161",
                "lat": "29.914217",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365307",
                "lat": "29.914386",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 190,
        "position": [
            {
                "lng": "103.370623",
                "lat": "29.914878",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370627",
                "lat": "29.914878",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370975",
                "lat": "29.914861",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 191,
        "position": [
            {
                "lng": "103.363099",
                "lat": "29.917447",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364015",
                "lat": "29.917013",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365453",
                "lat": "29.916471",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.366729",
                "lat": "29.916016",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368771",
                "lat": "29.915258",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369239",
                "lat": "29.915107",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369569",
                "lat": "29.915022",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369918",
                "lat": "29.914948",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370277",
                "lat": "29.914902",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370596",
                "lat": "29.91488",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.363099",
                    "lat": "29.917447",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363219",
                    "lat": "29.91739",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363316",
                    "lat": "29.917344",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363495",
                    "lat": "29.917259",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363521",
                    "lat": "29.917247",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363855",
                    "lat": "29.917089",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363658",
                    "lat": "29.917182",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364015",
                    "lat": "29.917013",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364032",
                    "lat": "29.917007",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364033",
                    "lat": "29.917006",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364429",
                    "lat": "29.916857",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364202",
                    "lat": "29.916943",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364672",
                    "lat": "29.916765",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364632",
                    "lat": "29.916781",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365028",
                    "lat": "29.916631",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364833",
                    "lat": "29.916705",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365062",
                    "lat": "29.916618",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365062",
                    "lat": "29.916618",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365245",
                    "lat": "29.916549",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365007",
                    "lat": "29.916639",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365062",
                    "lat": "29.916618",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365062",
                    "lat": "29.916618",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365416",
                    "lat": "29.916485",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36524",
                    "lat": "29.916551",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365453",
                    "lat": "29.916471",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365453",
                    "lat": "29.916471",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365658",
                    "lat": "29.916398",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365365",
                    "lat": "29.916504",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365453",
                    "lat": "29.916471",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365453",
                    "lat": "29.916471",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365951",
                    "lat": "29.916293",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365812",
                    "lat": "29.916343",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366241",
                    "lat": "29.91619",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365947",
                    "lat": "29.916295",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366362",
                    "lat": "29.916147",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366117",
                    "lat": "29.916234",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366525",
                    "lat": "29.916089",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366245",
                    "lat": "29.916189",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366719",
                    "lat": "29.91602",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366524",
                    "lat": "29.916089",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366729",
                    "lat": "29.916016",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366729",
                    "lat": "29.916016",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366947",
                    "lat": "29.915935",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366611",
                    "lat": "29.916058",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366729",
                    "lat": "29.916016",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366729",
                    "lat": "29.916016",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366882",
                    "lat": "29.915959",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366882",
                    "lat": "29.915959",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.367011",
                    "lat": "29.915911",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366839",
                    "lat": "29.915975",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366882",
                    "lat": "29.915959",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366882",
                    "lat": "29.915959",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36711",
                    "lat": "29.915874",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36711",
                    "lat": "29.915874",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.367251",
                    "lat": "29.915822",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366908",
                    "lat": "29.91595",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.367464",
                    "lat": "29.915743",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366998",
                    "lat": "29.915916",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36711",
                    "lat": "29.915874",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36711",
                    "lat": "29.915874",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.367501",
                    "lat": "29.915729",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.367107",
                    "lat": "29.915876",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.367346",
                    "lat": "29.915787",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 192,
        "position": [
            {
                "lng": "103.356742",
                "lat": "29.920569",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.35701",
                "lat": "29.920458",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357136",
                "lat": "29.920706",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357489",
                "lat": "29.920592",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357512",
                "lat": "29.920638",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.35726",
                    "lat": "29.920666",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357489",
                    "lat": "29.920592",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357512",
                    "lat": "29.920638",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357494",
                    "lat": "29.920603",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357512",
                    "lat": "29.920638",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 193,
        "position": [
            {
                "lng": "103.357522",
                "lat": "29.920659",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357613",
                "lat": "29.920845",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.357522",
                    "lat": "29.920659",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357605",
                    "lat": "29.920829",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357522",
                    "lat": "29.920659",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357613",
                    "lat": "29.920845",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357522",
                    "lat": "29.920659",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357598",
                    "lat": "29.920814",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 194,
        "position": [
            {
                "lng": "103.367134",
                "lat": "29.914495",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367129",
                "lat": "29.914561",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 195,
        "position": [
            {
                "lng": "103.367127",
                "lat": "29.914585",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367072",
                "lat": "29.915385",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367008",
                "lat": "29.915533",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.366802",
                "lat": "29.915675",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365351",
                "lat": "29.91622",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.365578",
                    "lat": "29.916135",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365351",
                    "lat": "29.91622",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.365851",
                    "lat": "29.916032",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365351",
                    "lat": "29.91622",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366145",
                    "lat": "29.915922",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365713",
                    "lat": "29.916084",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366278",
                    "lat": "29.915872",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366262",
                    "lat": "29.915878",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366262",
                    "lat": "29.915878",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366261",
                    "lat": "29.915878",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366261",
                    "lat": "29.915878",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.365837",
                    "lat": "29.916037",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366445",
                    "lat": "29.915809",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366297",
                    "lat": "29.915865",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366297",
                    "lat": "29.915865",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366262",
                    "lat": "29.915878",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366262",
                    "lat": "29.915878",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366002",
                    "lat": "29.915976",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366644",
                    "lat": "29.915734",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366455",
                    "lat": "29.915805",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366455",
                    "lat": "29.915805",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366297",
                    "lat": "29.915865",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366297",
                    "lat": "29.915865",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366261",
                    "lat": "29.915878",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366261",
                    "lat": "29.915878",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366124",
                    "lat": "29.91593",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366837",
                    "lat": "29.915651",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366802",
                    "lat": "29.915675",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366802",
                    "lat": "29.915675",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366455",
                    "lat": "29.915805",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366455",
                    "lat": "29.915805",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366421",
                    "lat": "29.915818",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366903",
                    "lat": "29.915606",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366802",
                    "lat": "29.915675",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366802",
                    "lat": "29.915675",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366489",
                    "lat": "29.915793",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.367047",
                    "lat": "29.915442",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.367008",
                    "lat": "29.915533",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.367008",
                    "lat": "29.915533",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366802",
                    "lat": "29.915675",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366802",
                    "lat": "29.915675",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366686",
                    "lat": "29.915719",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.367052",
                    "lat": "29.915432",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.367008",
                    "lat": "29.915533",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.366802",
                    "lat": "29.915675",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.366767",
                    "lat": "29.915688",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 196,
        "position": [
            {
                "lng": "103.367388",
                "lat": "29.9145",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367142",
                "lat": "29.914495",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367132",
                "lat": "29.914495",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 197,
        "position": [
            {
                "lng": "103.367435",
                "lat": "29.909755",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367292",
                "lat": "29.909808",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367247",
                "lat": "29.909825",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 198,
        "position": [
            {
                "lng": "103.367221",
                "lat": "29.909834",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36717",
                "lat": "29.909854",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 199,
        "position": [
            {
                "lng": "103.369993",
                "lat": "29.909089",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369977",
                "lat": "29.908995",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 200,
        "position": [
            {
                "lng": "103.372383",
                "lat": "29.921292",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372328",
                "lat": "29.920994",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372089",
                "lat": "29.919947",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371678",
                "lat": "29.918123",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 201,
        "position": [
            {
                "lng": "103.371673",
                "lat": "29.918099",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371672",
                "lat": "29.918095",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371947",
                "lat": "29.917887",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371767",
                "lat": "29.917109",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371616",
                "lat": "29.916423",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371495",
                "lat": "29.915825",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371296",
                "lat": "29.914868",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371353",
                "lat": "29.914865",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371352",
                "lat": "29.914853",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 202,
        "position": [
            {
                "lng": "103.37135",
                "lat": "29.914829",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371335",
                "lat": "29.914627",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.373394",
                "lat": "29.914451",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.375482",
                "lat": "29.9143",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 203,
        "position": [
            {
                "lng": "103.370048",
                "lat": "29.907857",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370101",
                "lat": "29.90841",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370183",
                "lat": "29.909074",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370491",
                "lat": "29.911249",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370711",
                "lat": "29.912979",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370906",
                "lat": "29.914367",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370914",
                "lat": "29.914428",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 204,
        "position": [
            {
                "lng": "103.370918",
                "lat": "29.914451",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370975",
                "lat": "29.914861",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371121",
                "lat": "29.915764",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371304",
                "lat": "29.916776",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371477",
                "lat": "29.917663",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 205,
        "position": [
            {
                "lng": "103.371482",
                "lat": "29.917687",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371566",
                "lat": "29.917986",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 206,
        "position": [
            {
                "lng": "103.367999",
                "lat": "29.915224",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368002",
                "lat": "29.915223",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36814",
                "lat": "29.915491",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 207,
        "position": [
            {
                "lng": "103.370488",
                "lat": "29.911228",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370301",
                "lat": "29.911265",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 208,
        "position": [
            {
                "lng": "103.370274",
                "lat": "29.91127",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369975",
                "lat": "29.911327",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369452",
                "lat": "29.911434",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368943",
                "lat": "29.911536",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.367843",
                "lat": "29.911785",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 209,
        "position": [
            {
                "lng": "103.372387",
                "lat": "29.921316",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.37246",
                "lat": "29.921711",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372333",
                "lat": "29.921845",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372368",
                "lat": "29.922031",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372578",
                "lat": "29.922101",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372565",
                "lat": "29.922352",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372538",
                "lat": "29.922631",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372446",
                "lat": "29.922904",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372336",
                "lat": "29.923166",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372008",
                "lat": "29.923592",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372312",
                "lat": "29.923939",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.372241",
                "lat": "29.923985",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371791",
                "lat": "29.924292",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371694",
                "lat": "29.924353",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371548",
                "lat": "29.924444",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371377",
                "lat": "29.924553",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.371025",
                "lat": "29.924787",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370602",
                "lat": "29.925063",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370106",
                "lat": "29.925414",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.369703",
                "lat": "29.925689",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368873",
                "lat": "29.92615",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36848",
                "lat": "29.926346",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.368103",
                "lat": "29.926439",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36811",
                "lat": "29.92648",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.372146",
                    "lat": "29.923413",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.372008",
                    "lat": "29.923592",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.372304",
                    "lat": "29.923929",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.372043",
                    "lat": "29.92412",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.371858",
                    "lat": "29.924246",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.371914",
                    "lat": "29.924208",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.371791",
                    "lat": "29.924292",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.371694",
                    "lat": "29.924353",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.371691",
                    "lat": "29.924355",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.371538",
                    "lat": "29.924451",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.371377",
                    "lat": "29.924553",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.371296",
                    "lat": "29.924607",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.3713",
                    "lat": "29.924604",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.371081",
                    "lat": "29.92475",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.371009",
                    "lat": "29.924797",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370758",
                    "lat": "29.924961",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370951",
                    "lat": "29.924835",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370602",
                    "lat": "29.925063",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370602",
                    "lat": "29.925063",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370507",
                    "lat": "29.92513",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370682",
                    "lat": "29.925011",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370602",
                    "lat": "29.925063",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370602",
                    "lat": "29.925063",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370472",
                    "lat": "29.925155",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370472",
                    "lat": "29.925155",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370378",
                    "lat": "29.925222",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370556",
                    "lat": "29.925096",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370472",
                    "lat": "29.925155",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370472",
                    "lat": "29.925155",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370257",
                    "lat": "29.925307",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370439",
                    "lat": "29.925178",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370106",
                    "lat": "29.925414",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370106",
                    "lat": "29.925414",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370063",
                    "lat": "29.925443",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370214",
                    "lat": "29.925337",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.370106",
                    "lat": "29.925414",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.370106",
                    "lat": "29.925414",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.369886",
                    "lat": "29.925564",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.369848",
                    "lat": "29.92559",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.369703",
                    "lat": "29.925689",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.369703",
                    "lat": "29.925689",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.369571",
                    "lat": "29.925762",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.369733",
                    "lat": "29.925668",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.369703",
                    "lat": "29.925689",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.369703",
                    "lat": "29.925689",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.369281",
                    "lat": "29.925923",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.369478",
                    "lat": "29.925814",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.369075",
                    "lat": "29.926038",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.369221",
                    "lat": "29.925957",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.368899",
                    "lat": "29.926136",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36908",
                    "lat": "29.926035",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.368873",
                    "lat": "29.92615",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.368716",
                    "lat": "29.926228",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.368241",
                    "lat": "29.926405",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.368103",
                    "lat": "29.926439",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.368103",
                    "lat": "29.926439",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.368106",
                    "lat": "29.926456",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.368205",
                    "lat": "29.926414",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.368103",
                    "lat": "29.926439",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.368103",
                    "lat": "29.926439",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36811",
                    "lat": "29.926478",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 210,
        "position": [
            {
                "lng": "103.370669",
                "lat": "29.922329",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370683",
                "lat": "29.922395",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 211,
        "position": [
            {
                "lng": "103.370687",
                "lat": "29.922418",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370733",
                "lat": "29.922658",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370715",
                "lat": "29.922661",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.37072",
                "lat": "29.922685",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 212,
        "position": [
            {
                "lng": "103.37072",
                "lat": "29.922685",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370758",
                "lat": "29.92288",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 213,
        "position": [
            {
                "lng": "103.370756",
                "lat": "29.922867",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370414",
                "lat": "29.92292",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.370411",
                "lat": "29.922903",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 214,
        "position": [
            {
                "lng": "103.383297",
                "lat": "29.907574",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.3833",
                "lat": "29.907444",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 215,
        "position": [
            {
                "lng": "103.383381",
                "lat": "29.90792",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.384358",
                "lat": "29.907634",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.384378",
                "lat": "29.907685",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 216,
        "position": [
            {
                "lng": "103.38309",
                "lat": "29.90743",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383097",
                "lat": "29.90741",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 217,
        "position": [
            {
                "lng": "103.383287",
                "lat": "29.907729",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383365",
                "lat": "29.907912",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 218,
        "position": [
            {
                "lng": "103.395015",
                "lat": "29.909722",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394995",
                "lat": "29.909707",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394917",
                "lat": "29.909622",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394885",
                "lat": "29.909543",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394856",
                "lat": "29.909332",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394836",
                "lat": "29.909128",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394861",
                "lat": "29.908903",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394895",
                "lat": "29.908675",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394761",
                "lat": "29.908651",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394766",
                "lat": "29.908397",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394726",
                "lat": "29.908229",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394626",
                "lat": "29.908079",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394366",
                "lat": "29.907882",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.392974",
                "lat": "29.90706",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.392929",
                "lat": "29.907033",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.392252",
                "lat": "29.906656",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.391624",
                "lat": "29.906413",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.390965",
                "lat": "29.906158",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.390228",
                "lat": "29.90595",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.389755",
                "lat": "29.90589",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.388997",
                "lat": "29.905839",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.388523",
                "lat": "29.905885",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.387819",
                "lat": "29.90607",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.387014",
                "lat": "29.906327",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.385629",
                "lat": "29.906783",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.385587",
                "lat": "29.906695",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.384851",
                "lat": "29.906937",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383956",
                "lat": "29.907238",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383344",
                "lat": "29.907439",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383249",
                "lat": "29.907448",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.395015",
                    "lat": "29.909722",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394995",
                    "lat": "29.909707",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394995",
                    "lat": "29.909707",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394917",
                    "lat": "29.909622",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394917",
                    "lat": "29.909622",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394886",
                    "lat": "29.909545",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394917",
                    "lat": "29.909622",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394885",
                    "lat": "29.909543",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394884",
                    "lat": "29.909536",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 219,
        "position": [
            {
                "lng": "103.401284",
                "lat": "29.911766",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.401289",
                "lat": "29.911752",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.401284",
                    "lat": "29.911766",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401289",
                    "lat": "29.911752",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 220,
        "position": [
            {
                "lng": "103.385078",
                "lat": "29.912153",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.385294",
                "lat": "29.912023",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.386499",
                "lat": "29.911378",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.387909",
                "lat": "29.910681",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.38945",
                "lat": "29.910142",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.390142",
                "lat": "29.909898",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.390996",
                "lat": "29.909679",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.392062",
                "lat": "29.909453",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.392582",
                "lat": "29.909367",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.393061",
                "lat": "29.909321",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.393069",
                "lat": "29.909515",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.393093",
                "lat": "29.909544",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.393251",
                "lat": "29.909557",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.393262",
                "lat": "29.909505",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.393704",
                "lat": "29.909537",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.394108",
                "lat": "29.909602",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.395052",
                "lat": "29.909871",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.394978",
                    "lat": "29.90985",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395052",
                    "lat": "29.909871",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394691",
                    "lat": "29.909768",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394767",
                    "lat": "29.90979",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394767",
                    "lat": "29.90979",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395052",
                    "lat": "29.909871",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394448",
                    "lat": "29.909699",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394541",
                    "lat": "29.909726",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394541",
                    "lat": "29.909726",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395052",
                    "lat": "29.909871",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394226",
                    "lat": "29.909636",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394455",
                    "lat": "29.909701",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394455",
                    "lat": "29.909701",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394541",
                    "lat": "29.909726",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394541",
                    "lat": "29.909726",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394767",
                    "lat": "29.90979",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394767",
                    "lat": "29.90979",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394923",
                    "lat": "29.909834",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393971",
                    "lat": "29.90958",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394108",
                    "lat": "29.909602",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394108",
                    "lat": "29.909602",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394455",
                    "lat": "29.909701",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394455",
                    "lat": "29.909701",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394658",
                    "lat": "29.909759",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393717",
                    "lat": "29.909539",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394108",
                    "lat": "29.909602",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.394108",
                    "lat": "29.909602",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394406",
                    "lat": "29.909687",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393518",
                    "lat": "29.909524",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393704",
                    "lat": "29.909537",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393704",
                    "lat": "29.909537",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.394037",
                    "lat": "29.909591",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393237",
                    "lat": "29.909556",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393251",
                    "lat": "29.909557",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393251",
                    "lat": "29.909557",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393262",
                    "lat": "29.909505",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393262",
                    "lat": "29.909505",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393704",
                    "lat": "29.909537",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393704",
                    "lat": "29.909537",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393751",
                    "lat": "29.909545",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392971",
                    "lat": "29.90933",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393061",
                    "lat": "29.909321",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393061",
                    "lat": "29.909321",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393069",
                    "lat": "29.909515",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393069",
                    "lat": "29.909515",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393093",
                    "lat": "29.909544",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393093",
                    "lat": "29.909544",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393251",
                    "lat": "29.909557",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393262",
                    "lat": "29.909505",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393652",
                    "lat": "29.909533",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392681",
                    "lat": "29.909357",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393061",
                    "lat": "29.909321",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.393262",
                    "lat": "29.909505",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393381",
                    "lat": "29.909514",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392587",
                    "lat": "29.909367",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392804",
                    "lat": "29.909346",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392804",
                    "lat": "29.909346",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.393061",
                    "lat": "29.909321",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392347",
                    "lat": "29.909406",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392582",
                    "lat": "29.909367",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392582",
                    "lat": "29.909367",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392804",
                    "lat": "29.909346",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392804",
                    "lat": "29.909346",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392835",
                    "lat": "29.909343",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392116",
                    "lat": "29.909444",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392177",
                    "lat": "29.909434",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392177",
                    "lat": "29.909434",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392582",
                    "lat": "29.909367",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392582",
                    "lat": "29.909367",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392741",
                    "lat": "29.909352",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.391945",
                    "lat": "29.909478",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392062",
                    "lat": "29.909453",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392062",
                    "lat": "29.909453",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392177",
                    "lat": "29.909434",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392177",
                    "lat": "29.909434",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392502",
                    "lat": "29.90938",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.391725",
                    "lat": "29.909524",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.391853",
                    "lat": "29.909497",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.391853",
                    "lat": "29.909497",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392062",
                    "lat": "29.909453",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.392062",
                    "lat": "29.909453",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.392216",
                    "lat": "29.909428",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.391473",
                    "lat": "29.909578",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.391853",
                    "lat": "29.909497",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.391853",
                    "lat": "29.909497",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.391886",
                    "lat": "29.90949",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.391227",
                    "lat": "29.90963",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.391792",
                    "lat": "29.90951",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390982",
                    "lat": "29.909683",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390996",
                    "lat": "29.909679",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390996",
                    "lat": "29.909679",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.391516",
                    "lat": "29.909569",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390771",
                    "lat": "29.909737",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390996",
                    "lat": "29.909679",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390996",
                    "lat": "29.909679",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.391344",
                    "lat": "29.909605",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390523",
                    "lat": "29.9098",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390673",
                    "lat": "29.909762",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390673",
                    "lat": "29.909762",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390996",
                    "lat": "29.909679",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390996",
                    "lat": "29.909679",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.391128",
                    "lat": "29.909651",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390258",
                    "lat": "29.909868",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390284",
                    "lat": "29.909861",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390284",
                    "lat": "29.909861",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390673",
                    "lat": "29.909762",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390673",
                    "lat": "29.909762",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390812",
                    "lat": "29.909726",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390065",
                    "lat": "29.909925",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390142",
                    "lat": "29.909898",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390142",
                    "lat": "29.909898",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390642",
                    "lat": "29.90977",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.389919",
                    "lat": "29.909977",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390142",
                    "lat": "29.909898",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390142",
                    "lat": "29.909898",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390284",
                    "lat": "29.909861",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390284",
                    "lat": "29.909861",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390386",
                    "lat": "29.909835",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.389617",
                    "lat": "29.910083",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.389882",
                    "lat": "29.90999",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.389882",
                    "lat": "29.90999",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390142",
                    "lat": "29.909898",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.390142",
                    "lat": "29.909898",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390203",
                    "lat": "29.909882",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38934",
                    "lat": "29.91018",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38945",
                    "lat": "29.910142",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38945",
                    "lat": "29.910142",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.389882",
                    "lat": "29.90999",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.389882",
                    "lat": "29.90999",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.390017",
                    "lat": "29.909942",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38914",
                    "lat": "29.91025",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38945",
                    "lat": "29.910142",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38945",
                    "lat": "29.910142",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.389678",
                    "lat": "29.910062",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.388878",
                    "lat": "29.910342",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.389057",
                    "lat": "29.910279",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.389057",
                    "lat": "29.910279",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38945",
                    "lat": "29.910142",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38945",
                    "lat": "29.910142",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.389519",
                    "lat": "29.910118",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38875",
                    "lat": "29.910387",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38878",
                    "lat": "29.910377",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38878",
                    "lat": "29.910377",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.389057",
                    "lat": "29.910279",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.389057",
                    "lat": "29.910279",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.389198",
                    "lat": "29.91023",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.388486",
                    "lat": "29.910479",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38878",
                    "lat": "29.910377",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38878",
                    "lat": "29.910377",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.388942",
                    "lat": "29.91032",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.388448",
                    "lat": "29.910493",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.388902",
                    "lat": "29.910334",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38814",
                    "lat": "29.9106",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.388208",
                    "lat": "29.910576",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.388208",
                    "lat": "29.910576",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.388602",
                    "lat": "29.910439",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.387958",
                    "lat": "29.910664",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.388208",
                    "lat": "29.910576",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.388208",
                    "lat": "29.910576",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.388531",
                    "lat": "29.910463",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.387591",
                    "lat": "29.910838",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387675",
                    "lat": "29.910797",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.387675",
                    "lat": "29.910797",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387909",
                    "lat": "29.910681",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.388065",
                    "lat": "29.910627",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.387319",
                    "lat": "29.910973",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387431",
                    "lat": "29.910917",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.387431",
                    "lat": "29.910917",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387675",
                    "lat": "29.910797",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.387675",
                    "lat": "29.910797",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387785",
                    "lat": "29.910742",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.387127",
                    "lat": "29.911068",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387604",
                    "lat": "29.910832",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.386891",
                    "lat": "29.911184",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387431",
                    "lat": "29.910917",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.387431",
                    "lat": "29.910917",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387434",
                    "lat": "29.910916",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.386807",
                    "lat": "29.911226",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387256",
                    "lat": "29.911004",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.386587",
                    "lat": "29.911334",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.387027",
                    "lat": "29.911117",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38639",
                    "lat": "29.911436",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.386499",
                    "lat": "29.911378",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.386499",
                    "lat": "29.911378",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.386946",
                    "lat": "29.911157",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.386142",
                    "lat": "29.911569",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.386499",
                    "lat": "29.911378",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.386499",
                    "lat": "29.911378",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.386734",
                    "lat": "29.911262",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385884",
                    "lat": "29.911707",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.386474",
                    "lat": "29.911391",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385683",
                    "lat": "29.911815",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.386224",
                    "lat": "29.911525",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385443",
                    "lat": "29.911943",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385674",
                    "lat": "29.911819",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385674",
                    "lat": "29.911819",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385939",
                    "lat": "29.911677",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385275",
                    "lat": "29.912034",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385294",
                    "lat": "29.912023",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385294",
                    "lat": "29.912023",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385674",
                    "lat": "29.911819",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385674",
                    "lat": "29.911819",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385773",
                    "lat": "29.911766",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385149",
                    "lat": "29.912111",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385294",
                    "lat": "29.912023",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385294",
                    "lat": "29.912023",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38557",
                    "lat": "29.911875",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385078",
                    "lat": "29.912153",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385294",
                    "lat": "29.912023",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385294",
                    "lat": "29.912023",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385422",
                    "lat": "29.911954",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.385078",
                    "lat": "29.912153",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385277",
                    "lat": "29.912033",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 221,
        "position": [
            {
                "lng": "103.395078",
                "lat": "29.909878",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.39513",
                "lat": "29.909894",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.396619",
                "lat": "29.910331",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.397914",
                "lat": "29.910712",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.399005",
                "lat": "29.911039",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.400571",
                "lat": "29.911541",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.401307",
                "lat": "29.911773",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.401231",
                    "lat": "29.911749",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401307",
                    "lat": "29.911773",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401147",
                    "lat": "29.911723",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401307",
                    "lat": "29.911773",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401084",
                    "lat": "29.911703",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401307",
                    "lat": "29.911773",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400829",
                    "lat": "29.911622",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400929",
                    "lat": "29.911654",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400929",
                    "lat": "29.911654",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401039",
                    "lat": "29.911688",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401039",
                    "lat": "29.911688",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401307",
                    "lat": "29.911773",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.40058",
                    "lat": "29.911544",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400643",
                    "lat": "29.911564",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400643",
                    "lat": "29.911564",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401039",
                    "lat": "29.911688",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401039",
                    "lat": "29.911688",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401216",
                    "lat": "29.911744",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400335",
                    "lat": "29.911465",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400399",
                    "lat": "29.911485",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400399",
                    "lat": "29.911485",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400571",
                    "lat": "29.911541",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400571",
                    "lat": "29.911541",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400929",
                    "lat": "29.911654",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400929",
                    "lat": "29.911654",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400978",
                    "lat": "29.911669",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400114",
                    "lat": "29.911395",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400571",
                    "lat": "29.911541",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400571",
                    "lat": "29.911541",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400643",
                    "lat": "29.911564",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400643",
                    "lat": "29.911564",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400773",
                    "lat": "29.911605",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399985",
                    "lat": "29.911353",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400399",
                    "lat": "29.911485",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.400399",
                    "lat": "29.911485",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400497",
                    "lat": "29.911517",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39976",
                    "lat": "29.911281",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399842",
                    "lat": "29.911307",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399842",
                    "lat": "29.911307",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399849",
                    "lat": "29.911309",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399849",
                    "lat": "29.911309",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400306",
                    "lat": "29.911456",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399481",
                    "lat": "29.911192",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39982",
                    "lat": "29.9113",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39982",
                    "lat": "29.9113",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399842",
                    "lat": "29.911307",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399842",
                    "lat": "29.911307",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.400148",
                    "lat": "29.911405",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399231",
                    "lat": "29.911112",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39982",
                    "lat": "29.9113",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39982",
                    "lat": "29.9113",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399849",
                    "lat": "29.911309",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399849",
                    "lat": "29.911309",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399863",
                    "lat": "29.911314",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398878",
                    "lat": "29.911001",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399005",
                    "lat": "29.911039",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399005",
                    "lat": "29.911039",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399389",
                    "lat": "29.911162",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398761",
                    "lat": "29.910966",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399005",
                    "lat": "29.911039",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399005",
                    "lat": "29.911039",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399274",
                    "lat": "29.911125",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398519",
                    "lat": "29.910893",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399005",
                    "lat": "29.911039",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.399005",
                    "lat": "29.911039",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.399033",
                    "lat": "29.911048",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398301",
                    "lat": "29.910828",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398965",
                    "lat": "29.911027",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.398129",
                    "lat": "29.910777",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39872",
                    "lat": "29.910954",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397897",
                    "lat": "29.910707",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397914",
                    "lat": "29.910712",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397914",
                    "lat": "29.910712",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39848",
                    "lat": "29.910882",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397653",
                    "lat": "29.910635",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397914",
                    "lat": "29.910712",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397914",
                    "lat": "29.910712",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.398299",
                    "lat": "29.910827",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397374",
                    "lat": "29.910553",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397476",
                    "lat": "29.910583",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397476",
                    "lat": "29.910583",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397635",
                    "lat": "29.91063",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397635",
                    "lat": "29.91063",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397889",
                    "lat": "29.910705",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397134",
                    "lat": "29.910483",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397635",
                    "lat": "29.91063",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397635",
                    "lat": "29.91063",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397778",
                    "lat": "29.910672",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396859",
                    "lat": "29.910402",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397476",
                    "lat": "29.910583",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.397476",
                    "lat": "29.910583",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397554",
                    "lat": "29.910606",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396596",
                    "lat": "29.910324",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396619",
                    "lat": "29.910331",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396619",
                    "lat": "29.910331",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397258",
                    "lat": "29.910519",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39638",
                    "lat": "29.910261",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396619",
                    "lat": "29.910331",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396619",
                    "lat": "29.910331",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.397059",
                    "lat": "29.91046",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396148",
                    "lat": "29.910193",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396619",
                    "lat": "29.910331",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.396619",
                    "lat": "29.910331",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396806",
                    "lat": "29.910386",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395876",
                    "lat": "29.910113",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396561",
                    "lat": "29.910314",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395688",
                    "lat": "29.910058",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395799",
                    "lat": "29.910091",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395799",
                    "lat": "29.910091",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396202",
                    "lat": "29.910209",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.3955",
                    "lat": "29.910003",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395799",
                    "lat": "29.910091",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395799",
                    "lat": "29.910091",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.396029",
                    "lat": "29.910158",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395264",
                    "lat": "29.909933",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395833",
                    "lat": "29.9101",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.395078",
                    "lat": "29.909878",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39513",
                    "lat": "29.909894",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39513",
                    "lat": "29.909894",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395686",
                    "lat": "29.910057",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39513",
                    "lat": "29.909894",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395292",
                    "lat": "29.909941",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.39513",
                    "lat": "29.909894",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395209",
                    "lat": "29.909917",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 222,
        "position": [
            {
                "lng": "103.401333",
                "lat": "29.911782",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.401429",
                "lat": "29.911812",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.401333",
                    "lat": "29.911782",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401429",
                    "lat": "29.911812",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401333",
                    "lat": "29.911782",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.40141",
                    "lat": "29.911806",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 223,
        "position": [
            {
                "lng": "103.401296",
                "lat": "29.911729",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.401326",
                "lat": "29.911639",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.402391",
                "lat": "29.911975",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.402771",
                "lat": "29.912096",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.403606",
                "lat": "29.912436",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.405866",
                "lat": "29.913347",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.401972",
                    "lat": "29.911843",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.402311",
                    "lat": "29.91195",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401296",
                    "lat": "29.911729",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401314",
                    "lat": "29.911676",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401296",
                    "lat": "29.911729",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401326",
                    "lat": "29.911639",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401326",
                    "lat": "29.911639",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401619",
                    "lat": "29.911731",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.401326",
                    "lat": "29.911639",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.401425",
                    "lat": "29.91167",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 224,
        "position": [
            {
                "lng": "103.37931",
                "lat": "29.910449",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.380566",
                "lat": "29.910247",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.380749",
                "lat": "29.910962",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.381301",
                "lat": "29.913108",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 225,
        "position": [
            {
                "lng": "103.376833",
                "lat": "29.910881",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.378376",
                "lat": "29.910601",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.379283",
                "lat": "29.910454",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 226,
        "position": [
            {
                "lng": "103.381309",
                "lat": "29.91313",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.381335",
                "lat": "29.913184",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 227,
        "position": [
            {
                "lng": "103.381333",
                "lat": "29.913184",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.3815",
                "lat": "29.913528",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.381446",
                    "lat": "29.913417",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.3815",
                    "lat": "29.913528",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 228,
        "position": [
            {
                "lng": "103.381511",
                "lat": "29.91355",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.381694",
                "lat": "29.913924",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.381878",
                "lat": "29.914328",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.381835",
                "lat": "29.914372",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.38192",
                "lat": "29.914599",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.381989",
                "lat": "29.914604",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382396",
                "lat": "29.915558",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382068",
                "lat": "29.916687",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382262",
                "lat": "29.916926",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.381511",
                    "lat": "29.91355",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381644",
                    "lat": "29.913821",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381559",
                    "lat": "29.913649",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381694",
                    "lat": "29.913924",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381694",
                    "lat": "29.913924",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381769",
                    "lat": "29.914089",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381604",
                    "lat": "29.91374",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381694",
                    "lat": "29.913924",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381694",
                    "lat": "29.913924",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381878",
                    "lat": "29.914328",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381878",
                    "lat": "29.914328",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381865",
                    "lat": "29.914341",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381856",
                    "lat": "29.91428",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381878",
                    "lat": "29.914328",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381878",
                    "lat": "29.914328",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381835",
                    "lat": "29.914372",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38192",
                    "lat": "29.914599",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38192",
                    "lat": "29.914599",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381989",
                    "lat": "29.914604",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381989",
                    "lat": "29.914604",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382044",
                    "lat": "29.914733",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381869",
                    "lat": "29.914462",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38192",
                    "lat": "29.914599",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381989",
                    "lat": "29.914604",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382088",
                    "lat": "29.914836",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382023",
                    "lat": "29.914684",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382209",
                    "lat": "29.915119",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382199",
                    "lat": "29.915096",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382388",
                    "lat": "29.915539",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382235",
                    "lat": "29.915182",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382396",
                    "lat": "29.915558",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382357",
                    "lat": "29.915693",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382364",
                    "lat": "29.915668",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382297",
                    "lat": "29.915899",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382297",
                    "lat": "29.915899",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382224",
                    "lat": "29.91615",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382325",
                    "lat": "29.915802",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382297",
                    "lat": "29.915899",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382297",
                    "lat": "29.915899",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382188",
                    "lat": "29.916275",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382259",
                    "lat": "29.916029",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382123",
                    "lat": "29.916498",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382234",
                    "lat": "29.916117",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382072",
                    "lat": "29.916674",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382163",
                    "lat": "29.916361",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382068",
                    "lat": "29.916687",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382068",
                    "lat": "29.916687",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382262",
                    "lat": "29.916926",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382098",
                    "lat": "29.916583",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382068",
                    "lat": "29.916687",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 229,
        "position": [
            {
                "lng": "103.379607",
                "lat": "29.910402",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.3792",
                "lat": "29.908346",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 230,
        "position": [
            {
                "lng": "103.378791",
                "lat": "29.906357",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.378724",
                "lat": "29.906065",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 231,
        "position": [
            {
                "lng": "103.379096",
                "lat": "29.907697",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.378796",
                "lat": "29.90638",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 234,
        "position": [
            {
                "lng": "103.379102",
                "lat": "29.907723",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.379195",
                "lat": "29.908322",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 235,
        "position": [
            {
                "lng": "103.378724",
                "lat": "29.906065",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.378725",
                "lat": "29.905443",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 236,
        "position": [
            {
                "lng": "103.382007",
                "lat": "29.905699",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382123",
                "lat": "29.905835",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382096",
                "lat": "29.905918",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382053",
                "lat": "29.906093",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.38208",
                "lat": "29.906235",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382174",
                "lat": "29.906359",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382329",
                "lat": "29.906576",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382581",
                "lat": "29.90691",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382772",
                "lat": "29.907174",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383012",
                "lat": "29.907398",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383126",
                "lat": "29.907445",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383222",
                "lat": "29.907448",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 237,
        "position": [
            {
                "lng": "103.37551",
                "lat": "29.914299",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.375591",
                "lat": "29.914293",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.375846",
                "lat": "29.914275",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.377082",
                "lat": "29.914164",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.378084",
                "lat": "29.913991",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.379567",
                "lat": "29.913626",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.38117",
                "lat": "29.913224",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 238,
        "position": [
            {
                "lng": "103.381196",
                "lat": "29.913218",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.381333",
                "lat": "29.913184",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.382626",
                "lat": "29.913103",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383121",
                "lat": "29.913015",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.383515",
                "lat": "29.912884",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.38388",
                "lat": "29.912721",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.384741",
                "lat": "29.912333",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.384942",
                "lat": "29.91223",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.384996",
                "lat": "29.912202",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.385055",
                "lat": "29.912166",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.384942",
                    "lat": "29.91223",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384996",
                    "lat": "29.912202",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.384996",
                    "lat": "29.912202",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385055",
                    "lat": "29.912166",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.384677",
                    "lat": "29.912362",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384741",
                    "lat": "29.912333",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.384741",
                    "lat": "29.912333",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384942",
                    "lat": "29.91223",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.384458",
                    "lat": "29.912461",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384741",
                    "lat": "29.912333",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.384996",
                    "lat": "29.912202",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.385027",
                    "lat": "29.912183",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.384282",
                    "lat": "29.91254",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38442",
                    "lat": "29.912478",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38442",
                    "lat": "29.912478",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384741",
                    "lat": "29.912333",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.384741",
                    "lat": "29.912333",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384796",
                    "lat": "29.912305",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.384173",
                    "lat": "29.912589",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38442",
                    "lat": "29.912478",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38442",
                    "lat": "29.912478",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384606",
                    "lat": "29.912394",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383931",
                    "lat": "29.912698",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384392",
                    "lat": "29.91249",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383705",
                    "lat": "29.912799",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383726",
                    "lat": "29.91279",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383726",
                    "lat": "29.91279",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38388",
                    "lat": "29.912721",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38388",
                    "lat": "29.912721",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384169",
                    "lat": "29.912591",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383444",
                    "lat": "29.912908",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383515",
                    "lat": "29.912884",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383515",
                    "lat": "29.912884",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38388",
                    "lat": "29.912721",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38388",
                    "lat": "29.912721",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.384102",
                    "lat": "29.912621",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383292",
                    "lat": "29.912958",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383515",
                    "lat": "29.912884",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383515",
                    "lat": "29.912884",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383726",
                    "lat": "29.91279",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383726",
                    "lat": "29.91279",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383837",
                    "lat": "29.91274",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383052",
                    "lat": "29.913027",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383121",
                    "lat": "29.913015",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383121",
                    "lat": "29.913015",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383515",
                    "lat": "29.912884",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383515",
                    "lat": "29.912884",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383605",
                    "lat": "29.912844",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382811",
                    "lat": "29.91307",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382834",
                    "lat": "29.913066",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382834",
                    "lat": "29.913066",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383121",
                    "lat": "29.913015",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383121",
                    "lat": "29.913015",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383435",
                    "lat": "29.912911",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382536",
                    "lat": "29.913109",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382626",
                    "lat": "29.913103",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382626",
                    "lat": "29.913103",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383121",
                    "lat": "29.913015",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.383121",
                    "lat": "29.913015",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.383168",
                    "lat": "29.912999",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382242",
                    "lat": "29.913127",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382626",
                    "lat": "29.913103",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382626",
                    "lat": "29.913103",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382834",
                    "lat": "29.913066",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382834",
                    "lat": "29.913066",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382985",
                    "lat": "29.913039",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382051",
                    "lat": "29.913139",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382056",
                    "lat": "29.913139",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382056",
                    "lat": "29.913139",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382067",
                    "lat": "29.913138",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382067",
                    "lat": "29.913138",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382626",
                    "lat": "29.913103",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382626",
                    "lat": "29.913103",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.38267",
                    "lat": "29.913095",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.38191",
                    "lat": "29.913148",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382062",
                    "lat": "29.913138",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382062",
                    "lat": "29.913138",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382067",
                    "lat": "29.913138",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382067",
                    "lat": "29.913138",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382428",
                    "lat": "29.913115",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381742",
                    "lat": "29.913158",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381998",
                    "lat": "29.913142",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381998",
                    "lat": "29.913142",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382056",
                    "lat": "29.913139",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382056",
                    "lat": "29.913139",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382062",
                    "lat": "29.913138",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.382062",
                    "lat": "29.913138",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382246",
                    "lat": "29.913127",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381545",
                    "lat": "29.913171",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381998",
                    "lat": "29.913142",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381998",
                    "lat": "29.913142",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.382002",
                    "lat": "29.913142",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.381605",
                    "lat": "29.913167",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.381794",
                    "lat": "29.913155",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 239,
        "position": [
            {
                "lng": "103.373022",
                "lat": "29.905226",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.373025",
                "lat": "29.905285",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 240,
        "position": [
            {
                "lng": "103.373029",
                "lat": "29.905309",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.373112",
                "lat": "29.905703",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.373195",
                "lat": "29.906017",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.373462",
                "lat": "29.906862",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.373777",
                "lat": "29.907839",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.374066",
                "lat": "29.908775",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.374273",
                "lat": "29.909427",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.374549",
                "lat": "29.91024",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 241,
        "position": [
            {
                "lng": "103.374557",
                "lat": "29.910263",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.374585",
                "lat": "29.910346",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.374908",
                "lat": "29.911367",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.375238",
                "lat": "29.912368",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 242,
        "position": [
            {
                "lng": "103.375246",
                "lat": "29.912391",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.375385",
                "lat": "29.912813",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.375565",
                "lat": "29.913753",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.375668",
                "lat": "29.914288",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 243,
        "position": [
            {
                "lng": "103.363118",
                "lat": "29.915109",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36311",
                "lat": "29.915096",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 244,
        "position": [
            {
                "lng": "103.363096",
                "lat": "29.915076",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363076",
                "lat": "29.915054",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36322",
                "lat": "29.914972",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 245,
        "position": [
            {
                "lng": "103.365942",
                "lat": "29.913054",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36593",
                "lat": "29.91304",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365886",
                "lat": "29.913075",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 246,
        "position": [
            {
                "lng": "103.365866",
                "lat": "29.913091",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364315",
                "lat": "29.914344",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364201",
                "lat": "29.914436",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363926",
                "lat": "29.914588",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363882",
                "lat": "29.914809",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363878",
                "lat": "29.914812",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 247,
        "position": [
            {
                "lng": "103.363926",
                "lat": "29.914588",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36381",
                "lat": "29.914408",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363782",
                "lat": "29.914345",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363699",
                "lat": "29.914389",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363496",
                "lat": "29.91435",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363448",
                "lat": "29.914341",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363416",
                "lat": "29.914298",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363147",
                "lat": "29.914423",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363057",
                "lat": "29.914727",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.363042",
                "lat": "29.914736",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36322",
                "lat": "29.914972",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 248,
        "position": [
            {
                "lng": "103.363147",
                "lat": "29.914423",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362997",
                "lat": "29.914195",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36277",
                "lat": "29.914327",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362854",
                "lat": "29.914441",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 249,
        "position": [
            {
                "lng": "103.362997",
                "lat": "29.914195",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362878",
                "lat": "29.914029",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362878",
                "lat": "29.914032",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [],
        "noCompletion": []
    },
    {
        "deviceId": 250,
        "position": [
            {
                "lng": "103.395034",
                "lat": "29.909739",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.39509",
                "lat": "29.909778",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.395165",
                "lat": "29.909802",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.39513",
                "lat": "29.909894",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.395034",
                    "lat": "29.909739",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39509",
                    "lat": "29.909778",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.395165",
                    "lat": "29.909802",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.39513",
                    "lat": "29.909894",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 251,
        "position": [
            {
                "lng": "103.365018",
                "lat": "29.925966",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.365013",
                "lat": "29.926004",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36492",
                "lat": "29.926412",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.364826",
                "lat": "29.926465",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36453",
                "lat": "29.926505",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36311",
                "lat": "29.92656",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362642",
                "lat": "29.926463",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361719",
                "lat": "29.925866",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36146",
                "lat": "29.926134",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.361312",
                "lat": "29.926053",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.360596",
                "lat": "29.925583",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.359675",
                "lat": "29.924929",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.358956",
                "lat": "29.924359",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.358708",
                "lat": "29.924107",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.358428",
                "lat": "29.92362",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.35721",
                "lat": "29.921484",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357475",
                "lat": "29.921358",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357434",
                "lat": "29.921277",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.364815",
                    "lat": "29.926467",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364755",
                    "lat": "29.926475",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.364696",
                    "lat": "29.926483",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.364624",
                    "lat": "29.926492",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363504",
                    "lat": "29.926545",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363237",
                    "lat": "29.926555",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.363334",
                    "lat": "29.926551",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36311",
                    "lat": "29.92656",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.363072",
                    "lat": "29.926552",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362975",
                    "lat": "29.926532",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362728",
                    "lat": "29.926481",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362728",
                    "lat": "29.926481",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362646",
                    "lat": "29.926464",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362872",
                    "lat": "29.926511",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362728",
                    "lat": "29.926481",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362728",
                    "lat": "29.926481",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362642",
                    "lat": "29.926463",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362642",
                    "lat": "29.926463",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362555",
                    "lat": "29.926406",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362715",
                    "lat": "29.926478",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362642",
                    "lat": "29.926463",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362642",
                    "lat": "29.926463",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362424",
                    "lat": "29.926322",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362526",
                    "lat": "29.926388",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362424",
                    "lat": "29.926322",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362424",
                    "lat": "29.926322",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362322",
                    "lat": "29.926256",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362406",
                    "lat": "29.92631",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36218",
                    "lat": "29.926164",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361689",
                    "lat": "29.925897",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36146",
                    "lat": "29.926134",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36146",
                    "lat": "29.926134",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361312",
                    "lat": "29.926053",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361312",
                    "lat": "29.926053",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361268",
                    "lat": "29.926024",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361312",
                    "lat": "29.926053",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361218",
                    "lat": "29.925991",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361383",
                    "lat": "29.926092",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361312",
                    "lat": "29.926053",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361312",
                    "lat": "29.926053",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36096",
                    "lat": "29.925822",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361319",
                    "lat": "29.926057",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361312",
                    "lat": "29.926053",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361312",
                    "lat": "29.926053",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360745",
                    "lat": "29.925681",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360745",
                    "lat": "29.925681",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360718",
                    "lat": "29.925663",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361029",
                    "lat": "29.925867",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360745",
                    "lat": "29.925681",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360745",
                    "lat": "29.925681",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360596",
                    "lat": "29.925583",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360596",
                    "lat": "29.925583",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36047",
                    "lat": "29.925494",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360664",
                    "lat": "29.925628",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360596",
                    "lat": "29.925583",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360596",
                    "lat": "29.925583",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360231",
                    "lat": "29.925324",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360495",
                    "lat": "29.925511",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360213",
                    "lat": "29.925311",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360213",
                    "lat": "29.925311",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360059",
                    "lat": "29.925202",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360389",
                    "lat": "29.925436",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360213",
                    "lat": "29.925311",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360213",
                    "lat": "29.925311",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35989",
                    "lat": "29.925082",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360153",
                    "lat": "29.925268",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360022",
                    "lat": "29.925175",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360022",
                    "lat": "29.925175",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359783",
                    "lat": "29.925006",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359783",
                    "lat": "29.925006",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359714",
                    "lat": "29.924957",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360033",
                    "lat": "29.925183",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360022",
                    "lat": "29.925175",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360022",
                    "lat": "29.925175",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359675",
                    "lat": "29.924929",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359675",
                    "lat": "29.924929",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359598",
                    "lat": "29.924868",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359911",
                    "lat": "29.925097",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359783",
                    "lat": "29.925006",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359783",
                    "lat": "29.925006",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359675",
                    "lat": "29.924929",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359675",
                    "lat": "29.924929",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359367",
                    "lat": "29.924684",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359737",
                    "lat": "29.924973",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359675",
                    "lat": "29.924929",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359675",
                    "lat": "29.924929",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359155",
                    "lat": "29.924516",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359155",
                    "lat": "29.924516",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359147",
                    "lat": "29.92451",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359459",
                    "lat": "29.924758",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358986",
                    "lat": "29.924383",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359257",
                    "lat": "29.924597",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359155",
                    "lat": "29.924516",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359155",
                    "lat": "29.924516",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358956",
                    "lat": "29.924359",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358956",
                    "lat": "29.924359",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358848",
                    "lat": "29.924249",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.35905",
                    "lat": "29.924433",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358956",
                    "lat": "29.924359",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358956",
                    "lat": "29.924359",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358708",
                    "lat": "29.924107",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358708",
                    "lat": "29.924107",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358675",
                    "lat": "29.924049",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.35883",
                    "lat": "29.924231",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358708",
                    "lat": "29.924107",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358708",
                    "lat": "29.924107",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358533",
                    "lat": "29.923802",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358533",
                    "lat": "29.923802",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358525",
                    "lat": "29.923789",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358614",
                    "lat": "29.923944",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358533",
                    "lat": "29.923802",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358533",
                    "lat": "29.923802",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358428",
                    "lat": "29.92362",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358428",
                    "lat": "29.92362",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358347",
                    "lat": "29.923478",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358554",
                    "lat": "29.92384",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358428",
                    "lat": "29.92362",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358428",
                    "lat": "29.92362",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358288",
                    "lat": "29.923374",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358457",
                    "lat": "29.92367",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358428",
                    "lat": "29.92362",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358428",
                    "lat": "29.92362",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358193",
                    "lat": "29.923208",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358282",
                    "lat": "29.923365",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358019",
                    "lat": "29.922903",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.35822",
                    "lat": "29.923255",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358013",
                    "lat": "29.922892",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358013",
                    "lat": "29.922892",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357934",
                    "lat": "29.922753",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358104",
                    "lat": "29.923051",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358013",
                    "lat": "29.922892",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358013",
                    "lat": "29.922892",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357839",
                    "lat": "29.922587",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358048",
                    "lat": "29.922954",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357756",
                    "lat": "29.922442",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357756",
                    "lat": "29.922442",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357729",
                    "lat": "29.922394",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357875",
                    "lat": "29.922651",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357758",
                    "lat": "29.922446",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357758",
                    "lat": "29.922446",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357756",
                    "lat": "29.922442",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357756",
                    "lat": "29.922442",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357611",
                    "lat": "29.922186",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357774",
                    "lat": "29.922473",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357758",
                    "lat": "29.922446",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357758",
                    "lat": "29.922446",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357513",
                    "lat": "29.922015",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357712",
                    "lat": "29.922365",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357407",
                    "lat": "29.921829",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357407",
                    "lat": "29.921829",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35739",
                    "lat": "29.921799",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357554",
                    "lat": "29.922087",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357407",
                    "lat": "29.921829",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357407",
                    "lat": "29.921829",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357355",
                    "lat": "29.921737",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357355",
                    "lat": "29.921737",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.3573",
                    "lat": "29.921641",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357413",
                    "lat": "29.921839",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357355",
                    "lat": "29.921737",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357355",
                    "lat": "29.921737",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35721",
                    "lat": "29.921484",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.35721",
                    "lat": "29.921484",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357475",
                    "lat": "29.921358",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357475",
                    "lat": "29.921358",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357456",
                    "lat": "29.92132",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357304",
                    "lat": "29.921649",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35721",
                    "lat": "29.921484",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357475",
                    "lat": "29.921358",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357434",
                    "lat": "29.921277",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 252,
        "position": [
            {
                "lng": "103.356984",
                "lat": "29.921064",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.357401",
                "lat": "29.920921",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.356984",
                    "lat": "29.921064",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357301",
                    "lat": "29.920955",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.356984",
                    "lat": "29.921064",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357401",
                    "lat": "29.920921",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357078",
                    "lat": "29.921032",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357401",
                    "lat": "29.920921",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.357384",
                    "lat": "29.920927",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.357401",
                    "lat": "29.920921",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 253,
        "position": [
            {
                "lng": "103.363075",
                "lat": "29.917459",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.362551",
                "lat": "29.91772",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.360787",
                "lat": "29.919192",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.36031",
                "lat": "29.919528",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.360215",
                "lat": "29.919587",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.360245",
                    "lat": "29.919568",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360215",
                    "lat": "29.919587",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360403",
                    "lat": "29.919463",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36031",
                    "lat": "29.919528",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360215",
                    "lat": "29.919587",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360727",
                    "lat": "29.919234",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360678",
                    "lat": "29.919268",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360678",
                    "lat": "29.919268",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36046",
                    "lat": "29.919423",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360862",
                    "lat": "29.91913",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360787",
                    "lat": "29.919192",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360787",
                    "lat": "29.919192",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360678",
                    "lat": "29.919268",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360678",
                    "lat": "29.919268",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360588",
                    "lat": "29.919332",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361056",
                    "lat": "29.918967",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360787",
                    "lat": "29.919192",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360787",
                    "lat": "29.919192",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360756",
                    "lat": "29.919214",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361299",
                    "lat": "29.918765",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361162",
                    "lat": "29.918879",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361546",
                    "lat": "29.918559",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361415",
                    "lat": "29.918668",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361754",
                    "lat": "29.918385",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361589",
                    "lat": "29.918523",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.361946",
                    "lat": "29.918225",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361673",
                    "lat": "29.918453",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362048",
                    "lat": "29.91814",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.361861",
                    "lat": "29.918296",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362261",
                    "lat": "29.917962",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362013",
                    "lat": "29.918169",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362473",
                    "lat": "29.917785",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362156",
                    "lat": "29.918049",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362613",
                    "lat": "29.917689",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362551",
                    "lat": "29.91772",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362551",
                    "lat": "29.91772",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36228",
                    "lat": "29.917946",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36273",
                    "lat": "29.917631",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362551",
                    "lat": "29.91772",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362551",
                    "lat": "29.91772",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.36247",
                    "lat": "29.917788",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362951",
                    "lat": "29.917521",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362655",
                    "lat": "29.917668",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362551",
                    "lat": "29.91772",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362439",
                    "lat": "29.917814",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362764",
                    "lat": "29.917614",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362551",
                    "lat": "29.91772",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362551",
                    "lat": "29.91772",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362296",
                    "lat": "29.917933",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.362551",
                    "lat": "29.91772",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.362304",
                    "lat": "29.917926",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 254,
        "position": [
            {
                "lng": "103.360192",
                "lat": "29.919601",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.360167",
                "lat": "29.919617",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.358991",
                "lat": "29.92028",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.359081",
                    "lat": "29.920229",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358991",
                    "lat": "29.92028",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359354",
                    "lat": "29.920075",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358991",
                    "lat": "29.92028",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359837",
                    "lat": "29.919803",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359531",
                    "lat": "29.919976",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.359906",
                    "lat": "29.919764",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359606",
                    "lat": "29.919933",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.36011",
                    "lat": "29.919649",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359826",
                    "lat": "29.919809",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360192",
                    "lat": "29.919601",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360167",
                    "lat": "29.919617",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360167",
                    "lat": "29.919617",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.359964",
                    "lat": "29.919732",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.360167",
                    "lat": "29.919617",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.360104",
                    "lat": "29.919653",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    },
    {
        "deviceId": 255,
        "position": [
            {
                "lng": "103.358968",
                "lat": "29.920293",
                "altitude": 'null',
                "time": 'null'
            },
            {
                "lng": "103.358617",
                "lat": "29.920491",
                "altitude": 'null',
                "time": 'null'
            }
        ],
        "completion": [
            [
                {
                    "lng": "103.358808",
                    "lat": "29.920383",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35879",
                    "lat": "29.920393",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.35879",
                    "lat": "29.920393",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358617",
                    "lat": "29.920491",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358968",
                    "lat": "29.920293",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358643",
                    "lat": "29.920477",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.358968",
                    "lat": "29.920293",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.35879",
                    "lat": "29.920393",
                    "altitude": 'null',
                    "time": 'null'
                }
            ],
            [
                {
                    "lng": "103.35879",
                    "lat": "29.920393",
                    "altitude": 'null',
                    "time": 'null'
                },
                {
                    "lng": "103.358753",
                    "lat": "29.920414",
                    "altitude": 'null',
                    "time": 'null'
                }
            ]
        ],
        "noCompletion": []
    }
]

dict_res = {}

for i in coord:
    dict_res[i['deviceId']] = i['completion']

with open('test.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['deviceId', 'x', 'y'])
    for key, value in dict_res.items():
        if len(value) > 0:
            rows = []
            for coord in value:
                for p in coord:
                    writer.writerow([key, p['lng'], p['lat']])
input_filename = 'test.csv'
output_filename = 'output.csv'

df = pd.read_csv(input_filename)
df.dropna(how='all', inplace=True)  # 删除所有元素都是NaN的行
df.to_csv(output_filename, index=False)
