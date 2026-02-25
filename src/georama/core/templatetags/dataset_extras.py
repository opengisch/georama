from django import template
from qgis_server_light.interface.qgis import Custom, DataSet, Raster, Vector

register = template.Library()


@register.simple_tag
def icon_by_dataset(dataset: Vector | Raster | Custom):
    if isinstance(dataset, Vector):
        return "fa fa-bezier-curve"
    elif isinstance(dataset, Raster):
        return "fa fa-th"
    elif isinstance(dataset, Custom):
        return "fa fa-asterisk"
    else:
        return "fa fa-question"


@register.simple_tag
def sort_dataset_list_by_title(datasets: list[DataSet]):
    return sorted(datasets, key=lambda d: d.title.casefold())
