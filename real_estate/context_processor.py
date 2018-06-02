def site_details(request):
    context_data = dict()
    context_data['custom_site_name'] = "Real Estate"
    context_data['custom_site_author'] = "Jerry Shikanga"
    context_data['custom_site_keywords'] = "real estate, project"
    context_data['custom_site_telephone'] = '254700-000-000'
    context_data['custom_site_email'] = 'info@shikanga.me'
    context_data['custom_site_address'] = '116, Juja, Kenya'
    return context_data
