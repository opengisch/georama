class ServerConfig:
    def get(self) -> dict:
        return {
            "server": {
                "url": "OVERWRITTEN AT RUNTIME",
                "mimetype": "application/json; charset=UTF-8",
                "encoding": "utf-8",
                "gzip": False,
                "languages": ["en-US", "fr-CA"],
                "pretty_print": True,
                "limit": 10,
                "map": {
                    "url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                    "attribution": '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>',
                },
            },
            "logging": {"level": "INFO"},
            "metadata": {
                "identification": {
                    "title": {
                        "en": "pygeoapi default instance",
                        "fr": "instance par défaut de pygeoapi",
                    },
                    "description": {
                        "en": "pygeoapi provides an API to geospatial data",
                        "fr": "pygeoapi fournit une API aux données géospatiales",
                    },
                    "keywords": {
                        "en": ["geospatial", "data", "api"],
                        "fr": ["géospatiale", "données", "api"],
                    },
                    "keywords_type": "theme",
                    "terms_of_service": "https://creativecommons.org/licenses/by/4.0/",
                    "url": "https://example.org",
                },
                "license": {
                    "name": "CC-BY 4.0 license",
                    "url": "https://creativecommons.org/licenses/by/4.0/",
                },
                "provider": {"name": "Organization Name", "url": "https://opengis.ch"},
                "contact": {
                    "name": "Clemens, Rudert",
                    "position": "Scruffy",
                    "address": "clemens@opengis.ch",
                    "city": "Basel",
                    "stateorprovince": "Basel-Stadt",
                    "postalcode": "4058",
                    "country": "Switzerland",
                    "phone": "+xx-xxx-xxx-xxxx",
                    "fax": "+xx-xxx-xxx-xxxx",
                    "email": "clemens@opengis.ch",
                    "url": "https://opengis.ch",
                    "hours": "Mo-Fr 08:00-17:00",
                    "instructions": "During hours of service. Off on weekends.",
                    "role": "pointOfContact",
                },
            },
            "resources": {},
        }
