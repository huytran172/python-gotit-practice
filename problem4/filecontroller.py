from storefront import StorefrontConfig
import json, time, re

class FileController:

    @staticmethod
    def read_file(file_name: str) -> StorefrontConfig:
        with open(file_name, 'r') as myfile:
            data = myfile.read()

        # Remove trailing space after the last object 
        data = re.sub('\,(?=\s*?[\}\]])','' ,data.rstrip())
        parsed_dict = json.loads(data)

        return StorefrontConfig(parsed_dict)


    @staticmethod
    def write_file(object: StorefrontConfig, file_name: str):
        fp = open(file_name, 'w')
        data_str = json.dumps(object.data, sort_keys=True, indent=4, separators=(',', ': '))
        fp.write(data_str)
        fp.close()

modify_data = {
        "expiration_time": 200,
        "product": "qchat",
        "utm_campaign": str(time.time()),
        "storefront": {
            "banner_enabled": False,
            "purchase_options": [
            {
                "button_text": "Dynamic offer 1 - button_text",
                "description": "Dynamic offer 1 - description",
                "id": "",
                "price": "99.99",
                "price_text": "price_text",
                "session_count": "0",
                "subtitle": "Dynamic offer - subtitle",
                "title": "Dynamic offer - title",
                "suffix": "Dynamic offer - suffix",
                "trial_duration": 0,
                "min_member_count": 1,
                "max_member_count": 1,
                "action": "purchase",
                "frequency_view": "monthly",
                "free_learning_subscription": False,
                "team_type": "personal",
                "frequency": None,
            }
        ]
    }
}

if __name__ == '__main__':
    config = FileController.read_file("data.json")
    config.update(modify_data)
    FileController.write_file(config, "result.json")