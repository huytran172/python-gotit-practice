
def updateHelper(data: object, modify_data: object):
    if isinstance(data, dict):
        for key, value in modify_data.items():
            if key in data and isinstance(data[key], dict):
                updateHelper(data[key], value)
            else:
                data[key] = value
        return data 


class StorefrontConfig:

    def __init__(self, data: object):
        self.data = data

    def update(self, modify_data: object):
        self.data = updateHelper(self.data, modify_data)

        


