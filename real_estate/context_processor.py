from django.conf import settings
from  property.models import BuildingType, SaleType


def site_details(request):
    context_data = dict()
    context_data['custom_site_name'] = "Real Estate"
    context_data['custom_site_author'] = "Jerry Shikanga"
    context_data['custom_site_keywords'] = "real estate, project"
    context_data['custom_site_telephone'] = '254700-000-000'
    context_data['custom_site_email'] = 'info@shikanga.me'
    context_data['custom_site_address'] = '116, Juja, Kenya'

    # context_data['MEDIA_URL'] = settings.MEDIA_URL
    context_data['property_sale_type_list'] = SaleType.objects.all()
    context_data['property_building_type_list'] = BuildingType.objects.all()

    context_data['MEDIA_URL'] = settings.MEDIA_URL

    return context_data
