def display_resources(resources):
    if len(resources) == 0:
        print("No resources available")
        return

    print("ID | Name | Category | Quantity")

    for resource in resources:
        print(resource[0], "|", resource[1], "|",
              resource[2], "|", resource[3])


def search_by_id(resources, resource_id):
    for resource in resources:
        if resource[0] == resource_id:
            print("Resource found:", resource)
            return

    print("Resource ID not found")


def search_by_category(resources, category):
    found = False

    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource)
            found = True

    if found == False:
        print("No resource found in this category")


def find_unavailable(resources):
    found = False

    for resource in resources:
        if resource[3] == 0:
            print("Unavailable resource:", resource)
            found = True

    if found == False:
        print("No unavailable resources found")


def validate_resources(resources):
    valid_resources = []

    for resource in resources:
        if len(resource) != 4:
            print("Invalid resource record:", resource)

        elif not isinstance(resource[3], (int, float)):
            print("Invalid quantity for ID:", resource[0])

        elif resource[3] < 0:
            print("Negative quantity is not allowed:", resource[0])

        else:
            valid_resources.append(resource)

    return valid_resources


resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

print("===== ALL RESOURCES =====")
display_resources(resources)

print("\n===== SEARCH BY CATEGORY =====")
search_by_category(resources, "Electronics")

print("\n===== UNAVAILABLE RESOURCES =====")
find_unavailable(resources)

print("\n===== SEARCH UNKNOWN ID =====")
search_by_id(resources, 999)

print("\n===== TEST NEGATIVE QUANTITY =====")

test_resources = resources + [
    [106, "Speaker", "Audio", -2]
]

validate_resources(test_resources)

print("\n===== TEST EMPTY RESOURCE LIST =====")

empty_resources = []

display_resources(empty_resources)
search_by_category(empty_resources, "Audio")
find_unavailable(empty_resources)