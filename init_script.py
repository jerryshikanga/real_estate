def main () :
    from property.models import SaleType, BuildingType

    buildingtypes = []
    buildingtypes.append({"name": "Apartment", "description": "These are apartments"})
    buildingtypes.append({"name": "Bungalow", "description": "These are bungalows"})
    buildingtypes.append({"name": "Mansion", "description": "These are mansions"})
    buildingtypes.append({"name": "Skyscraper", "description": "These are skyscrapers"})

    saletypes = []
    saletypes.append({"name": "Rent", "description": "Leased for a period of time only"})
    saletypes.append({"name": "Sale", "description": "your forever"})

    for type in buildingtypes:
        obj = BuildingType.objects.create(
            name=type.get("name"),
            description=type.get("description")
        )
        obj.save()

    for type in saletypes:
        obj = SaleType.objects.create(
            name=type.get("name"),
            description=type.get("description")
        )
        obj.save()


if __name__ == '__main__':
    main()