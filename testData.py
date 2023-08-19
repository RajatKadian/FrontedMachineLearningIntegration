# import requests
#
# # Assuming you have input_data as a dictionary
# input_data = {
#     'length': [44.301529],
#     'weight': [9.439796e-01],
#     'count': [612.683711],
#     'looped': [107.881919],
#     'neighbors': [2.238271],
#     'income': [8.689590e+08]
# }
#
# # Make a POST request to the Flask API to get predictions
# response = requests.post('http://127.0.0.1:5000/predict', json={'data': input_data})
#
# # Check the response status
# if response.status_code == 200:
#     # Get the predictions from the response
#     predictions = response.json()['predictions']
#     print("Predictions:", predictions)
#     print(predictions)
# else:
#     print("Failed to get predictions. Status Code:", response.status_code)
import random


def package_version(package_list):
    package_versions = {}

    for package in package_list:
        package_name = package[0]
        version = package[1]

        if package_name in package_versions:
            print("hello", package_name)
            # package_versions[package_name].append(version)
        else:
            package_versions[package_name] = [version]

    return package_versions


# Create two lists of lists, each containing 5 elements
package_list_1 = [
    ["numpy", "1.21.0"],
    ["pandas", "1.3.2"],
    ["matplotlib", "3.4.3"],
    ["scikit-learn", "0.24.2"],
    ["requests", "2.26.0"]
]

# Random shuffle is removed from here
# random.shuffle(package_list_1)

package_list_2 = package_list_1 + [['pandas', '1.4.2']]
# print(package_list_2)

# Create a new dictionary to store the result
result_dict_1 = package_version(package_list_1)
print(result_dict_1)
