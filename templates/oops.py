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
