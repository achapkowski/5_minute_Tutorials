from arcgis.gis import GIS

gis = GIS(profile='your_enterprise_profile', verify_cert=False, trust_env=True)

servers = gis.admin.servers.list()
for server in servers:
    for service in server.services.list():
        if service.properties.type.lower() == "imageserver" and \
           service.properties.minInstancesPerNode >= 1:
            edit_values = dict(service.properties)
            edit_values['minInstancesPerNode'] = 0
            result = service.edit(edit_values)
            if result:
                print(f'modified: {service.properties.serviceName}')
            else:
                print(f'service not modified: {service.properties.serviceName}')
    del server

