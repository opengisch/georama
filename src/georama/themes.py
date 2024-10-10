from georama.clogs.interfaces.geomapfish import load_geoportal_config_from_path
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

config = load_geoportal_config_from_path("/home/kalle/projects/opengis/georama/scratch_2.json")
serializer_config = SerializerConfig(indent="  ")
print(JsonSerializer(serializer_config).render(config.themes[3].unique_layers_and_groups.layers))
