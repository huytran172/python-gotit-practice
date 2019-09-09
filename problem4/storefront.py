
def updateHelper(data: object, modify_data: object):
    if isinstance(data, dict):
        for key, value in modify_data.items():
            if key in data:
                data[key] = value
        for key, value in data.items():
            return {key: updateHelper(value, modify_data)}
    else:
        return data 

class StorefrontConfig:

    def __init__(self, data: object):
        self.data = data

    def update(self, modify_data: object):
        print(self.data)
        print(modify_data)
        self.data = updateHelper(self.data, modify_data)

        


